import random
from words import words
import string

def get_valid_word(words):  #this function is used to get a valid word from the list of words
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman(): #this function is used to play the game
    word = get_valid_word(words)   
    word_letters = set(word) 
    alphabet = set(string.ascii_uppercase)
    used_letters = set() 

    lives = 5 #this is the number of lives the player has
    while len(word_letters) > 0 and lives > 0:
        print("You have used these letters: ", ' '.join(sorted(used_letters))) 
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input("Type a letter: ").upper() #this is the letter given by the user
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                lives +=1 #player gains a life when they guess a correct letter
                print(f"You have gained a life. You now have, {lives} lives left.")
            else:
                lives -= 1 #player loses a life when they guess a wrong letter
                print("Letter is not in word.")
                print(f"You have {lives} lives left.")
        elif user_letter in used_letters:
            print("You have already used that letter. Please try again.")
        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print(f"Sorry, you died. The word was {word}")
    else:
        print(f"Yay! You guessed the word {word} correctly!")

hangman()



        