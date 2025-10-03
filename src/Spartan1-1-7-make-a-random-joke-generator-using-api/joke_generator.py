#!/usr/bin/env python3
"""
Random Joke Generator using API
A simple Python application that fetches random jokes from various APIs
and displays them to the user with a clean command-line interface.
"""

import requests
import json
import sys
import time
from typing import Dict, Optional, List


class JokeGenerator:
    """
    A class to generate random jokes using various joke APIs.
    """
    
    def __init__(self):
        """Initialize the JokeGenerator with available APIs."""
        self.apis = {
            'jokeapi': {
                'url': 'https://v2.jokeapi.dev/joke/Any',
                'params': {'blacklistFlags': 'nsfw,religious,political,racist,sexist,explicit'},
                'name': 'JokeAPI'
            },
            'official_joke': {
                'url': 'https://official-joke-api.appspot.com/random_joke',
                'params': {},
                'name': 'Official Joke API'
            },
            'icanhazdad': {
                'url': 'https://icanhazdadjoke.com/',
                'params': {},
                'name': 'Dad Jokes API'
            }
        }
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Random Joke Generator 1.0 (https://github.com/Spartan1-1-7)'
        })
    
    def fetch_joke_from_jokeapi(self) -> Optional[Dict]:
        """
        Fetch a joke from JokeAPI.
        
        Returns:
            Dict containing joke data or None if failed
        """
        try:
            api_info = self.apis['jokeapi']
            response = self.session.get(
                api_info['url'], 
                params=api_info['params'], 
                timeout=10
            )
            response.raise_for_status()
            
            data = response.json()
            if data.get('error'):
                return None
            
            if data.get('type') == 'single':
                return {
                    'joke': data.get('joke'),
                    'type': 'single',
                    'source': api_info['name']
                }
            elif data.get('type') == 'twopart':
                return {
                    'setup': data.get('setup'),
                    'delivery': data.get('delivery'),
                    'type': 'twopart',
                    'source': api_info['name']
                }
        except requests.exceptions.RequestException as e:
            print(f"Error fetching from {api_info['name']}: {e}")
            return None
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error parsing response from {api_info['name']}: {e}")
            return None
    
    def fetch_joke_from_official_joke_api(self) -> Optional[Dict]:
        """
        Fetch a joke from Official Joke API.
        
        Returns:
            Dict containing joke data or None if failed
        """
        try:
            api_info = self.apis['official_joke']
            response = self.session.get(api_info['url'], timeout=10)
            response.raise_for_status()
            
            data = response.json()
            return {
                'setup': data.get('setup'),
                'delivery': data.get('punchline'),
                'type': 'twopart',
                'source': api_info['name']
            }
        except requests.exceptions.RequestException as e:
            print(f"Error fetching from {api_info['name']}: {e}")
            return None
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error parsing response from {api_info['name']}: {e}")
            return None
    
    def fetch_joke_from_icanhazdad(self) -> Optional[Dict]:
        """
        Fetch a joke from Dad Jokes API.
        
        Returns:
            Dict containing joke data or None if failed
        """
        try:
            api_info = self.apis['icanhazdad']
            headers = {'Accept': 'application/json'}
            response = self.session.get(
                api_info['url'], 
                headers=headers, 
                timeout=10
            )
            response.raise_for_status()
            
            data = response.json()
            return {
                'joke': data.get('joke'),
                'type': 'single',
                'source': api_info['name']
            }
        except requests.exceptions.RequestException as e:
            print(f"Error fetching from {api_info['name']}: {e}")
            return None
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error parsing response from {api_info['name']}: {e}")
            return None
    
    def get_random_joke(self, api_preference: Optional[str] = None) -> Optional[Dict]:
        """
        Get a random joke from available APIs.
        
        Args:
            api_preference: Specific API to use ('jokeapi', 'official_joke', 'icanhazdad')
        
        Returns:
            Dict containing joke data or None if all APIs fail
        """
        if api_preference and api_preference in self.apis:
            method_name = f"fetch_joke_from_{api_preference}"
            if hasattr(self, method_name):
                return getattr(self, method_name)()
        
        # Try all APIs in order if no preference or preference failed
        methods = [
            self.fetch_joke_from_jokeapi,
            self.fetch_joke_from_official_joke_api,
            self.fetch_joke_from_icanhazdad
        ]
        
        for method in methods:
            joke = method()
            if joke:
                return joke
        
        return None
    
    def display_joke(self, joke_data: Dict) -> None:
        """
        Display a joke in a formatted way.
        
        Args:
            joke_data: Dictionary containing joke information
        """
        print("\n" + "="*60)
        print(f"Source: {joke_data.get('source', 'Unknown')}")
        print("="*60)
        
        if joke_data.get('type') == 'single':
            print(f"\n{joke_data.get('joke')}")
        elif joke_data.get('type') == 'twopart':
            print(f"\nSetup: {joke_data.get('setup')}")
            print("...")
            time.sleep(2)  # Add suspense
            print(f"Punchline: {joke_data.get('delivery')}")
        
        print("\n" + "="*60)
    
    def run_interactive_mode(self) -> None:
        """Run the joke generator in interactive mode."""
        print("Welcome to the Random Joke Generator!")
        print("Press Enter to get a joke, 'q' to quit, or choose an API:")
        print("1 - JokeAPI (general jokes)")
        print("2 - Official Joke API (setup/punchline format)")
        print("3 - Dad Jokes API (dad jokes)")
        print("-" * 50)
        
        api_map = {
            '1': 'jokeapi',
            '2': 'official_joke',
            '3': 'icanhazdad'
        }
        
        while True:
            try:
                user_input = input("\nPress Enter for random joke, 1-3 for specific API, or 'q' to quit: ").strip().lower()
                
                if user_input == 'q':
                    print("Thanks for using the Random Joke Generator! Have a great day!")
                    break
                
                api_preference = api_map.get(user_input)
                
                print("Fetching a joke for you...")
                joke = self.get_random_joke(api_preference)
                
                if joke:
                    self.display_joke(joke)
                else:
                    print("Sorry, couldn't fetch a joke right now. Please check your internet connection and try again.")
                
            except KeyboardInterrupt:
                print("\n\nThanks for using the Random Joke Generator! Have a great day!")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")


def main():
    """Main function to run the joke generator."""
    generator = JokeGenerator()
    
    # Check command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == '--single':
            # Get a single joke and exit
            joke = generator.get_random_joke()
            if joke:
                generator.display_joke(joke)
            else:
                print("Sorry, couldn't fetch a joke right now.")
                sys.exit(1)
        elif sys.argv[1] == '--help':
            print("Random Joke Generator")
            print("Usage:")
            print("  python joke_generator.py           - Interactive mode")
            print("  python joke_generator.py --single  - Get one joke and exit")
            print("  python joke_generator.py --help    - Show this help")
        else:
            print("Invalid argument. Use --help for usage information.")
            sys.exit(1)
    else:
        # Run in interactive mode
        generator.run_interactive_mode()


if __name__ == "__main__":
    main()