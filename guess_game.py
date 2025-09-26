import random

def play_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < 1 or guess > 10:
                print("Please guess a number between 1 and 10.")
            elif guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    play_game()