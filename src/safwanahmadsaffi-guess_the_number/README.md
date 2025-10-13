# guess_the_number — Project helper

This folder contains a tiny helper `todo.py` for the `guess_the_number` project. It's a minimal command-line todo list used by contributors to track small tasks for the project.


Files
- `todo.py` — simple CLI to add/list/complete/clear tasks. Stores tasks in `todo.json` next to the script.
- `requirements.txt` — minimal dependencies (empty or small). See below.

Usage

Run the todo helper with Python 3.7+:

```bash
python todo.py list
python todo.py add "Write tests for game"
python todo.py done 1
python todo.py clear
```

No installation is required — the script only uses the Python standard library.

License

This helper is provided under the same license as the repository.
