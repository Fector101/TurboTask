from setuptools import setup, find_packages

setup(
    name="TurboTask",
    version="0.2",
    packages=find_packages(),
    install_requires=['colorama'],
    author='Fabian',
    url='https://github.com/Fector101/TurboTask/',
    entry_points={
        "console_scripts": [
            "TurboTask=turbotask.main:main",
        ],
    },
    author_email='fabianjoseph063@gmail.com',
    description='A command-line tool that Makes Handling files quick and easy.',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
