# TurboTask

**TurboTask** is a command-line tool that makes handling files quick and easy. It offers various functionalities such as removing whitespace, commenting, and other utilities for efficient file processing.

## Features

- **noWhiteSpace**: Removes all whitespace and comments in CSS files to reduce the file size.
- **myStrip**: Strips unwanted characters or patterns from files.
- **File handling**: Supports handling files directly through the command line.

## Installation

To install **TurboTask**, you need to have Python 3.6+ installed. You can install **TurboTask** via `pip` by following the steps below:

1. Clone the repository:

   ```bash
   git clone https://github.com/Fector101/TurboTask.git
   cd TurboTask
   ```

2. Create a virtual environment (optional, but recommended):

    ```python3 -m venv myenv
    source myenv/bin/activate  # For Linux/macOS
    myenv\Scripts\activate     # For Windows
    ```

3. Install the package:

    ```pip install .```

## Usage

Once installed, you can run TurboTask directly from the command line by using the following syntax:
    ```TurboTask <command> <file-path> [optional-output-path]```

## Available Commands

- **noWhiteSpace**: This command removes all whitespaces and comments in a given CSS file.
    ```TurboTask noWhiteSpace <input-css-file> [optional-output-file]```

- **input-css-file**: The path to the input CSS file.
- **optional-output-file**: The optional path to save the output file. If not provided, the output will be saved as TurboTask/no whitespace.css   by default.

Example:
    `TurboTask noWhiteSpace header.css`
    <!-- myStrip: Strips unwanted characters or patterns from the specified file. This feature will be available in future releases. -->
This will process the header.css file and output the result to TurboTask/no whitespace.css.

To specify a custom output path:
    TurboTask noWhiteSpace header.css output/no_whitespace.css

## 🤝 Contributing

We welcome contributions to TurboTask. If you'd like to contribute, please follow the steps below:

1. Fork the repository.
2. Create a new branch for your changes.
3. Commit your changes.
4. Push your changes to your fork.
5. Open a pull request with a description of your changes.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

- Fabian - <fector101@yahoo.com>
- GitHub: <https://github.com/Fector101/TurboTask>

Acknowledgments
    Inspired by various open-source CLI tools.
