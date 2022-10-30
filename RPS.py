import random

user = input("Enter the choice(Rock/Paper/Scissors): ")

actions = ["Paper", "Scissors", "Rock"]
computer = random.choice(actions)

print(f"You chose {user} and Computer chose {computer}")
if computer == user:
    print("Its A Tie")
elif user == "Rock":
    if computer == "Scissors":
        print("You Won")
    else:
        print("You Lost")
elif user == "Paper":
    if computer == "Rock":
        print("You Won")
    else:
        print("You Lost")
elif user == "Scissors":
    if computer == "Paper":
        print("You Won")
    else:
        print("You Lost")
