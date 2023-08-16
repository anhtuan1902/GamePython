import random
from hangman_words import word_list
from hangman_art import stages, logo

class Hangman:
    def __init__(self):
        self.live = 6 # number of live players
        self.word = random.choice(word_list) # choose a random a word
        self.blank_word = ["_" for _ in range(len(self.word))] # list of blank words needed to replace a letter
        
    def print_blank_word(self):
        blank = ''
        for letter in self.blank_word:
            blank += letter + ' '
        return blank
    
    def check_letter(self, letter):
        if letter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.blank_word[i] = letter
            return True
        else:
            self.live -= 1
            return False

    def start_game(self): 
        print("Starting game...")
        print(logo)
        print("\nWelcome to Hangman Game! Here is blank: " + self.print_blank_word())
        
        while self.live > 0:
            guess_letter = input("Guess a letter: ")
            
            if not self.check_letter(letter=guess_letter):
                print(f"You guess {guess_letter}, that's not in the word. You lose a life.")
                
            print(self.print_blank_word())
            print(stages[self.live])
            
            if "_" not in self.blank_word:
                print("Congratulations! You win!")
                break
            
        if self.live == 0:
            print("You lose!")    
        
    

def main():
    hangman = Hangman()
    hangman.start_game()
    
    
    
main()

