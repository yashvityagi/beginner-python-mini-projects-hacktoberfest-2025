# Password Generator CLI Tool

A simple command-line tool to generate random passwords.

## Description

This tool generates secure random passwords based on user-specified criteria such as length and character types. It's built with Python's standard library, making it easy to run without external dependencies.

## How to Run

1. Ensure you have Python 3 installed.
2. Navigate to the project directory.
3. Run the tool: `python main.py [options]`

## Options

- `-l, --length`: Length of the password (default: 12)
- `--no-upper`: Exclude uppercase letters
- `--no-lower`: Exclude lowercase letters
- `--no-digits`: Exclude digits
- `--no-symbols`: Exclude symbols

## Sample Output

```bash
$ python main.py
aB3!kL9#mN2p

$ python main.py -l 8 --no-symbols
aB3kL9mN

$ python main.py -l 16
X7@fP2!wQ9#zR4&v
```
