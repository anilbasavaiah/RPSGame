import random


def gameresult(userInput):
    computer_choice = ["rock", "paper", "scissors"]
    cc = random.choice(computer_choice)
    if userInput == cc:
        print(f"It's a tie, computer says {cc}")
    else:
        if userInput == "rock" and cc == "paper":
            print(f"Computer wins with {cc}")
        elif userInput == "rock" and cc == "scissors":
            print(f"You win, the computer says {cc}")
        elif userInput == "scissors" and cc == "rock":
            print(f"Computer wins with {cc}")
        elif userInput == "scissors" and cc == "paper":
            print(f"You win, the computer says {cc}")
        elif userInput == "paper" and cc == "rock":
            print(f"You win, the computer says {cc}")
        elif userInput == "paper" and cc == "scissors":
            print(f"Computer wins with {cc}")


while True:
    userinput = input("Please select your option 'rock', 'paper', 'scissors': ").lower()
    gameresult(userinput)
