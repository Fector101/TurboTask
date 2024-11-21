/**
 * TurboTask File Processing Toolkit
 * Main entry point for the application
 * 
 * @module index
 */

const fs = require('fs');
const path = require('path');
const readline = require('readline');

const {greenText,redText,createDirectory,readFile,writeFile} = require("./helper")
const {removeComments, myStrip} = require('./workers/basic')


/**
 * Process a single CSS file
 * @param {string} inputFilePath - Path to the input CSS file
 * @param {string} outputFilePath - Path where the processed file will be saved
 * @param {boolean} [removeWhitespace=true] - Whether to remove whitespace
 * @param {boolean} [removeCommentsFlag=true] - Whether to remove comments
 */
function processFile(inputFilePath, outputFilePath, removeWhitespace = true, removeCommentsFlag = true) {
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

  if (!fs.existsSync(outputDirectoryPath)) {
    createDirectory(outputDirectoryPath);
  }

  fs.readdirSync(inputDirectoryPath, { withFileTypes: true }).forEach((entry) => {
    const fullPath = path.join(inputDirectoryPath, entry.name);

    if (entry.isDirectory()) {
      // If the entry is a directory, recurse into it
      processDirectory(fullPath, path.join(outputDirectoryPath, entry.name));
    } else if (entry.isFile() && entry.name.endsWith('.css')) {
      // If the entry is a CSS file, process it
      const relativePath = path.relative(inputDirectoryPath, fullPath);
      const outputFilePath = path.join(outputDirectoryPath, relativePath);
      processFile(fullPath, outputFilePath);
    }
  });
}

// Initialize CLI interface
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

/**
 * Main application entry point
 * Handles user input and initiates file processing
 */
function main() {
  rl.question('Enter the input CSS file or directory path: ', (inputPath) => {
    rl.question('Enter the output Folder (default is "TurboTask-output"): ', (outputPath) => {
      outputPath = outputPath || 'TurboTask-output';

      if (fs.existsSync(inputPath)) {
        if (fs.lstatSync(inputPath).isDirectory()) {
          processDirectory(inputPath, outputPath);
        } else if (fs.lstatSync(inputPath).isFile() && inputPath.endsWith('.css')) {
          const outputFilePath = path.join(outputPath, path.basename(inputPath));
          processFile(inputPath, outputFilePath);
        }
      } else {
        console.error(`${redText(inputPath)} does not exist.`);
      }

      rl.close();
    });
  });
}

main();