import random

computer = random.choice([-1, 0, 1])
user = input("Enter your choice: ")
userDict = {"r": 1, "p": 0, "s":-1}
choiceDict = {-1: "scissor", 0: "paper", 1:"rock"}
user_input = userDict[user]

print(f"you have entered {choiceDict[user_input]} and computer chose {choiceDict[computer]}")

if(computer == user_input):
    print("its a draw")

else:
    if(computer == -1 and user_input == 0):
        print("computer win!")
    elif(computer == -1 and user_input == 1):
        print("you win!")
    elif(computer == 0 and user_input == -1):
        print("you win!")
    elif(computer == 0 and user_input == 1):
        print("computer win!")
    elif(computer == 1 and user_input == -1):
        print("comuter win!")
    elif(computer == 1 and user_input == 0):
        print("you win!")
