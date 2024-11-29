import random

correct_number = random.randint(1,10)

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 to 10")

while True:
    try:
        guess = int(input("Enter your guess:"))

        if guess < 1 or guess > 10:
            print("Please enter a number between 1 to 10!")
            continue
        if guess == correct_number:
            print(f"Congratulations! You have guessed the Correct Number:{correct_number}")
            break

        elif guess < correct_number:
            print("Too low!Try Again.")
        else:
            print("Too High! Try Again.")
        
    except ValueError:
        print("Invalid input.Please enter a number between 1 to 10")

        
