def main():
    guess_word=get_word()
    lives=get_lives()
    suggested_letters=[]
    while lives > 0:
        display_word(guess_word, suggested_letters)
        guess=get_guess(suggested_letters)
        if guess in suggested_letters:
            print(f"{guess} has already been guessed.")
            continue
        suggested_letters.append(guess)
        lives=assess_guess(guess_word, guess, lives)
        print(f"Lives left: {lives}")
    print("Game over.")


def get_word():
    guess_word=input("Enter a word: ")
    return guess_word

def get_lives():
    lives=int(input("Enter the number of lives: "))
    return lives

def get_guess(suggested_letters):
    guess=input("Enter a letter: ")
    return guess


def assess_guess(secret_word, guessed_letter, lives_left):
    if guessed_letter in secret_word:
        return lives_left
    else:
        print(f"{guessed_letter} is not in the word.")
        return lives_left - 1
    
def display_word(secret_word, suggested_letters):
    for letter in secret_word:
        if letter in suggested_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")

main()