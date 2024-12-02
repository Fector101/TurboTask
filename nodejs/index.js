#!/usr/bin/env node

/**
 * TurboTask File Processing Toolkit
 * Main entry point for the application
 * 
 * @module index
 */
const fs = require('fs')
const path = require('path');
const { Command } = require("commander")
const { description, version } = require('./package.json');
const { 
    greenText, redText,
    createDirectory, readFile, writeFile,
    deleteEmptyFolders,moveFileToDirectory,
    failSafeRootPath,logErrors,formattedDate,
    Progress  
    } = require("./helper")
const { removeComments, myStrip} = require('./workers/basic')
const folders_to_ignore = ['node_modules', '.git','venv','myvenv','env']


/**
 * Process a single CSS file
 * @param {string} inputFilePath - Path to the input CSS file || CSS Folder Path
 * @param {string} outputFilePath - Path where the processed file will be saved
*/
//  * @param {boolean} [removeCommentsFlag=true] - Whether to remove comments
function noWhiteSpace(inputFilePath, outputFilePath) {
    // Error Checking for when function is imported directly
    inputFilePath = [" ", ""].includes(inputFilePath) ? "./" : inputFilePath
    if (!fs.existsSync(inputFilePath)) {
        console.error(`${redText(inputPath)} does not exist.`)
        return
    }
    // Point to Another Function If Folder Path Passed In.
    if (fs.lstatSync(inputFilePath).isDirectory()) {
        processDirectory(inputFilePath, outputFilePath)
        return
    }

    let cssContent = readFile(inputFilePath);
    if (!cssContent) return;

    // if (removeCommentsFlag) {
    cssContent = removeComments(cssContent);
    // }

    cssContent = myStrip(cssContent);

    writeFile(
        cssContent,
        outputFilePath,
        `Successfully Created a File without WhiteSpace in ${greenText(outputFilePath)}`,
        `Failed to write File Output in '${redText(outputFilePath)}'`
    );
}

/**
 * Process a directory of CSS files
 * @param {string} inputDir - Path to the input directory
 * @param {string} [outputDir='TurboTask-output'] - Path where processed files will be saved
 */
function processDirectory(inputDir, outputDir = 'TurboTask-output') {
    const inputDirectoryPath = path.resolve(inputDir);
    const outputDirectoryPath = path.resolve(outputDir);

    function isNodeModulesPath(path) {
        const nm_str = 'node_modules'
        const index_of_node_modules_str = __dirname.lastIndexOf(nm_str)
        if (index_of_node_modules_str === -1) {
            return false
        } else {
            return path === __dirname.slice(0, nm_str.length + index_of_node_modules_str)
        }
    }

    // const paths_to_ignore=[ 'node_modules' ]

    // if (!fs.existsSync(outputDirectoryPath)) {
    //   createDirectory(outputDirectoryPath);
    // }

    fs.readdirSync(inputDirectoryPath, { withFileTypes: true }).forEach((entry) => {
        const fullPath = path.join(inputDirectoryPath, entry.name);

        if (!folders_to_ignore.includes(entry.name) && entry.isDirectory() && path.resolve(fullPath) !== outputDirectoryPath) {
            // If the entry is a directory, recurse into it
            processDirectory(fullPath, path.join(outputDirectoryPath, entry.name));
        } else if (entry.isFile() && entry.name.endsWith('.css')) {

            if (!fs.existsSync(outputDirectoryPath)) {
                createDirectory(outputDirectoryPath);
            }
            // If the entry is a CSS file, process it
            const relativePath = path.relative(inputDirectoryPath, fullPath);
            const outputFilePath = path.join(outputDirectoryPath, relativePath);
            noWhiteSpace(fullPath, outputFilePath);
        }
    });
}


//  * @param {string} [format='*'] - If not provided for function, function arranges all formats

/**
 * Recursively proccess a directory and Moves each format to a certain folder in base Directory or given dir
 * @param {string} [Basedir='./'] - Path To start the Scan
 */
function groupFormat(Basedir = './') {
// function groupFormat(Basedir = './',format = '') {
    // TODO group only a specified format
    console.log(`Root Folder: ${path.resolve('./')}`)
    let folders = [Basedir]
    let current_folder = folders[0]
    let list_of_filesNdFolders = fs.readdirSync(current_folder)
    // console.log(list_of_filesNdFolders)
    const task_progress = new Progress()
    task_progress.start(0)
    // return
    let errors_count=0
    let errors=[]

    function updateErrorInfo(error,file_path){
        errors_count+=1
        

        let err_name='UnknownError '
        if(error.code==='ENOENT'){
            err_name='No such file or directory '
        }else if(error.code=== 'EACCES'){
            err_name='Permission denied '
        }
        errors.push({
            name: err_name,
            code: error.code || "UnknownCode",
            message: error.message || "No message available",
            location: file_path,
            time: formattedDate()
        })
        task_progress.updateErrorCount(errors_count)
    }


    while (folders.length) {
        for (let each of list_of_filesNdFolders) {
            const current_path = path.join(current_folder, each)
            
            let stats_ = undefined
            try{stats_ = fs.statSync(current_path)}
            catch(err){//Should be file moved or permission error
                updateErrorInfo(err,current_path)
                continue
            }
            if (stats_.isDirectory()) {
                let has_files_in_it = false
                try {
                    has_files_in_it = fs.readdirSync(current_path).length
                }
                catch (err) { // Incase i can't read dir
                    // console.log('Error reading folder', err)
                    updateErrorInfo(err,current_path)
                    has_files_in_it = 0
                }
                const group_in_name = current_path.startsWith('group')
                if (has_files_in_it && !group_in_name && !folders_to_ignore.includes(each)) {
                    // console.log(current_path)
                    folders.push(current_path)
                    task_progress.updateTotal(1)
                }else if(!has_files_in_it){
                    deleteEmptyFolders(current_path)
                }
            }
            else {
                const folder_name = `group ${each.slice(each.lastIndexOf('.'))}`.trim()

                if (!fs.existsSync(folder_name)) {
                    fs.mkdirSync(folder_name)
                    // console.log('making folder')
                }
                try {
                    // console.log('moving file ',each)
                    const running_frm_script_path=process.argv[1]
                    if(running_frm_script_path !== path.resolve(current_folder, path.basename(current_path) ) ){
                        // Fail safe from then package is required and not ran from terminal
                        moveFileToDirectory(current_path, folder_name);
                    }
                }
                catch (err) { 
                    updateErrorInfo(err,current_path)   // TODO await function in helper.js and throw error
                    // console.log('moving file error', err) 
                }
            }
        }
        folders.shift()
        current_folder = folders[0]
        if(current_folder){
            // console.log(current_folder,'|||')
            task_progress.increment()
            list_of_filesNdFolders = fs.readdirSync(current_folder)
        }

    }
    task_progress.stop()
    console.log('Done !!!')
    errors_count && logErrors(errors,Basedir)
}

if (require.main === module) {

    const program = new Command();
    program
        .version(version)
        .description(`${description}\nTurboTask: A versatile Node.js toolkit for file processing operations. Currently supports CSS minification with plans for expanded functionality`)
        .helpOption('-h, --help', 'display help for command');

    //commands
    program.command('noWhiteSpace <input_css_path> [output_path]')
        .description('Removes whitespace from CSS file or All CSS Files in Given Dir')
        .action((inputCssFilePath, outputFilePath = 'TurboTask-output') => {

            inputCssFilePath = failSafeRootPath(inputCssFilePath)

            if (fs.existsSync(inputCssFilePath)) {
                outputFilePath = path.join(outputFilePath, path.basename(inputCssFilePath));
                noWhiteSpace(inputCssFilePath, outputFilePath);
            } else {
                console.error(`${redText(inputCssFilePath)} does not exist.`);
            }
        });

    // program.command('group [Basedir] [format]')
    program.command('group [Basedir]')
        .description('Groups Files According to Format in Separate Folders')
        .action((Basedir = './') => {
        // .action((Basedir = './', format='') => {

            Basedir = failSafeRootPath(Basedir)

            if (fs.existsSync(Basedir)) {
                groupFormat(Basedir);
            } else {
                console.error(`${redText(Basedir)} does not exist.`);
            }
        });

    // Parse the command-line arguments
    program.parse(process.argv);
}


module.exports = { noWhiteSpace,groupFormat }