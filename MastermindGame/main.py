import random


class MastermindGame:
    def __init__(self):
        self.player_1 = str(random.randint(1000, 10000))
        self.blank_number = ["_" for _ in range(len(str(self.player_1)))]
    
    def print_blank_number(self):
        blank = ''
        for num in self.blank_number:
            blank += num + ' '
        return blank
    
    def check_blank_number(self, num_guess):
        count = 0
        
        for num in num_guess:
            for i in range(len(str(self.player_1))):
                if str(self.player_1)[i] == num:
                    self.blank_number[i] = num
                    count += 1
                    
        if "_" not in self.blank_number:
            print("You've become a Mastermind!")
        elif count > 0:
            print(f'Not quite the number. You did get {count} digits correct.')
        else:
            print("None of the numbers in your input match.")
    

def main():
    mastermind_game = MastermindGame()
    count = 0
    while "_" in mastermind_game.blank_number:
        print(mastermind_game.print_blank_number())
        num_guess = input("Guess number has 4 digits: ")
        mastermind_game.check_blank_number(num_guess=num_guess)
        count += 1
    
    
    print(f"It took you only {count} tries.")


main()
    
    
        

    