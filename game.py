# Task 4
# Anuja's Rock-Paper-Scissors Game


import random

def play_game():
    """
    Main function to play the Rock-Paper-Scissors game.
    """
    
    # Define the possible choices
    options = ["rock", "paper", "scissors"]
    
    # Initialize scores
    user_score = 0
    computer_score = 0
    
    print("--- Welcome to Rock-Paper-Scissors! ---")
    
    

    while True:
        print("\n-----------------------------------------")
        
       
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        
        
        if user_choice not in options:
            print(f"Invalid choice '{user_choice}'. Please try again.")
            continue # Skips the rest of the loop and asks again

        

        computer_choice = random.choice(options)
        
        
        print(f"\nYou chose:     {user_choice.title()}")
        print(f"Computer chose: {computer_choice.title()}\n")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            
            print("You win! 🥳")
            user_score += 1
        else:
            print("You lose! 😢")
            computer_score += 1
            
        
        print(f"\n--- Score ---")
        print(f"You: {user_score} | Computer: {computer_score}")
        
        
        print("-----------------------------------------")
        play_again = input("Do you want to play another round? (y/n): ").lower()
        
        if play_again != 'y' and play_again != 'yes':
            break # Exit the while loop

    
    print("\nThanks for playing! Here is the final score:")
    print(f"You: {user_score} | Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations, you won the match!")
    elif computer_score > user_score:
        print("Better luck next time!")
    else:
        print("It's a draw overall!")



if __name__ == "__main__":
    play_game()