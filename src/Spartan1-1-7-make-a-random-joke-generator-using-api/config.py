"""
Configuration settings for the Random Joke Generator.
"""

# API Configuration
API_CONFIG = {
    'timeout': 10,  # Request timeout in seconds
    'max_retries': 3,  # Maximum number of retries for failed requests
    'user_agent': 'Random Joke Generator 1.0 (https://github.com/Spartan1-1-7)',
    'default_api_preference': None,  # None for random, or specify 'jokeapi', 'official_joke', 'icanhazdad'
}

# Display Configuration
DISPLAY_CONFIG = {
    'show_source': True,  # Show the API source for each joke
    'punchline_delay': 2,  # Seconds to wait before showing punchline
    'separator_char': '=',  # Character used for separators
    'separator_length': 60,  # Length of separator lines
}

# Content Filtering (for JokeAPI)
CONTENT_FILTER = {
    'blacklist_flags': ['nsfw', 'religious', 'political', 'racist', 'sexist', 'explicit'],
    'safe_mode': True,  # Enable safe mode filtering
}