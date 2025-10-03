**Text Analyzer CLI**

A beginner-friendly Python CLI tool that analyzes text from a file or standard input. It reports counts for lines, words, characters, unique words, and shows the most frequent words.

Features
- Reads from a file or stdin
- Counts lines, words, characters, unique words
- Shows top N most common words
- Optional case-insensitive analysis
- Pure Python, no external dependencies

How to Run
1) Using a file
- Put your text in a file, e.g., `samples/sample.txt`.
- Run: `python main.py samples/sample.txt --top 5 --ignore-case`

2) Using stdin
- Run: `echo "Hello hello world" | python main.py --top 3 --ignore-case`

Examples
Command
`python main.py samples/sample.txt --top 5 --ignore-case`

Sample Output
```
Summary:
- Lines        : 3
- Words        : 17
- Characters   : 96
- Unique words : 13

Top words:
word | count
---------------
the  | 3
and  | 2
to   | 2
is   | 2
of   | 1
```

Notes
- Use `--top N` to change how many words to show (default: 10).
- Use `--ignore-case` to combine words like `The` and `the`.
- Omit the file or pass `-` to read from stdin.

Requirements
- Python 3.8+
- No external libraries required

