import random

# Computer chooses between -1 (water), 0 (gun), 1 (snake)
computer = random.choice([-1, 0, 1])

# Dictionary for mapping user input
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

# Take user input
youstr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()

# Validate input
if youstr not in youDict:
    print("Invalid input! Please enter only 's', 'w', or 'g'.")
    exit()

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

'''
-1 = water
 0 = gun
 1 = snake
'''

# Game logic
if computer == you:
    print("It's a draw!")

else:
    if computer == -1 and you == 1:
        print("You win!")
    elif computer == -1 and you == 0:
        print("You lose!")
    elif computer == 1 and you == -1:
        print("You lose!")
    elif computer == 1 and you == 0:
        print("You win!")
    elif computer == 0 and you == -1:
        print("You win!")
    elif computer == 0 and you == 1:
        print("You lose!")
    else:
        print("Something went wrong!")
