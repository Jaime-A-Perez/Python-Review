import random
options = ("rock", "paper", "scissors")
is_there_a_winer = False
rounds = 0
computter_wins = 0
user_wins = 0
while not is_there_a_winer:
    print()
    print('*' * 30)
    print('         ROUND', rounds)
    print(f"computer = {computter_wins}")
    print(f"user = {user_wins}")
    print('*' * 10)
    user_choice = input("rock paper scissors : ")
    if not user_choice in options:
        print("""
              ** Invalid Option **

              * try again *

              """)
        user_choice = input("rock paper scissors : ")

    computer_choice = random.choice(options)



    if user_choice == computer_choice:
        print(""" 
              Tie!""")
    elif user_choice == "rock":
        if computer_choice == "paper":
            print("""
                  paper beast stone
                  COMPUTER WINS!
                  """)
            computter_wins += 1
        else: 
            print("""
                  stone beast scissors
                  USER WINS!
                  """)
            user_wins += 1
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print("""
                  scissors beast paper
                  COMPUTER WINS!
                  """)
            computter_wins += 1
        else: 
            print("""
                  paper beast rock
                  USER WINS!
                  """)
            user_wins += 1
    else:
        if computer_choice == "rock":
            print("""
                  rock best scissors
                  COMPUTER WINS!
                  """)
            computter_wins += 1
        else: 
            print("""
                  scissors beast paper
                  USER WINS!
                  """)
            user_wins += 1

    if computter_wins == 2:
        print("""
              
              THE FINAL WINNER IS THE COMPUTTER""")
        print()
        print('*' * 30)
        break
    if user_wins == 2:
        print("""
              
              THE FINAL WINNER IS THE USER""")
        print()
        print('*' * 30)
        break


    rounds += 1
    