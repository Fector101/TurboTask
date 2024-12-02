#!/usr/bin/env node

/**
 * TurboTask File Processing Toolkit
 * Main entry point for the application
 * 
 * @module index
 */
const fs = require('fs')
const path = require('path');
const {Command} = require("commander")
const { description, version } = require('./package.json');

const {greenText,redText,createDirectory,readFile,writeFile} = require("./helper")
const {removeComments, myStrip} = require('./workers/basic')
const folders_to_ignore=[ 'node_modules', '.git']


/**
 * Process a single CSS file
 * @param {string} inputFilePath - Path to the input CSS file || CSS Folder Path
 * @param {string} outputFilePath - Path where the processed file will be saved
 * @param {boolean} [removeCommentsFlag=true] - Whether to remove comments
 */
function noWhiteSpace(inputFilePath, outputFilePath, removeCommentsFlag = true) {
  // Error Checking for when function is imported directly
  inputFilePath=[" ",""].includes(inputFilePath) ? "./":inputFilePath
  if(!fs.existsSync(inputFilePath)){
    console.error(`${redText(inputPath)} does not exist.`)
    return
  }
  // Point to Another Function If Folder Path Passed In.
  if (fs.lstatSync(inputFilePath).isDirectory()){
    processDirectory(inputFilePath, outputFilePath)
    return
  }

  let cssContent = readFile(inputFilePath);
  if (!cssContent) return;

  if (removeCommentsFlag) {
    cssContent = removeComments(cssContent);
  }

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

  function isNodeModulesPath(path){
    const nm_str='node_modules'
    const index_of_node_modules_str=__dirname.lastIndexOf(nm_str)
    if(index_of_node_modules_str === -1){
      return false
    }else{
      return path === __dirname.slice(0,nm_str.length + index_of_node_modules_str)
    }
  }

  // const paths_to_ignore=[ 'node_modules' ]

  // if (!fs.existsSync(outputDirectoryPath)) {
  //   createDirectory(outputDirectoryPath);
  // }

  fs.readdirSync(inputDirectoryPath, { withFileTypes: true }).forEach((entry) => {
    const fullPath = path.join(inputDirectoryPath, entry.name);

    if ( !folders_to_ignore.includes(entry.name) && entry.isDirectory() && path.resolve(fullPath) !== outputDirectoryPath) {
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


/**
 * Recursively proccess a directory and Moves each format to a certain folder in base Directory or given dir
 * @param {string} [format='*'] - If not provided for function, function arranges all formats
 * @param {string} [Basedir='./'] - Path To start the Scan
 */
function groupFormat(format='',Basedir='./'){
    
    let folders = [Basedir]
    while (folders.length){
        const current_folder=folders[0]
        const list_of_filesNdFolders=fs.readdirSync(current_folder)
        
        for (const each in list_of_filesNdFolders){
            const current_path = path.join(current_folder ,each)
            const stats_= fs.statSync(filePath)
            if (stats_.isDirectory){
                    let has_files_in_it=false
                    try{
                        has_files_in_it = fs.readdirSync(current_path).length
                    }
                    catch(err){ // Incase i can't read dir
                      console.log('Error reading folder',e)
                        has_files_in_it=0
                    }
                    const group_in_name= current_path.startsWith('group')
                    if (has_files_in_it && !group_in_name && !folders_to_ignore.includes(each)){
                        folders.append(current_path)
                    }
            }
            else{
                const folder_name = `group ${each.slice(each.lastIndexOf('.'))}`.trim()
                
                if (!fs.existsSync(folder_name)){
                    // fs.mkdirSync(folder_name)
                    console.log('making folder')
                }
                try{
                  console.log('moving file')
                    // moveFileToDirectory(current_path, folder_name);
                }
                catch(err){console.log('moving file error',err)}
            }
        }
        
        folders.shift()
        deleteEmptyFolders(currentPath)

    }
}


if(require.main === module){

  const program = new Command();
  program
      .version('0.2.14')
      .description(`${description}\nTurboTask: A versatile Node.js toolkit for file processing operations. Currently supports CSS minification with plans for expanded functionality`)
      // .version(version, '-V, --version', 'output the version number')
      .helpOption('-h, --help', 'display help for command');

      //commands
      program.command('noWhiteSpace <input_css_path> [output_path]')
      .description('Removes whitespace from CSS file or All CSS Files in Given Dir')
      .action((inputCssFilePath, outputFilePath = 'TurboTask-output') => {

        inputCssFilePath=[" ",""].includes(inputCssFilePath) ? "./":inputCssFilePath

        if (fs.existsSync(inputCssFilePath)) {
            outputFilePath = path.join(outputFilePath, path.basename(inputCssFilePath));
            noWhiteSpace(inputCssFilePath, outputFilePath);
        } else {
          console.error(`${redText(inputCssFilePath )} does not exist.`);
        }
      });

      // Parse the command-line arguments
      program.parse(process.argv);
}
module.exports={noWhiteSpace}