import pickle
import random

class GuessTheWord:

    def __init__(self):
        self.name = "Word Master"

    def _readWordList(self, path: str) -> list:

        words = []
        with open(path, 'rb') as file:
            while True:
                try:
                    word = pickle.load(file)
                    words.append(word)
                except EOFError:
                    break

        return words
    
    def _selectRandomWord(self, path: str) -> tuple:

        words = self._readWordList(path)

        randomChoice = random.choice(words)
        randomWord = randomChoice[0]
        randomWordMeaning = randomChoice[1]

        return randomWord, randomWordMeaning
    
    def _revealCharacters(self, word: str, userInput: str):

        revealed = []
        indices = []

        for i, char in enumerate(word):
            if char in userInput:
                revealed.append(char)
                indices.append(i)
            else:
                revealed.append('_')
                indices.append(i)

        return revealed, indices
    
    def initializeGame(self) -> tuple:

        print("""\n
Welcome to Word Master!
              
The rules are simple: you will be given a hint and the number of letters, and you have to guess the 
word within the given number of tries.
              
So let's start by initializing the game!
              """)
        
        print("\nSelect a difficulty level (enter the difficulty code):\n")
        print("""
Easy (5 tries) --> 1
Medium (4 tries) --> 2
Hard (3 tries) --> 3
Extreme (2 tries) --> 4
              """)
        
        numberOfLevels = 10

        userChoice = int(input("Enter you choice: "))

        if userChoice == 1:
            numberOfTries = 5

        elif userChoice == 2:
            numberOfTries = 4

        elif userChoice == 3:
            numberOfTries = 3

        elif userChoice == 4:
            numberOfTries = 2

        return numberOfLevels, numberOfTries
    
    def main(self, path: str, numberOfTries: int, numberOfLevels: int) -> None:

        print(f"""\n
You have {numberOfTries} tries for each level. There will be {numberOfLevels} levels. Wish you all the best :)
              """)
           
        for level in range(1, numberOfLevels + 1):

            randomWord, randomWordMeaning = self._selectRandomWord(path)
            randomWordLength = len(randomWord)

            for t in range(numberOfTries):

                print("\n")
                print(f"\nLevel number: {level}\n")
                print(f"Number of tries left: {numberOfTries}\n")

                print(f"\nHint: {randomWordMeaning}\n")
                print(("_" * randomWordLength) + f" ({randomWordLength} letters)\n")

                userGuess = input("Enter the word that comes to your mind: ").lower()
                partialWordObj = self._revealCharacters(randomWord, userGuess)
                partialWord = ''.join(partialWordObj[0])

                if userGuess == randomWord:
                    print("Congratulations you guessed the word!")
                    break
                else:
                    print("\nNope! That is incorrect!\n")
                    numberOfTries -= 1

                    print("Revealed characters: ", partialWord)

                    if numberOfTries == 0:
                        print("GAME OVER!\n")
                        print(f"The word was {randomWord.upper()}\n")
                        break

        return None

if __name__ == "__main__":

    guesser = GuessTheWord()
    
    path = r"D:\Programs\PythonPrograms\hacktoberfest_2025\Hacktoberfest-2025-Beginner-Python-Projects\src\Avik43218-word-guessing-game\valid_words.dat"
    numberOfLevels, numberOfTries = guesser.initializeGame()

    guesser.main(path=path, numberOfLevels=numberOfLevels, numberOfTries=numberOfTries)
