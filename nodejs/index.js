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
    failSafeRootPath} = require("./helper")
const { removeComments, myStrip, GroupFormat} = require('./workers/classes')


const folders_to_ignore = ['node_modules', '.git','venv','myvenv','env']


/**
 * Process a single CSS file
 * @param {string} inputFilePath - Path to the input CSS file || CSS Folder Path
 * @param {string} outputFilePath - Path where the processed file will be saved
*/
function noWhiteSpace(inputFilePath, outputFilePath) {
    
    // Error Checking for when function is imported directly
    inputFilePath = failSafeRootPath(inputFilePath)

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

    cssContent = removeComments(cssContent);
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


/**
 * Recursively proccess a directory and Moves each format to a certain folder in base Directory or given dir
 * @instance group().then(operation_details=>console.log(operation_details))
 * @param {string} [Basedir='./'] - Path To start the Scan
 * @returns {object} Object of Number of scanned Folders, Moved Files And Object of Errors if any
 */
function group(Basedir= './'){
    const instance_ = new GroupFormat(Basedir)
    return instance_.start()
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
            group(Basedir)
        });

    // Parse the command-line arguments
    program.parse(process.argv);
}


module.exports = { noWhiteSpace, group}