/**
 * TurboTask Helper Utilities
 * Core utility functions for file operations and console formatting
 * 
 * @module helper
 */

const fs = require('fs');
const path = require('path');

/**
 * Format text in green color for console output
 * @param {string} text - Text to be colored
 * @returns {string} ANSI color formatted string
 */
function greenText(text) {
  return `\x1b[32m${text}\x1b[0m`;
}

/**
 * Format text in red color for console output
 * @param {string} text - Text to be colored
 * @returns {string} ANSI color formatted string
 */
function redText(text) {
  return `\x1b[31m${text}\x1b[0m`;
}

/**
 * Create a directory and any necessary parent directories
 * @param {string} directoryPath - Path of the directory to create
 */
function createDirectory(directoryPath) {
  try {
    if (!fs.existsSync(directoryPath)) {
      fs.mkdirSync(directoryPath, { recursive: true });
    }
  } catch (e) {
    console.error(`Failed to create directory '${redText(directoryPath)}': ${e.message}`);
  }
}

/**
 * Read file contents safely with error handling
 * @param {string} inputCssFilePath - Path to the file to read
 * @returns {string|null} File contents or null if operation fails
 */
function readFile(inputCssFilePath) {
  try {
    return fs.readFileSync(inputCssFilePath, 'utf8');
  } catch (e) {
    if (e.code === 'ENOENT') {
      console.error(`<Error - ${redText(inputCssFilePath)} Doesn't Exist>`);
    } else {
      console.error(`${redText(inputCssFilePath)} doesn't exist or cannot be read: ${error.message}`);
    }
    return null;
  }
}

/**
 * Write content to a file with directory creation and error handling
 * @param {string} content - Content to write to file
 * @param {string} filePath - Path where file should be written
 * @param {string} [goodMsg='<Dev> - Default Success Msg'] - Success message
 * @param {string} [errorMsg='<Dev> - Default Error Msg'] - Error message
 */
function writeFile(content, filePath, goodMsg = "<Dev> - Default Success Msg", errorMsg = "<Dev> - Default Error Msg") {
  try {
    const folderPath = path.dirname(filePath);
    if (folderPath) {
      createDirectory(folderPath);
    }
    fs.writeFileSync(filePath, content);
    console.log(goodMsg);
  } catch (e) {
    console.error(errorMsg);
  }
}

module.exports = {
  greenText,
  redText,
  createDirectory,
  readFile,
  writeFile
}