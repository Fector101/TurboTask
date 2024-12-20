# TurboTask File Processing Toolkit

[![PyPI version](https://badge.fury.io/py/TurboTask.svg)](https://badge.fury.io/py/TurboTask)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Support-orange.svg)](https://buymeacoffee.com/fector101)

> A versatile Node.js toolkit designed to simplify file processing tasks, with a focus on efficiency and ease of use. 
Currently supports File Grouping and CSS minification with plans for expanded functionality including media analysis, and more.

## 🚀 Features

### Current Capabilities

- **File Grouping**
  - Automatically organize files by file type
  - Handle nested directory processing

- **CSS Processing**
  - Minification by removing comments and whitespace
  - Single file or bulk directory processing
  - Directory structure preservation
  - Built-in validation checks
  - Custom output path configuration

## 📦 Installation

**Prerequisites**: Python 3.6 or higher

### Via pip (Recommended)

```bash
pip install turbotask
```

### From Source

```bash
# Clone the repository
git clone https://github.com/Fector101/TurboTask.git
cd TurboTask

# Optional: Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Unix/macOS
# or
venv\Scripts\activate     # Windows

# Install from source
pip install .
```

## 🔨 Usage Guide

### Note: In terminal use PascalCase it's `TurboTask --help` not `turbotask --help`

### File Grouping

```bash
TurboTask group [optional_main_path]
```

The argument:

1. [optional_main_path] The main Folder the code will start the scan from (default is './' the folder the code is being ran from).

**Examples:**

```bash
# Group files in current directory
TurboTask group

# Group files in specific directory
TurboTask group "C:/Users/Bob/Downloads"
```

### CSS Processing Commands

#### Remove Whitespace and Comments

```bash
TurboTask noWhiteSpace <input-css-file> [output-file]
```

**Arguments:**

- `input-css-file`: Path to source CSS file
- `output-file`: (Optional) Destination path for processed file
- Defaults to `./TurboTask-output/[original-filename]`

**Examples:**

```bash
# Basic usage
TurboTask noWhiteSpace styles.css

# Custom output path
TurboTask noWhiteSpace styles.css dist/minified.css
```

## 🤝 Contributing

We appreciate contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your PR:

- Includes a clear description of the changes
- Updates relevant documentation
- Adds tests if applicable


## 🐛 Reporting Issues

Found a bug? Please open an issue on our [GitHub Issues](https://github.com/Fector101/TurboTask/issues) page.

## ☕ Support the Project

If you find TurboTask helpful, consider buying me a coffee! Your support helps maintain and improve the project.

<a href="https://www.buymeacoffee.com/fector101" target="_blank">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="60">
</a>

Your support helps me to:
- Maintain and improve TurboTask
- Add new features
- Keep the project active

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Fabian**

- Email: fector101@yahoo.com
- GitHub: [@Fector101](https://github.com/Fector101/TurboTask)

## 🙏 Acknowledgments

- Inspired by the open-source CLI tool community
- Thanks to all contributors who help improve TurboTask

## 📚 Documentation

For detailed documentation and advanced usage examples, visit our [GitHub](https://github.com/Fector101/TurboTask/).

---

Found this project helpful? Give it a ⭐️ on GitHub!