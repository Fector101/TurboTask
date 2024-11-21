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

    // Remove all newlines first
    code = code.replace(/\n/g, '');

    // Process each character
    for (let char of code) {
        if (checkpoints.includes(char)) {
            removeSpace = true;
            newStr = newStr.trim();  // Remove trailing spaces

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
            newStr = newStr.trim();
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

    // Validate comment structure
    if ((code.match(/\/\*/g) || []).length !== (code.match(/\*\//g) || []).length) {
        return code;  // Return original if comments are mismatched
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
    }
    return newStr;
}

// Export a simpler version for the module
module.exports.removeComments = function (css) {
    return css.replace(/\/\*.*?\*\//gs, '');
}

module.exports = {
    removeComments,
    myStrip
}