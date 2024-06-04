#Rock-Paper-Scissors Game
import random
print("""Rock-Paper-Scissors Game 
Introduction - Rock beats scissors, scissors beat paper, and paper beats rock""")
your_choices = ("rock", "paper", "scissors")
running = True
while running:
    You = input("Enter Your Choice : ")
    computer = random.choice(your_choices)
    print("You : ", You)
    print("Computer : ", computer)
    if You in your_choices:
        if You==computer:
            print("it's a tie!")
        elif You== "rock" and computer=="scissors":
            print("You Win!")
        elif You== "scissors" and computer=="paper":
            print("You Win!")
        elif You== "paper" and computer=="rock":
            print("You Win!")
        else:
            print("You Lose!")
    else:
        print("Enter correct choice")
    if not input("play again? (yes/no): ").lower()=="yes":
        running=False
print("THANK YOU!")
