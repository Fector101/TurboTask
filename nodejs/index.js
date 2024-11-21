#!/usr/bin/env node

/**
 * TurboTask File Processing Toolkit
 * Main entry point for the application
 * 
 * @module index
 */
const fs = require('fs');
const path = require('path');
const {Command} = require("commander")
// const readline = require('readline');

const {greenText,redText,createDirectory,readFile,writeFile} = require("./helper")
const {removeComments, myStrip} = require('./workers/basic')


/**
 * Process a single CSS file
 * @param {string} inputFilePath - Path to the input CSS file
 * @param {string} outputFilePath - Path where the processed file will be saved
 * @param {boolean} [removeWhitespace=true] - Whether to remove whitespace
 * @param {boolean} [removeCommentsFlag=true] - Whether to remove comments
 */
function noWhiteSpace(inputFilePath, outputFilePath, removeWhitespace = true, removeCommentsFlag = true) {
  // Error Checking
  inputFilePath=[" ",""].includes(inputFilePath) ? "./":inputFilePath
  if(!fs.existsSync(inputFilePath)){
    console.error(`${redText(inputPath)} does not exist.`)
    return
  }
  if (fs.lstatSync(inputFilePath).isDirectory()){
    processDirectory(inputFilePath, outputFilePath)
    return
  }

  let cssContent = readFile(inputFilePath);
  if (!cssContent) return;

  if (removeCommentsFlag) {
    cssContent = removeComments(cssContent);
  }

  if (removeWhitespace) {
    cssContent = myStrip(cssContent);
  }

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

  const folders_to_ignore=[ 'node_modules' ]
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

if(require.main === module){

  const program = new Command();
  program
      .version('0.2.14')
      .description('TurboTask: A versatile Node.js toolkit for file processing operations. Currently supports CSS minification with plans for expanded functionality')
      .command('noWhiteSpace <input_css_file_path> [output_path]')
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