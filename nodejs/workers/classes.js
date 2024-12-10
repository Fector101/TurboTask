/**
 * TurboTask CSS Processing Module
 * Handles CSS minification operations
 * 
 * @module workers/basic
 */


const fs = require('fs')
const path = require('path');
const { 
    deleteEmptyFolders,moveFileToDirectory,
    logErrors,formattedDate,input,
    Progress  
    } = require("../helper")
const folders_to_ignore = ['node_modules', '.git','venv','myvenv','env']

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



/**
 * Recursively proccess a directory and Moves each format to a certain folder in base Directory or given dir
 * @param {string} [Basedir='./'] - Path To start the Scan
 * @returns {object} Object of Number of scanned Folders | And Object of Errors if any
 */
class GroupFormat {
    constructor(Basedir= './') {
        this.Basedir=Basedir
        this.errors_count=0
        this.errors=[]
        this.folders=[]
        this.task_progress = new Progress()
    }
  
    /**
     * Starts groupFormat process
     */
    async start() {
        console.log(`Root Folder: ${path.resolve(this.Basedir)}`)

        const user_input = await this.askToProceed("Enter \"y\" to Proceed or \"n\" to Cancel: ")

        if(user_input !== 'y') return "GoodBye!!!"

        this.folders = [this.Basedir]
        let current_folder = this.folders[0]
        let list_of_filesNdFolders = fs.readdirSync(current_folder)
        let number_of_scanned_folders=0
        let number_of_moved_files=0

        this.task_progress.start(1)
        

        while (this.folders.length) {
            number_of_scanned_folders++
            for (let each of list_of_filesNdFolders) {
            
                const current_path = path.resolve(path.join(current_folder, each))
                let stats_ = undefined
                
                try{stats_ = fs.statSync(current_path)}
                catch(err){ // Error would be because file/folder was moved or permission error
                    this.updateErrorInfo(err,current_path)
                    continue
                }
                
                if (stats_.isDirectory()) {
                    this.addFolderToKeepLoop(current_path,each)
                }
                else {
                    const folder_name = this.createGroupFolder(each)
                    this.moveFile(current_path,folder_name)
                    number_of_moved_files++
                    
                }
            }
    
            deleteEmptyFolders(current_folder)
    
            this.folders.shift()
            current_folder = this.folders[0]
    
            if(current_folder){
                this.task_progress.increment()
                list_of_filesNdFolders = fs.readdirSync(current_folder)
            }
    
        }
        this.task_progress.increment()
        deleteEmptyFolders(this.Basedir)
        this.task_progress.stop()
        console.log('Done !!!')
        this.errors_count && logErrors(this.errors,this.Basedir)
        
        return {
            "Number of scanned folders":number_of_scanned_folders,
            "Number of Moved Files":number_of_moved_files,
            'Errors':this.errors
        }
        
    }
    addFolderToKeepLoop(current_path,each){
        let not_empty = false
        try {not_empty = fs.readdirSync(current_path).length}
        catch (err) { // Incase i can't read dir
            this.updateErrorInfo(err,current_path)
            not_empty = 0
        }
        const group_in_name = each.startsWith('group')
        if (not_empty && !group_in_name && !folders_to_ignore.includes(each)) {
            this.folders.push(current_path)
            this.task_progress.updateTotal(1)
        }
    }
    /**
     * 
     * @param {Error} error - Error Object from Expectation 
     * @param {string} file_path - Path of file
     */
    updateErrorInfo(error,file_path){
        this.errors_count+=1

        let err_name='UnknownError '
        if(error.code==='ENOENT'){
            err_name='No such file or directory '
        }else if(error.code=== 'EACCES'){
            err_name='Permission denied '
        }
        this.errors.push({
            name: err_name,
            code: error.code || "UnknownCode",
            message: error.message || "No message available",
            location: file_path,
            time: formattedDate()
        })
        this.task_progress.updateErrorCount(this.errors_count)
    }
    async askToProceed(que) {
        const user_response = await input(que)
        return user_response.toLocaleLowerCase()
    }

    /**
    * Creates a folder for a certain format
    * @param {string} each - Current Folder name in Loop
    * @returns {string} Folder Name
    */
    createGroupFolder(each){
        const folder_name = path.join(this.Basedir,`group ${each.slice(each.lastIndexOf('.'))}`.trim())
        if (!fs.existsSync(folder_name)) {
            fs.mkdirSync(folder_name)
        }
        return folder_name
    }

    /**
    *  Moves file to Group Folder
    * @param {string} current_path - The files current Path
    * @param {string} folder_name - Path of folder being moved to
    */
    moveFile(current_path,folder_name){
        try {
            // Fail safe from then package is required and not ran from terminal
            const user_script_path=process.argv[1]
            if(user_script_path !== current_path){
                moveFileToDirectory(current_path, folder_name);
            }
        }
        catch (err) { 
            this.updateErrorInfo(err,current_path)   // TODO await function in helper.js and throw error
        }
    }


}



        
        
        
     
    

//  Export a simpler version for the module
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
module.exports={removeComments, myStrip, GroupFormat}