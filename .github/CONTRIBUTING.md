# Contributing to TurboTask

👋 First off, thanks for taking the time to contribute! 

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Development Setup](#development-setup)
  - [Python Setup](#python-setup)
  - [Node.js Setup](#nodejs-setup)
- [Development Process](#development-process)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)

## Code of Conduct

This project and everyone participating in it are governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to fector101@yahoo.com.

## Development Setup

### Python Setup
1. Fork and clone the repository
   ```bash
   git clone https://github.com/YOUR_USERNAME/TurboTask.git
   cd TurboTask/python
   ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # Unix/macOS
   # or
   venv\Scripts\activate     # Windows
   ```

3. Install development dependencies
   ```bash
   pip install -e ".[dev]"
   ```

### Node.js Setup
1. Navigate to Node.js directory
   ```bash
   cd nodejs
   ```

2. Install dependencies
   ```bash
   npm install
   ```

3. Link package locally
   ```bash
   npm link
   ```

## Development Process

1. Create a new branch for your feature
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes
   - Write tests for new features
   - Update documentation as needed
   - Follow style guidelines

3. Run tests
   - Python: `pytest`
   - Node.js: `npm test`

4. Commit your changes
   ```bash
   git commit -m "feat: add amazing feature"
   ```
   We follow [Conventional Commits](https://www.conventionalcommits.org/).

## Pull Request Process

1. Update the README.md with details of changes if applicable
2. Update the version numbers following [Semantic Versioning](https://semver.org/)
3. Create a Pull Request with a clear title and description
4. Link any relevant issues
5. Wait for review from maintainers

## Style Guidelines

### Python
- Follow PEP 8
- Use type hints
- Document functions using Google-style docstrings
- Maximum line length: 88 characters (Black formatter)

### Node.js
- Follow ESLint configuration
- Use TypeScript where possible
- Document using JSDoc
- Use Prettier for formatting

## Testing

### Python
```bash
pytest
pytest --cov=turbotask tests/
```

### Node.js
```bash
npm test
npm run test:coverage
```

## Documentation

- Update documentation for any new features
- Include examples in the README
- Add JSDoc/docstring for public APIs

## Questions?

Feel free to open an issue or reach out to fector101@yahoo.com.

---

Thank you for contributing to TurboTask! 🎉