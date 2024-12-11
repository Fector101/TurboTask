/**
 * TurboTask Helper Utilities
 * Core utility functions for file operations and console formatting
 * 
 * @module helper
 */

const fs = require('fs');
const path = require('path');
const cliProgress = require('cli-progress')
const colors = require('ansi-colors')
const os = require('os');


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
	return `\x1b[31m'${text}'\x1b[0m`;
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

	// This to move's the file
	// try {
    //     fs.renameSync(src, dest);
    // } catch (err) {
    //     throw err
    // }

	fs.rename(src, dest, (err) => {
		if (err) {
			console.error('Error moving the file:', err)
		} else {
			// console.log(`File moved to: ${dest}`)
		}
	})
}



function deleteEmptyFolders(dirPath) {
	// Read the contents of the directory
	try{
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
							// console.error('Error removing directory:', err);
						} else {
							// console.log(`Removed empty directory: ${dirPath}`);
						}
					});
				}
			});
		});
	}catch{}
}


class Progress {
	constructor() {
		this.range = 0
		this.progress_value = 0
		this.progress = new cliProgress.SingleBar({
			format: 'Grouping Formats |' + colors.cyan('{bar}') + '| {percentage}% || {value}/{total} Folders Scanned || errors: {errors}',
			barCompleteChar: '\u2588',
			barIncompleteChar: '\u2591',
			hideCursor: true
		})
	}
	start(range) {
		this.range = range
		this.progress.start(range, 0, { errors: "0" })
	}
	updateTotal(range) {
		this.range = this.range + range
		this.progress.setTotal(this.range)
	}
	increment(increment_no = 1) {
		// update values
		this.progress_value += 1
		this.progress.increment(increment_no)
	}
	stop() {
		this.progress.stop()
	}
	updateErrorCount(errors_no) {
		this.progress.update(this.progress_value, { errors: errors_no });
	}
	// stop the bar
}
/**
 * 
 * @param {string} inputted_path - Unformatted path from user
 * @returns {string} Right Format of Root path or inputted path
 */
function failSafeRootPath(inputted_path) {
	let new_path = inputted_path
	if ([" ", "", '/'].includes(inputted_path)) {
		console.log(colors.yellowBright(`Waring use './' as Based Directory, not '${inputted_path}'`))
		new_path = "./"
	}
	return new_path
}

function logErrors(list_of_errors, base_path) {
	// Save errors to the file
	let errorLogPath = path.resolve(base_path || __dirname, 'error_log.json');
	let hint_message = 'To see error logs Run ' + colors.cyan(`"cat ${errorLogPath}"`)
	function hintMessage() {
		if (os.type().includes('Windows')) {
			hint_message = 'To see error logs Run ' + colors.cyan(`"type ${errorLogPath}"`)
		} else if (os.type().includes('Linux') || os.type().includes('Darwin')) {
			hint_message = 'To see error logs Run ' + colors.cyan(`"cat ${errorLogPath}"`)
		}
		console.log(hint_message)
	}

	try {
		fs.writeFileSync(errorLogPath, JSON.stringify(list_of_errors, null, 2));
	} catch {
		errorLogPath = path.join(os.homedir(), 'Desktop', 'error_log.json');
		fs.writeFileSync(errorLogPath, JSON.stringify(list_of_errors, null, 2));
	}
	hintMessage()
}
function formattedDate(){
	const date = new Date();
	const hours = String(date.getHours()).padStart(2, '0');
	const minutes = String(date.getMinutes()).padStart(2, '0');
	const seconds = String(date.getSeconds()).padStart(2, '0');
	const day = date.toLocaleString('en-US', { weekday: 'long' });
	const dayOfMonth = date.getDate();
	const month = date.toLocaleString('en-US', { month: 'long' });
	const year = date.getFullYear();

	return `${hours}:${minutes}:${seconds}, ${day} ${dayOfMonth} ${month}, ${year}`;
}



const readline = require('readline');
/**
 * For getting Input From User 
 * @param {string} text - Question For User
 * @returns {string} Input from User
 */
function input(text=''){
	return new Promise((resolve, reject) => {
		const rl = readline.createInterface({
		input: process.stdin,
		output: process.stdout
		});
		
		rl.question(text, (user_input) => {
		rl.close();
		resolve(user_input)
		});
	})
	
}	





module.exports = {
	greenText, redText, createDirectory, readFile, writeFile,
	moveFileToDirectory, deleteEmptyFolders,
	failSafeRootPath, logErrors,formattedDate,input,
	Progress
}

