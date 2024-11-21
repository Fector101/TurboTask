const fs = require('fs');
const path = require('path');

// Function to color text in green
function greenText(text) {
  return `\x1b[32m${text}\x1b[0m`;
}

// Function to color text in red
function redText(text) {
  return `\x1b[31m${text}\x1b[0m`;
}

// Function to create a directory if it doesn't exist
function createDirectory(directoryPath) {
  try {
    if (!fs.existsSync(directoryPath)) {
      fs.mkdirSync(directoryPath, { recursive: true });
    }
  } catch (e) {
    console.error(`Failed to create directory '${redText(directoryPath)}': ${e.message}`);
  }
}

// Function to read a file asynchronously
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

// Function to write content to a file
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

// Function to remove digits from a string
function parseStr(string) {
  const nums = '0123456789';
  let str_ = '';
  for (const char of string) {
    if (!nums.includes(char)) {
      str_ += char;
    }
  }
  return str_.trim();
}

// Function to parse integer from a string
function parseIntFromStr(string) {
  let ii = '';
  for (const char of string) {
    if (!['-', ' ', '(', ')'].includes(char)) {
      ii += char;
    }
  }
  ii = ii.replace(/[a-zA-Z-]/g, '').trim();
  if (ii === '') {
    return 0;
  }
  return parseInt(ii, 10);
}
module.exports={
  greenText,redText,createDirectory,readFile,writeFile
}