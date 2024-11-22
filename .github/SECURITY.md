# Security Policy

## Supported Versions

| Version | Python Support | Node.js Support |
| ------- | ------------- | --------------- |
| 2.x.x   | ✅            | ✅              |
| 1.x.x   | ✅            | ✅              |
| < 1.0   | ❌            | ❌              |

## Reporting a Vulnerability

We take the security of TurboTask seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### Reporting Process

1. **DO NOT** create a public GitHub issue for the vulnerability.
2. Email your findings to fector101@yahoo.com
3. Include the following information:
   - Description of the vulnerability
   - Steps to reproduce
   - Possible impact
   - Suggested fix (if any)
   - Your contact information for follow-up

### What to Expect

1. **Response Time**: We aim to respond within 48 hours with confirmation of receipt.
2. **Updates**: We will keep you informed about the progress of fixing the vulnerability.
3. **Disclosure**: Once fixed, we will coordinate with you on the disclosure timeline.

## Security Best Practices

When using TurboTask:

1. Always verify file permissions before processing
2. Use the latest stable version
3. Run with appropriate user permissions
4. Validate input files before processing
5. Monitor output directories for unexpected changes

## Implementation Security

### Python Package
- Input validation on all file operations
- Safe path handling
- No arbitrary code execution
- Controlled file system access

### Node.js Package
- Strict input validation
- Sanitized file paths
- Limited scope of operations
- Controlled dependencies

## Secure Installation

### Python
```bash
pip install TurboTask --user
```

### Node.js
```bash
npm install turbotask --production
```

## Security Updates

- Security updates are released as soon as possible
- Critical vulnerabilities trigger immediate patch releases
- Updates are announced via GitHub releases
- Subscribe to GitHub releases for notifications

## Bug Bounty Program

Currently, we do not have a bug bounty program, but we deeply appreciate security researchers who take the time to report vulnerabilities.

## Recognition

We maintain a list of security researchers who have helped improve TurboTask's security. Contributors will be acknowledged (with permission) in our releases.

---

Last updated: November 2024