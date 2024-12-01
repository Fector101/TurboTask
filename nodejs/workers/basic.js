/**
 * TurboTask CSS Processing Module
 * Handles CSS minification operations
 * 
 * @module workers/basic
 */

/**
 * Remove whitespace from CSS while preserving functionality
 * @param {string} code - CSS content to process
 * @returns {string} Minified CSS content
 */
function myStrip(code) {
    let newStr = '';
    let removeSpace = false;
    let i = 0;
    let lengthOfStr = code.length;
    const checkpoints = ['{', ':', ';', '}'];

    code = code.replace(/\r?\n|\r/g, '');  // Removing new lines

    // Process each character
    for (let char of code) {
        if (checkpoints.includes(char)) {
            removeSpace = true;
            newStr = newStr.trim();  // Removing trailing spaces

            if (char === '{') {
                newStr += char;
            } else if (char === '}' && newStr[newStr.length - 1] === '{') {
                // Handle empty rule sets
                const indexOfLastClosedBraces = newStr.lastIndexOf('}');
                if (indexOfLastClosedBraces !== -1) {
                    newStr = newStr.substring(0, indexOfLastClosedBraces + 1);
                } else {
                    newStr += char;
                }
            } else {
                newStr += char;
            }
        } else if ((char === '/' && i + 1 !== lengthOfStr && code[i + 1] === '*') || 
                   (char === '*' && i - 1 !== -1 && code[i - 1] === '/')) {
            // Handle comment start
            newStr = newStr.trim();  // Stripping trailing whitespace when not adding semicolon
            newStr += char;
            removeSpace = true;
        } else if ((char === '*' && i + 1 !== lengthOfStr && code[i + 1] === '/') || 
                   (char === '/' && i - 1 !== -1 && code[i - 1] === '*')) {
            // Handle comment end
            newStr += char;
            removeSpace = true;
        } else if (char === ' ' && removeSpace) {
            // Skip space when flagged for removal
        } else {
            removeSpace = false;
            newStr += char;
        }
        i++;
    }
    return newStr;
}

/**
 * Remove CSS comments while preserving code structure
 * @param {string} code - CSS content to process
 * @returns {string} CSS content without comments
 */
function removeComments(code) {
    if (!code.includes('/*')) {
        return code;
    }
    
    let newStr = '';
    let foundCommentEnd = true;
    let i = 0;

    // Check if comment structure is valid
    if ((code.match(/\/\*/g) || []).length !== (code.match(/\*\//g) || []).length) {
        return code;  // Return the code as it is if the comments are mismatched
    }

    // Process each character
    for (let char of code) {
        if (char === '/' && i + 1 !== code.length && code[i + 1] === '*') {
            foundCommentEnd = false;
        } else if ((char === '*' && i + 1 !== code.length && code[i + 1] === '/') || 
                   (char === '/' && i - 1 !== -1 && code[i - 1] === '*')) {
            foundCommentEnd = true;
        } else if (foundCommentEnd) {
            newStr += char;
        }
        i++;
    }

    // Handle empty selectors and fragments
    const listForEmptyReturn = ['/', '*', '{'];
    if (listForEmptyReturn.some(item => item.replace(' ', '') === newStr)) {
        return '';
    } else {
        return newStr;
    }
}


function moveFileToDirectory(src, destDir) {
    const fileName = path.basename(src)
    let dest = path.join(destDir, fileName)
  
    // Check if the file already exists in the destination directory
    let counter = 1
    while (fs.existsSync(dest)) {
        const extname = path.extname(fileName) // gets extension name
        const basename = path.basename(fileName, extname) // get actual file name
        const newFileName = `${basename} (${counter})${extname}`
        dest = path.join(destDir, newFileName)
        counter++
    }
  
    // This try's to move or rename and move the file
    fs.rename(src, dest, (err) => {
        if (err) {
            console.error('Error moving the file:', err)
        } else {
            console.log(`File moved to: ${dest}`)
        }
    })
}
  
function deleteEmptyFolders(dirPath) {
    // Read the contents of the directory
    fs.readdir(dirPath, (err, files) => {
      if (err) {
        console.error('Error reading directory:', err);
        return;
      }
  
      // Iterate over the files and subdirectories in the directory
      files.forEach((file) => {
        const filePath = path.join(dirPath, file);
        
        // If it's a directory, recursively call deleteEmptyFolders
        fs.stat(filePath, (err, stats) => {
          if (err) {
            console.error('Error checking file stats:', err);
            return;
          }
  
          if (stats.isDirectory()) {
            // Recursively delete empty folders inside this directory
            deleteEmptyFolders(filePath);
          }
        });
      });
  
      // After checking subdirectories, check if the current directory is empty
      fs.readdir(dirPath, (err, files) => {
        if (files.length === 0) {
          // If it's empty, remove the directory
          fs.rmdir(dirPath, (err) => {
            if (err) {
              console.error('Error removing directory:', err);
            } else {
              console.log(`Removed empty directory: ${dirPath}`);
            }
          });
        }
      });
    });
}
  



// // Export a simpler version for the module
// module.exports.removeComments = function (css) {
//     return css.replace(/\/\*.*?\*\//gs, '');
// }


// const myStrip = function(css) {
//     return css
//     // First, remove spaces around the CSS braces, colons, and semicolons
//     .replace(/\s*({|}|:|;)\s*/g, '$1')
//     // Then, preserve spaces between selectors, but remove spaces inside the selector or rule
//     .replace(/(?<=\S)\s+(?=\S)/g, ''); 
// }
module.exports={removeComments, myStrip}