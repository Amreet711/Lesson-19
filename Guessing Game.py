import random
number=random.randint(0,9)
print("I have a number between 0and 9. can you guess it?\n")
playing=True
while playing:
    guess=int(input("Give me your best guess:"))
    if guess == number:
        print("Yay! You win.")
        print(f"The secret number was {number}")
        break
    else:
        print("Incorrect. Try again.")