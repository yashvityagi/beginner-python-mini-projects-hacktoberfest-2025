"""Simple todo CLI for the guess_the_number project.

Usage:
  python todo.py list
  python todo.py add "Task description"
  python todo.py done 2   # mark task #2 done
  python todo.py clear    # remove all completed tasks

Stores tasks in a local JSON file `todo.json` next to this script.
"""

from __future__ import annotations
import argparse
import json
import os
import sys
from typing import List, Dict

TASKS_FILE = os.path.join(os.path.dirname(__file__), "todo.json")


def load_tasks() -> List[Dict]:
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Corrupt todo.json — starting fresh.")
        return []


def save_tasks(tasks: List[Dict]) -> None:
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def list_tasks() -> None:
    tasks = load_tasks()
    if not tasks:
        print("No tasks. Use `python todo.py add \"descr\"` to add one.")
        return
    for i, t in enumerate(tasks, start=1):
        status = "✓" if t.get("done") else " "
        print(f"{i}. [{status}] {t.get('text')}")


def add_task(text: str) -> None:
    tasks = load_tasks()
    tasks.append({"text": text, "done": False})
    save_tasks(tasks)
    print("Added task:", text)


def complete_task(index: int) -> None:
    tasks = load_tasks()
    if index < 1 or index > len(tasks):
        print("Invalid task number")
        sys.exit(2)
    tasks[index - 1]["done"] = True
    save_tasks(tasks)
    print(f"Marked task #{index} done")


def clear_completed() -> None:
    tasks = load_tasks()
    remaining = [t for t in tasks if not t.get("done")]
    save_tasks(remaining)
    print(f"Removed {len(tasks)-len(remaining)} completed task(s)")


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="todo.py", description="Simple todo helper for project")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("list", help="List tasks")

    a_add = sub.add_parser("add", help="Add a new task")
    a_add.add_argument("text", nargs="+", help="Task description")

    a_done = sub.add_parser("done", help="Mark task done")
    a_done.add_argument("index", type=int, help="Task number")

    sub.add_parser("clear", help="Remove completed tasks")

    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> None:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.cmd == "list":
        list_tasks()
    elif args.cmd == "add":
        add_task(" ".join(args.text))
    elif args.cmd == "done":
        complete_task(args.index)
    elif args.cmd == "clear":
        clear_completed()
    else:
        # default: show help
        print("Usage: python todo.py (list|add|done|clear)")


if __name__ == "__main__":
    main()
