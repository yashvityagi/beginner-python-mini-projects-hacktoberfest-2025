# Python Typing Speed Test
A simple, lightweight command-line application to test your typing speed and accuracy. This single-file Python script provides a clean interface to practice typing and get instant feedback on your performance, including Words Per Minute (WPM) and accuracy.

!

# Features
1. Clean Console Interface: A minimalist and distraction-free UI that runs in any terminal.

2. Random Sentences: Pulls from a predefined list of sentences to ensure a different test each time.

3. Instant Feedback: Calculates and displays your WPM and accuracy immediately after you finish.

# Performance Metrics:

WPM: Calculated based on the standard of 5 characters per word.

Accuracy: Compares your input character-by-character against the prompt.

Play Again: Option to retake the test to track your improvement.

No Dependencies: Runs using only Python's standard libraries (time, random, os).

# How to Run
To run this project, you need to have Python installed on your system.

Save the Code:
Save the project code into a file named typing_test.py.

Open Your Terminal:
Open a command prompt (on Windows) or a terminal (on macOS/Linux).

Navigate to the Directory:
Use the cd command to navigate to the folder where you saved typing_test.py.

cd path/to/your/folder

Execute the Script:
Run the program using the following command:

python typing_test.py

The game will start, and you can follow the on-screen instructions.

How It Works
The script operates on a simple game loop controlled by the run_test() function.

Initialization: The program starts, displays a welcome message, and waits for the user to press Enter.

Test Begins: A random sentence is selected and displayed. A timer starts the moment the input prompt appears.

User Input: The script captures all user keystrokes until they press the Enter key, at which point the timer stops.

# Calculation:

The elapsed time is calculated by subtracting the start time from the end time.

Words Per Minute (WPM) is calculated using the formula: (character_count / 5) / time_in_minutes.

Accuracy is determined by comparing the user's input to the original sentence, character by character.

Display Results: The final results are cleared and displayed neatly on the screen. The user is then prompted to play again.