
# Hangman Game

## Overview

This is a simple Hangman game implemented in Python. The game randomly selects a word and the player has to guess the word by suggesting letters within a certain number of guesses.

## Files

- `game.py`: Contains the \`Hangman\` class that handles the game logic.
- `main.py`: The entry point of the program. It imports the \`Hangman\` class from \`game.py\` and starts the game.
    

## Requirements

- Python 3.x

## Usage

1. Clone the repository to your local machine.
   \`\`\`sh
   git clone https://github.com/gkridvan/LGG-Thomas4.git
   cd LGG-Thomas4
   \`\`\`

2. Ensure you have Python 3 installed on your machine. You can check the Python version by running:
   \`\`\`sh
   python --version
   \`\`\`

3. Run the game by executing the \`main.py\` file:
   \`\`\`sh
   python main.py
   \`\`\`

## Gameplay

- The game will display underscores representing the letters of the word to guess.
- Enter one letter at a time to guess the word.
- You have a limited number of lives (guesses). Each incorrect guess reduces your number of lives.
- The game ends when you either guess the word correctly or run out of lives.

## Example

\`\`\`
_ _ _ _ _ _ _
Lives left: 6
Enter a letter: a
_ a _ _ _ a _
Lives left: 6
Enter a letter: b
_ a _ _ _ a _
Lives left: 5
...
Congratulations, you won!
\`\`\`



## Author

- Rıdvan Gök


