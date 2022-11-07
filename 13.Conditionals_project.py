import random
options = ("rock", "paper", "scissors")
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
    else: 
        print("""
              stone beast scissors
              USER WINS!
              """)
elif user_choice == "paper":
    if computer_choice == "scissors":
        print("""
              scissors beast paper
              COMPUTER WINS!
              """)
    else: 
        print("""
              paper beast rock
              USER WINS!
              """)
else:
    if computer_choice == "rock":
        print("""
              rock best scissors
              COMPUTER WINS!
              """)
    else: 
        print("""
              scissors beast paper
              USER WINS!
              """)
                      
