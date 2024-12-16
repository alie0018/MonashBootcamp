from __future__ import annotations
import random

"""
Programming Task #2
Create a game where the user must correctly guess a randomly generated integer between 1 and 100.

The user should be notified whether their guess was “lower” or “higher” than the target number.

Author: Albert Liesman (32436793)
"""

def generate_target_number() -> int:
    """
    Generate a random number between 1 and 100.
    
    :return: A random integer between 1 and 100.
    """
    return random.randint(1, 100) # Return a random number between 1 and 100

def get_valid_guess() -> int:
    """
    Prompt the user for a valid guess and ensure it is an integer between 1 and 100.
    Re-prompt if the input is invalid.
    
    :return: A valid integer guess between 1 and 100.
    """
    while True:  # Keep asking until valid input is entered
        try:
            guess = int(input("Enter your guess (1-100): "))  # Convert input to integer
            if 1 <= guess <= 100:  # Check if guess is in the correct range
                return guess  # Return the valid guess
            else:
                print("Invalid input! Your guess must be between 1 and 100.")
        except ValueError:  # If input is not an integer, show an error
            print("Invalid input! Please enter a whole number.")

def give_feedback(guess: int, target: int) -> None:
    """
    Provide feedback to the user on whether their guess is higher or lower.
    
    :param guess: The user's guess.
    :param target: The target number to guess.
    """
    if guess < target:
        print("Your guess is LOWER than the target. Try again!")
    elif guess > target:
        print("Your guess is HIGHER than the target. Try again!")

def play_game() -> None:
    """
    Main game function that generates a target number and allows the user to guess.
    """
    print("Welcome to the Number Guessing Game!")
    print("A random number between 1 and 100 will be selected as the target. Can you guess it?")
    
    target_number = generate_target_number()  # Generate the random target number
    print(target_number)
    attempts = 0  # Keep track of the number of attempts
    
    while True:  # Game loop until the user guesses the correct number
        user_guess = get_valid_guess()  # Get a valid user guess
        attempts += 1  # Increment attempts
        
        if user_guess == target_number:  # Check if the guess is correct
            print(f"Congratulations! You've guessed the correct number {target_number} in {attempts} attempts!")
            break  # End the game
        else:
            give_feedback(user_guess, target_number)  # Give feedback if the guess is incorrect

# Run the game
if __name__ == "__main__":
    play_game()
