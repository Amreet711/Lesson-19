import random
while True:
    user=input("Please pick your move(rock, paper, scissors):")
    options=["rock", "paper", "scissors"]
    computer=random.choice(options)
    print(f"You chose {user} and the computer chose {computer}")
    if user == computer:
        print(f"Both players chose {user}. It's a tie!")
    elif user == "rock":
        if computer == "paper":
            print("Paper cover rock. You loose!")
        else:
            print("Rock smashes scissors. You win!")
    elif user == "paper":
        if computer == "rock":
            print("Paper covers rock. You win!")
        else:
            print("Scissors cut paper. You loose!")
    elif user == "scissors":
        if computer == "rock":
            print("Rock smashes scissors. You loose!")
        else:
            print("Scissors cut paper. You win!")
    else:
        print("INVALID ENTERY")
    play_again=input("Would you like to play again?(y/n)")
    if play_again == "n":
        break