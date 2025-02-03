import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    
    while True:
        user_guess = int(input("Enter your guess: "))
                
        if user_guess < number_to_guess:
            print("Too Low!")
        elif user_guess > number_to_guess:
            print("Too High!")
        else:
            print(f"Congratulations! You've guessed the number")
            break

number_guessing_game()
