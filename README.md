# TurboTask File Processing Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Package](https://img.shields.io/badge/Python-Package-blue)](./python)
[![Node.js Package](https://img.shields.io/badge/Node.js-Package-green)](./nodejs)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Support-orange.svg)](https://buymeacoffee.com/fector101)

> A powerful file processing toolkit available for both Python and Node.js, specializing in CSS optimization and more.

## 📦 Available Packages

### [Python Implementation](./python)

```bash
pip install TurboTask
```

- Python 3.6+ support
- Available via PyPI
- [View Python Documentation](./python/README.md)

### [Node.js Implementation](./nodejs)

```bash
npm install turbotask
```

- Node.js 14+ support
- Available via npm
- [View Node.js Documentation](./nodejs/README.md)

## 🚀 Key Features

Node.js implementation offers:

- **File Grouping**
  - Automatically organize files by file type
  - Handle nested directory processing

Both implementations offer:

- **CSS Processing**
  - Minification
  - Comment removal
  - Whitespace optimization
  - Directory structure preservation

- **Batch Processing**
  - Multiple file handling
  - Recursive directory processing
  - Custom output paths

## 🔄 Version Compatibility

| Feature                | Python Package | Node.js Package |
|-----------------------|----------------|-----------------|
| File Grouping         | ❌             | ✅              |
| CSS Minification      | ✅             | ✅              |
| Directory Processing  | ✅             | ✅              |
| Custom Output Paths   | ✅             | ✅              |
| File Validation       | ✅             | ✅              |

## 🎯 Quick Start

Choose your preferred implementation:

### Node.js

```bash
# Install
npm install -g turbotask

# Groups are files in current file directory
turbotask group "./"

# Group files in specific directory
turbotask group "C:/Users/jane/Downloads"

# Creates a 'TurboTask-output' Folder with minified CSS files
turbotask noWhiteSpace ./styles
```

### Python

```bash
# Install
pip install TurboTask

# Creates a 'TurboTask-output' Folder with minified CSS files
TurboTask noWhiteSpace style.css

# Creates a 'minified' Folder with minified CSS files
TurboTask noWhiteSpace ./styles ./minified
```

---

📚 For detailed documentation, visit the respective package directories:

- [Python Documentation](./python/README.md)
- [Node.js Documentation](./nodejs/README.md)

## 🐛 Reporting Issues

Found a bug? Please open an issue on our [GitHub Issues](https://github.com/Fector101/TurboTask/issues) page.

## 🛣️ Roadmap

- [ ] Media file analysis
- [ ] Cross-platform GUI
- [ ] Web interface
- [ ] API service

## ☕ Support the Project

If you find TurboTask helpful, consider buying me a coffee!

<a href="https://www.buymeacoffee.com/fector101" target="_blank">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="60">
</a>

## 👤 Author

**Fabian**

- Email: <fector101@yahoo.com>
- GitHub: [@Fector101](https://github.com/Fector101/TurboTask)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Found this project helpful? Give it a ⭐️ on GitHub!
