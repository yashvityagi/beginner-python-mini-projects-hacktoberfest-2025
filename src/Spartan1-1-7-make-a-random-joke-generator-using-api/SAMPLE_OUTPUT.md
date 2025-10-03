# Sample Output Examples

## Interactive Mode Welcome Screen
```
Welcome to the Random Joke Generator!
Press Enter to get a joke, 'q' to quit, or choose an API:
1 - JokeAPI (general jokes)
2 - Official Joke API (setup/punchline format)
3 - Dad Jokes API (dad jokes)
--------------------------------------------------

Press Enter for random joke, 1-3 for specific API, or 'q' to quit: 
```

## Sample Two-Part Joke Output
```
Fetching a joke for you...

============================================================
Source: JokeAPI
============================================================

Setup: Why don't scientists trust atoms?
...
Punchline: Because they make up everything!

============================================================
```

## Sample Single-Line Joke Output
```
Fetching a joke for you...

============================================================
Source: Dad Jokes API
============================================================

What does a female snake use for support? A co-Bra.

============================================================
```

## Single Joke Mode Output
```bash
$ python joke_generator.py --single

============================================================
Source: Official Joke API
============================================================

Setup: Why did the math book look so sad?
...
Punchline: Because it was full of problems!

============================================================
```

## Help Command Output
```bash
$ python joke_generator.py --help
Random Joke Generator
Usage:
  python joke_generator.py           - Interactive mode
  python joke_generator.py --single  - Get one joke and exit
  python joke_generator.py --help    - Show this help
```