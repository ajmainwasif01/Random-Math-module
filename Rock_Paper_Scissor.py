import random

def rock_paper_scissor():
    choices = ["Rock" , "Paper" , "Scissor"]
    user_score = 0
    computer_score = 0

    print("Welcome to the Rock-Paper-Scissors Game!")

    while True:
        print("\nYour choices: rock, paper, scissors")
        user_choice = input("Enter your choice (or 'quit' to exit): ").lower()
                
        if user_choice == "quit":
          print("Thanks for playing!")
          print(f"Final Scores: You: {user_score}, Computer: {computer_score}")
          break

        if user_choice not in choices:
           print("Invalid choice. Please choose 'rock' ,'paper' or 'scissor'.")
           continue
        computer_choice = random.choice(choices)
        print(f"Computer chose :{computer_choice}")           

        if user_choice == computer_choice:
           print("It's a tie!")
        
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
           print("You win this round!")
           user_score += 1

        else:
           print("Computer won this round!")
           computer_score += 1

        print(f"Current Scores: You: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    rock_paper_scissor()
