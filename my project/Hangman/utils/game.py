import random

class Hangman:
    def __init__(self):
        self.possible_words=['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find=list(random.choice(self.possible_words))
        self.lives= 5
        self.correctly_guessed_letters= [' _ '] * len(self.word_to_find)
        self.wrongly_guessed_lettters= []
        self.turn_count= 0
        self.error_count= 0

    def play(self):
        #asks the player to enter a letter
        guess_letter = input("Enter a word pls! ")

        #not more than a letter     
        if len(guess_letter) != 1:
            self.lives = 5
            print("Please enter just letter!!!!! ")
            return
        
        #not something else than a letter 
        if not guess_letter.isalpha():
            self.lives = 5
            print("Please just a letter")
            return
        
        #adding it to the correctly_guessed_letters list.
        if guess_letter in list(self.word_to_find):
            self.turn_count += 1
            for letter in range(len(self.word_to_find)):
                if self.word_to_find[letter] == guess_letter:
                    self.correctly_guessed_letters[letter] = guess_letter
            print(self.correctly_guessed_letters)
            
                
        #add it to the wrongly_guessed_letters and add 1 to error_count
        else: 
            self.lives -= 1
            self.turn_count += 1
            self.wrongly_guessed_lettters.append(guess_letter)
            self.error_count += 1
            print('wrong guess try again...')
       
    
    def start_game(self):
        #will call play() until the game is over
        self.play()
        
        while self.lives > 0 and self.correctly_guessed_letters != self.word_to_find:
           self.play()
        else:
            self.game_over()
        if len(self.correctly_guessed_letters) == len(self.word_to_find):
            self.well_played()

    #will call game_over() if lives is equal to 0.
    def game_over(self):
        print('game over... ')
    
    #we call it when the player won
    def well_played(self):        
        print(f'You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!')
        
game= Hangman()
game.start_game()