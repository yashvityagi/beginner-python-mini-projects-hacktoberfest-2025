#!/usr/bin/env python3
"""
Simple test script for the Random Joke Generator.
This script tests the basic functionality of the joke generator.
"""

import sys
import os

# Add the current directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from joke_generator import JokeGenerator


def test_joke_generator():
    """Test the basic functionality of the JokeGenerator class."""
    print("Testing Random Joke Generator...")
    print("-" * 40)
    
    # Initialize the generator
    generator = JokeGenerator()
    
    # Test each API individually
    apis_to_test = ['jokeapi', 'official_joke', 'icanhazdad']
    
    for api in apis_to_test:
        print(f"\nTesting {api}...")
        joke = generator.get_random_joke(api_preference=api)
        
        if joke:
            print(f"✓ Successfully fetched joke from {api}")
            print(f"  Type: {joke.get('type')}")
            print(f"  Source: {joke.get('source')}")
            
            # Display a short preview
            if joke.get('type') == 'single':
                preview = joke.get('joke', '')[:50] + "..." if len(joke.get('joke', '')) > 50 else joke.get('joke', '')
                print(f"  Preview: {preview}")
            elif joke.get('type') == 'twopart':
                setup_preview = joke.get('setup', '')[:50] + "..." if len(joke.get('setup', '')) > 50 else joke.get('setup', '')
                print(f"  Setup Preview: {setup_preview}")
        else:
            print(f"✗ Failed to fetch joke from {api}")
    
    # Test random joke (any API)
    print(f"\nTesting random joke (any API)...")
    joke = generator.get_random_joke()
    
    if joke:
        print("✓ Successfully fetched random joke")
        print(f"  Source: {joke.get('source')}")
    else:
        print("✗ Failed to fetch random joke")
    
    print("\n" + "-" * 40)
    print("Test completed!")


if __name__ == "__main__":
    test_joke_generator()