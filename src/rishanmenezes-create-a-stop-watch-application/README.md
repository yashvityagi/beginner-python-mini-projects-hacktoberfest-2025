# Stop Watch Application

A simple stopwatch application with lap timing functionality, implemented in Python.

## Features

- Start/stop timing
- Lap time recording
- Time display in HH:MM:SS.ss format
- Command-line interface
- Reset functionality

## Requirements

- Python 3.7+
- pytest (for running tests)

## Installation

No special installation required beyond Python. To install test dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the stopwatch from the command line:

```bash
python cli.py
```

### Controls

- SPACE - Start/Stop the stopwatch
- L - Record a lap time
- R - Reset the stopwatch
- Q - Quit the application

## Testing

Run the tests using pytest:

```bash
pytest test_stopwatch.py
```

## Implementation Details

The stopwatch implementation uses:

- `time.time()` for high-precision timing
- Dataclasses for lap time tracking
- Type hints for better code readability and IDE support
- Unit tests to verify functionality

## Contributing

Contributions are welcome! Please read the [Contributing Guide](../../CONTRIBUTING.md) first.

## License

This project is licensed under the terms of the [MIT License](../../LICENSE).