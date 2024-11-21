# TurboTask File Processing Toolkit

[![npm version](https://img.shields.io/npm/v/turbotask.svg)](https://www.npmjs.com/package/turbotask)
[![License](https://img.shields.io/npm/l/turbotask.svg)](https://github.com/yourusername/turbotask/blob/main/LICENSE)

A versatile Node.js toolkit for file processing operations. Currently supports CSS minification with plans for expanded functionality including file grouping, media duration analysis, and more.

## 🚀 Quick Start

```bash
npm install -g turbotask
```

## ✨ Features

### Current Features

- **CSS Processing**
  - Minify CSS files by removing comments and whitespace
  - Process single files or entire directories
  - Maintain directory structures
  - Safe processing with validation checks

### Planned Features

- File grouping by type
- Media file duration analysis
- More file processing capabilities (coming soon)

## 📦 Installation

### NPM

```bash
npm install -g turbotask
```

### Manual Installation

```bash
# Clone the repository
git clone https://github.com/Fector101/TurboTask.git

# Navigate to the project directory
cd turbotask

# Install dependencies
npm install
```

## 🔨 Usage

Currently, the tool supports CSS processing:

```bash
node index.js
```

The CLI will prompt you for:

1. Input path (file or directory)
2. Output directory (defaults to "TurboTask-output")

### Example

```bash
Enter the input CSS file or directory path: ./styles
Enter the output Folder (default is "TurboTask-output"): ./minified
```

## 🛠️ Core Utilities

### File Operations

#### Directory Management

```javascript
// Create directory (creates parent directories if needed)
createDirectory('./path/to/new/directory');
```

#### File Reading/Writing

```javascript
// Read file
const content = readFile('./path/to/file.css');

// Write file
writeFile(content, './output/path.css', 
  'Success message', 'Error message');
```

### Console Output

The toolkit includes formatted console output with color coding:

```javascript
console.log(greenText('Success!')); // Green colored success message
console.log(redText('Error!')); // Red colored error message
```

## 🏗️ Technical Architecture

### Core Modules

#### Helper Utilities (`helper.js`)

- File system operations
  - `createDirectory()`: Create directories recursively
  - `readFile()`: Safe file reading with error handling
  - `writeFile()`: Safe file writing with directory creation
- Console formatting
  - `greenText()`: Format success messages
  - `redText()`: Format error messages

#### CSS Processing (`workers/basic.js`)

- `removeComments()`: Strip CSS comments
- `myStrip()`: Remove unnecessary whitespace
- Validation and safety checks

### Error Handling

The toolkit implements comprehensive error handling:

- File existence validation
- Directory creation verification
- Read/Write operation protection
- Format-specific validation (e.g., CSS comment structure)
- Colored error messages for visibility

## 🔄 Future Development

The toolkit is designed for expansion. Planned features include:

1. **File Organization**
   - Group files by type
   - Smart file sorting
   - Duplicate detection

2. **Media Processing**
   - Duration analysis
   - Format conversion
   - Metadata extraction

3. **General Utilities**
   - Batch processing capabilities
   - Custom filtering rules
   - Advanced file manipulation

## 🤝 Contributing

Contributions are welcome! The modular architecture makes it easy to add new features:

1. Add new worker modules for specific file types
2. Extend helper utilities for common operations
3. Implement new CLI commands for new features

## ⚠️ Error Codes

Common error messages and their meanings:

- `<Error - [filepath] Doesn't Exist>`: File not found
- `Failed to create directory`: Permission or path issues
- Custom error messages can be specified for writeFile operations

## 📝 Notes

- The toolkit is under active development
- New features will be added progressively
- Maintains backward compatibility with existing functionality
- Focuses on safe file operations with comprehensive error handling

## 📄 License

MIT © Fabian Joseph
