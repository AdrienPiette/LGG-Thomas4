'''function which prompts the chooser player 
for his word and returns that word'''

def get_word():
    secret_word : str = input("Enter a word here: ").strip().lower()
    return secret_word

'''function which prompts the chooser player for a number of lives 
and returns this number of lives'''

def get_lives():
    while True:
        try:
            number_of_lives : int = int(input("Enter a number of lives: "))
            return number_of_lives
        except ValueError:
            print("Please enter a valid number.")

'''prompts the user for a letter:if user gives more than one letter, 
prompt againif already suggested letter, prompt againreturns the guessed letter'''

def get_guess(guessed_letters : str):
    while True:
        guessed_letter : str = input("Enter a letter here: ").strip().lower()
        if len(guessed_letter) != 1 or not guessed_letter.isalpha():
            print("Enter only one letter.")
        elif guessed_letter in guessed_letters:
            print("You already guessed that letter. Try again.")
        else:
            return guessed_letter

'''does the following:outputs if the guess is correct or not returns the current 
lives of the player depending on the outcome of the guess'''

def assess_guess(secret_word : str,guessed_letter : str,lives_left : int):
    if guessed_letter in secret_word:
        print(f"Good guess! The letter '{guessed_letter}' is in the word.")
    else:
        lives_left -= 1
        print(f"Wrong guess. The letter '{guessed_letter}' is not in the word. You have {lives_left} lives left.")
    return lives_left

'''display_word(...) does the following: displays the secret word with white spaces between the letters,hiding the non-guessed letters by replacing them with '_'
returns True if the correct word has been found, False otherwise'''

def display_word(secret_word : str, suggested_letters : list [str]) -> bool :
    displayed_word = ''.join([letter if letter in suggested_letters else '_' for letter in secret_word])
    print(displayed_word)
    return displayed_word == secret_word


'''function which orchestrates a full game'''

def main():
    secret_word : str = get_word()
    player_lives : int = get_lives()
    guessed_letters : str = []
    
    while player_lives > 0:
        display_word(secret_word, guessed_letters)
        guessed_letter = get_guess(guessed_letters)
        guessed_letters.append(guessed_letter)
        player_lives = assess_guess(secret_word, guessed_letter, player_lives)
        
        if display_word(secret_word, guessed_letters):
            print("Congratulations! You guessed the word correctly.")
            break
    else:
        print(f"Game over! The correct word was '{secret_word}'.")

if __name__ == "__main__":
    main()


        






