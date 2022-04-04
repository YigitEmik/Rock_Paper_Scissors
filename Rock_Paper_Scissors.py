import random
import time


def loading(string):
    print(string, end="")
    for i in range(0, 3):
        print(".", end="")
        time.sleep(1)
    print("")


def play():
    user_name = input("Enter your name to start: ")
    computer_score = 0
    user_score = 0
    while True:
        moves = ["rock", "paper", "scissors"]
        if computer_score == 3:
            print("Computer WON the match!")
            exit()
        elif user_score == 3:
            print(f"{user_name} WON the match!")
            exit()
        elif user_score or computer_score != 0:
            print(f"Scoreboard (Best OF Three)\nComputer vs {user_name}\n{computer_score}:{user_score}")
            time.sleep(2)
        user_roll = random.randint(1, 6)
        computer_roll = random.randint(1, 6)
        if computer_roll != user_roll:
            input("Please roll a dice to decide who starts first\nPress \"Enter\" to roll ")
            print("Rolling dices...")
            time.sleep(1)
            print(f"{user_name}, you rolled {user_roll} now its computer's turn")
            loading("Loading")
            print(f"Computer rolled {computer_roll}")
            time.sleep(0.50)
            loading("Calculating")
            loading("Comparing")
            if user_roll > computer_roll:
                print(f"{computer_roll} < {user_roll} {user_name} Goes first!")
                time.sleep(0.50)
                user_move = input("Choose One of the below\nrock,paper,scissors\nPlease enter your move: ")
                time.sleep(0.50)
                print("Computer Goes Now!")
            elif computer_roll > user_roll:
                print(f"{user_roll} < {computer_roll} Computer Goes first!")
                time.sleep(1)
                print("Computer made its move.")
                time.sleep(1)
                user_move = input("Choose One of the below\nrock,paper,scissors\nPlease enter your move: ")
            computer_move = random.choice(moves)
            time.sleep(1)
            loading("Please wait")
            # Conditions
            # Computer Loses
            if computer_move == "rock" and user_move == "paper":
                user_score = user_score + 1
                print(f"Computer's move was {computer_move} and your move was {user_move}.\n{user_name} WON!")
            elif computer_move == "scissors" and user_move == "rock":
                user_score = user_score + 1
                print(f"Computer's move was {computer_move} and your move was {user_move}.\n{user_name} WON!")
            elif computer_move == "paper" and user_move == "scissors":
                user_score = user_score + 1
                print(f"Computer's move was {computer_move} and your move was {user_move}.\n{user_name} WON!")
            # User Loses
            elif computer_move == "paper" and user_move == "rock":
                computer_score = computer_score + 1
                print(f"Computer's move was {computer_move} and your move was {user_move}.\nComputer WON!")
            elif computer_move == "scissors" and user_move == "paper":
                computer_score = computer_score + 1
                print(f"Computer's move was {computer_move} and your move was {user_move}.\nComputer WON!")
            elif computer_move == "rock" and user_move == "scissors":
                computer_score = computer_score + 1
                print(f"Computer's move was {computer_move} and your move was {user_move}.\nComputer WON!")

            # Tie situations
            elif computer_move == "scissors" and user_move == "scissors":
                print(f"Computer's move was {computer_move} and your move was {user_move}.\nIts a TIE!!")
            elif computer_move == "rock" and user_move == "rock":
                print(f"Computer's move was {computer_move} and your move was {user_move}.\nIts a TIE!!")
            elif computer_move == "paper" and user_move == "paper":
                print(f"Computer's move was {computer_move} and your move was {user_move}.\nIts a TIE!!")
        elif computer_roll == user_roll:
            input("Please roll a dice to decide who starts first\nPress \"Enter\" to roll ")
            print("Rolling dices...")
            time.sleep(1)
            print(f"{user_name}, you rolled {user_roll} now its computer's turn")
            loading("Loading")
            print(f"Computer rolled {computer_roll}")
            time.sleep(0.50)
            loading("Calculating")
            loading("Comparing")
            print("Rolls were same try again.")
play()
# Need to call the function to work :)