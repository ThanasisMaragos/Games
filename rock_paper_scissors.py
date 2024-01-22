import random
while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock, paper or scissors?: ").lower()
    if player == computer:
        print("computer:", computer)
        print("player: ", player)
        print("Tie")
    elif player =="rock":
        if computer == "scissors":
            print("computer:", computer)
            print("player: ", player)
            print("The player won!")
        elif computer =="paper":
            print("computer:", computer)
            print("player: ", player)
            print("The player lost :(")
    elif player == "paper":
        if computer == "scissors":
            print("computer:", computer)
            print("player: ", player)
            print("The player lost :(!")
        elif computer =="rock":
            print("computer:", computer)
            print("player: ", player)
            print("The player won! ")
    elif player == "scissors":
        if computer == "rock":
            print("computer:", computer)
            print("player: ", player)
            print("The player lost :(!")
        elif computer =="paper":
            print("computer:", computer)
            print("player: ", player)
            print("The player won! ")
    play_again = input("Play again?? Yes/No".lower())
    if play_again != "yes":
        break

print("Bye bot ")