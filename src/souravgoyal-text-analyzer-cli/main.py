"""
Text Analyzer CLI
-----------------
Beginner-friendly command-line tool to analyze a text input or file.

Features:
- Counts lines, words, characters
- Shows unique word count and most common words
- Case-insensitive option
- Simple, no external dependencies

Usage:
    python main.py path/to/file.txt --top 10 --ignore-case
    echo "Some text here" | python main.py --top 5

This script uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from typing import Iterable, List, Tuple


WORD_RE = re.compile(r"\b[\w']+\b", re.UNICODE)


@dataclass
class AnalysisResult:
    lines: int
    words: int
    characters: int
    unique_words: int
    top_words: List[Tuple[str, int]]


def read_text_from_stdin_or_file(path: str | None) -> str:
    """Return text from a file path or stdin if no path provided.

    If `path` is None or '-', reads from stdin. Otherwise reads file contents.
    """
    if path in (None, "-"):
        return sys.stdin.read()
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def tokenize(text: str, ignore_case: bool) -> List[str]:
    if ignore_case:
        text = text.lower()
    return WORD_RE.findall(text)


def analyze_text(text: str, top_n: int = 10, ignore_case: bool = True) -> AnalysisResult:
    lines = 0 if not text else text.count("\n") + 1
    characters = len(text)
    tokens = tokenize(text, ignore_case=ignore_case)
    words = len(tokens)
    counter = Counter(tokens)
    unique_words = len(counter)
    top_words = counter.most_common(top_n)
    return AnalysisResult(
        lines=lines,
        words=words,
        characters=characters,
        unique_words=unique_words,
        top_words=top_words,
    )


def format_table(pairs: Iterable[Tuple[str, int]], col1: str, col2: str) -> str:
    pairs_list = list(pairs)
    if not pairs_list:
        return f"{col1:>10} | {col2:>5}\n" + "-" * 19
    max_key = max(len(k) for k, _ in pairs_list + [(col1, 0)])
    max_val = max(len(str(v)) for _, v in pairs_list + [("", col2)])
    header = f"{col1:<{max_key}} | {col2:>{max_val}}"
    sep = "-" * (max_key + 3 + max_val)
    rows = [f"{k:<{max_key}} | {v:>{max_val}}" for k, v in pairs_list]
    return "\n".join([header, sep, *rows])


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyze text: counts and top words. Read from a file or stdin.",
        epilog="Tip: use '-' or omit file to read from stdin.",
    )
    parser.add_argument(
        "file",
        nargs="?",
        default=None,
        help="Path to a text file, or '-' for stdin. Defaults to stdin if omitted.",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=10,
        help="Show top N most common words (default: 10)",
    )
    parser.add_argument(
        "--ignore-case",
        action="store_true",
        help="Count words case-insensitively (default: false)",
    )
    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> int:
    ns = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        text = read_text_from_stdin_or_file(ns.file)
    except FileNotFoundError:
        print(f"Error: file not found: {ns.file}")
        return 1
    except UnicodeDecodeError:
        print("Error: could not decode file as UTF-8")
        return 1

    result = analyze_text(text, top_n=ns.top, ignore_case=ns.ignore_case)

    print("Summary:")
    print(f"- Lines        : {result.lines}")
    print(f"- Words        : {result.words}")
    print(f"- Characters   : {result.characters}")
    print(f"- Unique words : {result.unique_words}")
    print()
    print("Top words:")
    print(format_table(result.top_words, col1="word", col2="count"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

