import random # This import helps us to select a random word
from colorama import init, deinit, Fore, Style, Cursor #This import helps with color output

init(autoreset=True) # Colorama requires an init call. This is to add color to our output. Autoreset will reset the color of our output after every print
# List of possible secret words
word_list = ["space", "word", "cursor", "mouse", "crown", "logic", "plane", "stool", "tool", "plank", "fuzzy", "pizza", "about", "fizzy", "enter", "house", "speaker", "rocket", "movie", "light", "glass", "plant", "stand", "kitten"]

print(f"Welcome to {Fore.RED}w{Fore.BLUE}o{Fore.GREEN}r{Fore.YELLOW}d{Fore.CYAN}l{Fore.MAGENTA}e") # Welcome message

new_game = True # Set new_game to true so that the loop runs at least once.
while new_game:
    game_word = random.choice(word_list) # Let's choose a random secret word from the list. Here we use the random library we imported earlier
    game_word_l = list(game_word) # Now we break up the word into a list of characters (letters)
    game_word_c = len(game_word) # Number of letters in our secret word
    guess_limit = game_word_c + 1

    print(f"The secret word has {game_word_c} letters. You have {guess_limit} guesses remaning")
    guess_count = 0
    while True: # This will loop the round until we break out of it. (Number of guesses are up, or the player guesses right) 
        valid_guess = False # Default to an invalid guess. 
        while not valid_guess: # Loop until we have a valid guess
            guess = input() # Read user input
            if len(guess) != len(game_word): # Check if the guessed length is the same as the world length 
                print(f"Your guess has {len(guess)} letters, it need to be {len(game_word)}") # Print an error if not
            else:
                guess_count += 1 # Increase the guess count by 1 
                valid_guess = True # Set valid_guess to true if the input is valid
        print(Cursor.UP(), end="") # Move cursor up so we can update the entered word colors.
        if guess == game_word: # If the input matches our word, then output a message and break. No further check needed.
            print(f"{Fore.GREEN}{game_word}") # Print word in green, since everything is right. 
            print(f"{Fore.BLUE}Well done!") # Print a message in blue.
            break # Break out of the infinite loop.
        # If the guess was wrong, then we need to process the guess. 
        guess_l = list(guess) # Break the guess into a list of characters (letters)
        output = "" # This variable can hold our ouput
        
        for x in range(0,len(guess_l)): # Loop through all the letters in the guess. 
            if guess_l[x] == game_word_l[x]: output += Fore.GREEN + guess_l[x] # If the character matches in the right posisiton, add it to our output in green
            elif guess_l[x] in game_word_l: output += Fore.YELLOW + guess_l[x] # If the character is in the secret word but wrong place, add it to our output in yellow
            else: output = output + Fore.RESET + guess_l[x] # If we get here then the character is not part of the secret word

        if guess_count == guess_limit: # Player has run out of guesses.
            print(f"{output}\t {Fore.RED}You have run out of guesses :(")
            print(f"The secret word was {Fore.GREEN}{game_word}") # Print the secret word
            break # End the round

        if (guess_limit - guess_count) == 1: output += f"{Style.RESET_ALL}\t last guess!" # Print a unique message for the last guess
        else: output += f"{Style.RESET_ALL}\t {guess_limit - guess_count} guesses remaining"
        print(output) # Print the result

    # once we get here, we are out of the loop and the round is over
    print(f"{Fore.RED}Game Over{Fore.RESET}")
    ng = ""
    while ng not in ["y","n"]:
        print("Play again (y/n)? ", end = "")
        ng = input().lower()
        if ng == "n": new_game = False # Set new game to false if no and exit the loop. We don't need a check for yes since that is the default. 

deinit() # Colorama requires a deinit call