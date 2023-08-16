import random


EASY_LEVEL = 8
MEDIUM_LEVEL = 5
HARD_LEVEL = 3

def level_game(num):
    """ Returns the number lives in the game same level user choose.
    """
    if num == 0:
        return EASY_LEVEL
    elif num == 1:
        return MEDIUM_LEVEL
    else:
        return HARD_LEVEL
    

def check_number(num_random, num_guess):
    """Check result of guessed number correctly with random number
    """
    if num_random == num_guess:
        print("Congratulations!! You guessed the number exactly!!!")
        return True
    elif num_random > num_guess:
        print("Sorry, You guessed the number too small!! Please try again!")
        return False
    else:
        print("Sorry, You guessed the number too high!! Please try again!")
        return False
    

def main():
    print("Welcome to the Numer Guessing Game!!")
    num = int(input("Enter level number your want to play (0:'EASY', 1:'MEDIUM', Other:'HARD'): "))
    number_of_live = level_game(num)
    
    lower_bound = int(input("Enter lower bound number you want to play: "))
    upper_bound = int(input("Enter upper bound number you want to play: "))
    
    number_random = random.randint(lower_bound, upper_bound)
    
    start_game = True
    
    while start_game and number_of_live > 0:
        print(f"You have only {number_of_live} attempts remaining to guess the number")
        number_guess = int(input("Enter number you want to guess: "))
        
        if check_number(num_random=number_random, num_guess=number_guess):
            break
        else:
            number_of_live -= 1
            
            if number_of_live == 0:
                print("You loose!!")

main()
    