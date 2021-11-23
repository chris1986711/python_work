from random import randint

choice = ["rock","papar","scissors"]

computer = choice[randint(0,2)]

your_chioce= input("your choice:",)

print("your choice",your_chioce)

print("computer choice",computer)

if computer == your_chioce:
    print("even")
elif your_chioce == "rock" and computer == "scissors":
    print("you win")
elif your_chioce == "papar" and computer == "rock":
    print("you win") 
elif your_chioce == "scissors" and computer == "papar":
    print("you win")
elif your_chioce == "rock" and computer == "papar":
    print("you lose")
elif your_chioce == "papar" and computer == "scissors":
    print("you lose")
elif your_chioce == "scissors" and computer == "rock":
    print("you lose")                
