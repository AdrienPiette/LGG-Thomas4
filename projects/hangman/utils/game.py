
import random

class Hangman:

    def __init__(self):
        
        self.possible_words : str = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find : str = random(self.possible_words)
        self.lives : int = 5
        self.correctly_player_letters : str = "_" * len(self.word_to_find)
        self.wrongly_player_letters : str= []
        self.turn_count : int =  self.lives -1
        self.error_count : int  = self.lives


    def play(self):
        
        while True:
            player_letter : str = input("Enter a letter here: ").strip().lower()
            if len(player_letter) != 1 or not player_letter.isalpha():
                print("Enter only one letter.")
            elif player_letter in self.wrongly_player_letters:
                print("You already guessed that letter. Try again.")
            else:
                return player_letter
            
    def start_game(self):

        bad_guessed_letters = self.wrongly_player_letters
        secret_word : str = self.word_to_find
        player_lives : int = self.lives
        guessed_correctly_letters : str = self.correctly_player_letters

        while player_lives > 0:
            self.play()
        if self.lives == 0 :
            self.game_over()
        elif guessed_correctly_letters in self.correctly_player_letters:
            self.well_played()
        else:
            print(f"{guessed_correctly_letters}")
            print(f"{bad_guessed_letters}")
            print(f'{player_lives}')
            '''print(f'{}')'''

    def game_over(self):

        '''if'''



        
            





