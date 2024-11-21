# TurboTask

TurboTask is a command-line tool that simplifies file handling tasks, such as removing unnecessary whitespaces and comments from CSS files. It provides efficient ways to format and clean up your code in just a few commands.

## Features

- **Whitespace Removal**: Remove extra whitespace from your CSS files to make them more compact.
- **Comment Stripping**: Remove comments from CSS files, leaving only the actual styles.
- **Directory Processing**: Process entire directories containing CSS files, outputting cleaned-up files in the same folder structure.
- **Command-Line Interface (CLI)**: Easily run tasks via the terminal.

## Installation

To install TurboTask globally via npm:

```bash
npm install -g turbomask
```
Sure, I can help create a curated README.md for your project. Below is a suggested structure for your README.md, based on the context you've shared about the project.

# TurboTask

TurboTask is a command-line tool that simplifies file handling tasks, such as removing unnecessary whitespaces and comments from CSS files. It provides efficient ways to format and clean up your code in just a few commands.

## Features

- **Whitespace Removal**: Remove extra whitespace from your CSS files to make them more compact.
- **Comment Stripping**: Remove comments from CSS files, leaving only the actual styles.
- **Directory Processing**: Process entire directories containing CSS files, outputting cleaned-up files in the same folder structure.
- **Command-Line Interface (CLI)**: Easily run tasks via the terminal.

## Installation

To install TurboTask globally via npm:

```bash
npm install -g turbomask

Usage
Command-Line Commands

TurboTask supports the following command:
noWhiteSpace

Removes all unnecessary whitespace and comments from a CSS file.

Usage:

turbotask noWhiteSpace <input_css_file_path> [output_file_path]

    <input_css_file_path>: The path to the input CSS file to process.
    [output_file_path]: Optional. The path where the cleaned CSS file will be saved. Default is TurboTask/output/no_whitespace.css.

Example:

turbotask noWhiteSpace ./styles.css TurboTask/output/cleaned_styles.css

This will remove whitespace and comments from styles.css and save the cleaned file in TurboTask/output/cleaned_styles.css.
How It Works

    Whitespace Removal: The tool removes all unnecessary whitespace from CSS files, including spaces, tabs, and newlines, while maintaining the structure of the styles.
    Comment Stripping: Any comments (both block comments /* */ and inline comments) are stripped from the CSS content.
    Directory Handling: You can pass entire folders to TurboTask, and it will find all CSS files in the folder and subfolders, cleaning them in the same structure.

Customization
Color Output

The CLI outputs colored messages to indicate success and failure. You can change the colors for messages by modifying the chalk configuration in the main file.
File Paths

The tool assumes that you provide absolute or relative file paths for input and output. It will create any missing directories along the output path.
Example Code

Here's a simple example of using TurboTask programmatically in your Node.js application:

const { removeWhitespace } = require('turbotask');

removeWhitespace('input/styles.css', 'output/cleaned_styles.css');

Development
Prerequisites

    Node.js version 12 or higher
    npm (Node Package Manager)

Running the Project Locally

    Clone the repository:

git clone https://github.com/Fector101/TurboTask.git
cd TurboTask

Install dependencies:

npm install

Run the CLI tool locally:

    node index.js noWhiteSpace ./styles.css

Contributing

    Fork the repository.
    Create a new branch (git checkout -b feature/feature-name).
    Commit your changes (git commit -m 'Add new feature').
    Push to the branch (git push origin feature/feature-name).
    Open a pull request.

License

This project is licensed under the MIT License.


### Notes:
1. **Features Section**: I've listed the features based on the functionality you've described, such as whitespace removal, comment stripping, and directory processing.
2. **Installation and Usage**: Simple instructions to get the tool running and how to use it.
3. **Development Setup**: How to clone the project, install dependencies, and run it locally.
4. **Contributing**: Guidelines for contributing to the project.
