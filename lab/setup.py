# setup.py
from setuptools import setup, find_packages

setup(
    name="TurboTask",
    version="0.1",
    packages=find_packages(),
    install_requires=[],  # Any dependencies your tool needs
    entry_points={
        "console_scripts": [
            "TurboTask=turbotask.main:main",
        ],
    },
    author="Your Name",
    description="A command-line tool for executing tasks quickly.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/turbotask",  # Replace with your repo URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
