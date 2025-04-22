import random

lower_bound = 1
upper_bound = 20
max_attempts = 7

def get_guess():
  while True:
    try:
      guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
      if lower_bound <= guess <= upper_bound:
        return guess
      else:
        print(f"Invalid input. Please enter a number within {lower_bound} and {upper_bound}")
    except ValueError:
      print("Invalid input. Please enter a valid number.")
      
def check_guess(guess, secret_number):
  if guess == secret_number:
    return "Correct"
  elif guess < secret_number:
    return "Too low"
  else:
    return "Too high"
    
def play_game():
  secret_number = random.randint(lower_bound, upper_bound)
  attempts = 0
  won = False
  
  while attempts < max_attempts:
        attempts += 1
        attempts_left = max_attempts - attempts
        guess = get_guess()
        result = check_guess(guess, secret_number)

        if result == "Correct":
            print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
            won = True
            break
        else:
            print(f"{result}. \n{attempts_left} attempts remaining try again!")

  if not won:
        print(f"Sorry, you ran out of attempts! \nThe secret number is {secret_number}.")

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    while True:
        play_game()
        again = input("Would you like to play again? (yes/no): ").strip().lower()
        if again not in ['yes', 'y', 'Yes', 'Y']:
            print("Thanks for playing!")
            break
