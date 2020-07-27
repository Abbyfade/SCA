import random
def RockPaperScissors():
    options = ["rock", "paper", "scissors"]
    ComScore = 0
    UserScore = 0
    print("Welcome to the Rock, Paper, Scissors game!")
    user = input("Enter your name: ")

    check = input("Enter yes to play or quit to end the game: ").lower()

    while check == "yes":
        s = random.randint(0, 2)
        UserSelection = input("Enter Rock, Paper, or Scissors: ").lower()

        if UserSelection not in options:
            print("You didn't enter any of the options given")
            check = input("Enter yes to play or quit to end the game: ").lower()

        else:
            print("computer picks {}".format(options[s].title()))

            if options[s] == UserSelection:
                print("It's a tie")
                print("Computer : {x}       {user}: {y}".format(x=ComScore, user = user, y=UserScore))
                check = input("Enter yes to keep playing or quit to end the game: ").lower()

            elif options[s] == "rock" and UserSelection == "scissors":
                ComScore += 1
                print("Computer wins!")
                print("Rock smashes Scissors")
                print("Computer : {x}       {user}: {y}".format(x=ComScore, user = user, y=UserScore))
                check = input("Enter yes to keep playing or quit to end the game: ").lower()

            elif options[s] == "rock" and UserSelection == "paper":
                UserScore += 1
                print("You win!")
                print("Paper covers Rock")
                print("Computer : {x}       {user}: {y}".format(x=ComScore, user = user, y=UserScore))
                check = input("Enter yes to keep playing or quit to end the game: ").lower()

            elif options[s] == "paper" and UserSelection == "rock":
                ComScore += 1
                print("Computer wins!")
                print("Paper covers Rock")
                print("Computer : {x}       {user}: {y}".format(x=ComScore, user = user, y=UserScore))
                check = input("Enter yes to keep playing or quit to end the game: ").lower()

            elif options[s] == "paper" and UserSelection == "scissors":
                UserScore += 1
                print("You win!")
                print("Scissors cuts Paper")
                print("Computer : {x}       {user}: {y}".format(x=ComScore, user = user, y=UserScore))
                check = input("Enter yes to keep playing or quit to end the game: ").lower()

            elif options[s] == "scissors" and UserSelection == "rock":
                UserScore += 1
                print("You win!")
                print("Rock smashes Scissors")
                print("Computer : {x}       {user}: {y}".format(x=ComScore, user = user, y=UserScore))
                check = input("Enter yes to keep playing or quit to end the game: ").lower()

            elif options[s] == "scissors" and UserSelection == "paper":
                ComScore += 1
                print("Computer wins!")
                print("Scissors cuts Paper")
                print("Computer : {x}       {user}: {y}".format(x=ComScore, user = user, y=UserScore))
                check = input("Enter yes to keep playing or quit to end the game: ").lower()

RockPaperScissors()