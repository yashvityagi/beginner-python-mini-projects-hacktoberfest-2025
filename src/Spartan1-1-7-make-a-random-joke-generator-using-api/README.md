# Random Joke Generator using API

A simple yet feature-rich Python application that fetches random jokes from multiple APIs and displays them with a clean command-line interface. This project demonstrates API integration, error handling, and user interaction in Python.

## Features

- **Multiple API Sources**: Integrates with three different joke APIs for variety
  - JokeAPI (general jokes with content filtering)
  - Official Joke API (setup/punchline format)
  - Dad Jokes API (family-friendly dad jokes)

- **Interactive Mode**: User-friendly command-line interface with options to:
  - Get random jokes from any API
  - Choose specific API sources
  - Exit gracefully

- **Single Joke Mode**: Quick command-line option to get one joke and exit

- **Error Handling**: Robust error handling for network issues and API failures

- **Content Filtering**: Automatically filters out inappropriate content

- **Production Ready**: Includes proper logging, timeouts, and session management

## APIs Used

1. **JokeAPI** (https://jokeapi.dev/)
   - Provides both single-line and setup/punchline jokes
   - Includes content filtering for safe usage
   - Supports multiple categories

2. **Official Joke API** (https://github.com/15Dkatz/official_joke_api)
   - Simple setup/punchline format
   - Reliable and fast response times

3. **icanhazdadjoke** (https://icanhazdadjoke.com/api)
   - Curated collection of dad jokes
   - Family-friendly content

## Installation

### Prerequisites
- Python 3.6 or higher
- Internet connection for API access

### Setup

1. Clone or download this project
2. Navigate to the project directory:
   ```bash
   cd src/Spartan1-1-7-make-a-random-joke-generator-using-api
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Interactive Mode (Default)
Run the application without any arguments to enter interactive mode:

```bash
python joke_generator.py
```

In interactive mode, you can:
- Press Enter to get a random joke from any API
- Type `1` to get a joke from JokeAPI
- Type `2` to get a joke from Official Joke API
- Type `3` to get a joke from Dad Jokes API
- Type `q` to quit

### Single Joke Mode
Get one joke and exit:

```bash
python joke_generator.py --single
```

### Help
Display usage information:

```bash
python joke_generator.py --help
```

## Sample Output

```
Welcome to the Random Joke Generator!
Press Enter to get a joke, 'q' to quit, or choose an API:
1 - JokeAPI (general jokes)
2 - Official Joke API (setup/punchline format)
3 - Dad Jokes API (dad jokes)
--------------------------------------------------

Press Enter for random joke, 1-3 for specific API, or 'q' to quit: 

Fetching a joke for you...

============================================================
Source: JokeAPI
============================================================

Setup: Why don't scientists trust atoms?
...
Punchline: Because they make up everything!

============================================================
```

## Project Structure

```
Spartan1-1-7-make-a-random-joke-generator-using-api/
├── joke_generator.py    # Main application file
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## Code Features

### Object-Oriented Design
- Clean class structure with `JokeGenerator` class
- Modular methods for different API sources
- Proper encapsulation and separation of concerns

### Error Handling
- Network timeout handling
- JSON parsing error handling
- Graceful degradation when APIs are unavailable
- User-friendly error messages

### Session Management
- Persistent HTTP session for better performance
- Proper User-Agent headers for API compliance
- Connection reuse for efficiency

### User Experience
- Clear command-line interface
- Suspenseful delivery for setup/punchline jokes
- Multiple input options and help system
- Graceful exit handling

## Contributing

This project is part of Hacktoberfest 2025. Contributions are welcome! Please ensure:

1. Code follows Python best practices
2. New features include appropriate error handling
3. Documentation is updated for any changes
4. No inappropriate content or APIs are added

## Dependencies

- **requests**: HTTP library for API calls
  - Used for making HTTP requests to joke APIs
  - Handles timeouts, sessions, and error responses

## License

This project is open source and available under the MIT License.

## Author

Created by Spartan1-1-7 for Hacktoberfest 2025.

## Future Enhancements

Potential improvements for this project:
- Add more joke APIs for greater variety
- Implement local caching for offline mode
- Add joke rating and favorites system
- Create a web interface using Flask
- Add joke categories and filtering options
- Implement configuration file for API preferences