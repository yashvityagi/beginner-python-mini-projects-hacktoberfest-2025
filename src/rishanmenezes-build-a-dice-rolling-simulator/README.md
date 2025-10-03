# Dice Rolling Simulator

A beginner-friendly Python project that simulates rolling dice. Includes both a simple CLI and importable functions.

## Features
- Roll one or more dice with any number of sides
- See individual roll results and their sum
- Input validation with helpful error messages
- No external dependencies (except pytest for running tests)

## How to Run

1. Change into the project directory:
```powershell
cd src/rishanmenezes-build-a-dice-rolling-simulator
```

2. Run the interactive CLI:
```powershell
python cli.py
```

3. Or use in your own code:
```python
from dice import roll_die, roll_multiple

# Roll one 6-sided die
result = roll_die()  # returns int 1-6

# Roll multiple dice
results = roll_multiple(2, 6)  # returns list like [3, 5]
```

## Example Output
```
Dice Rolling Simulator (type 'exit' to quit)

Enter number of dice and sides (format: dice sides), e.g. '2 6': 3 6

Results: [4, 2, 6]
Sum: 12

Enter number of dice and sides (format: dice sides), e.g. '2 6': exit
Goodbye!
```

## Running Tests
```powershell
# Install pytest (if not already installed)
python -m pip install --user pytest

# Run tests
python -m pytest
```