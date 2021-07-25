import random


print(""" 
    --------------------------------
    |     Rock   Paper   Scissor   |      
    --------------------------------
    """)
print("""
     r - Rock
     p - paper
     s - scissor
""")
chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

lst = ['r', 'p', 's']

while no_of_chance < chance:
    user_input = input("Rock(r) , Paper(p) , Scissor(s):")
    computer_input = random.choice(lst)

    if user_input == computer_input:
        print("Tie Both get 0 points")

#if user rock -r
    elif user_input == "r" and computer_input == "p":
        computer_point = computer_point + 1
        print(f"you select '{user_input}' and computer select '{computer_input}'")
        print("computer wins 1 point")
        print(f"your point is '{human_point}' and computer point is '{computer_point}'")

    elif user_input == "r" and computer_input == "s":
        human_point = human_point + 1
        print(f"you select '{user_input}' and computer select 's'")
        print("You wins 1 point")
        print(f"your point is '{human_point}' and computer point is '{computer_point}'")

    #if user paper -p

    elif user_input == "p" and computer_input == "s":
        computer_point = computer_point + 1
        print(f"you select '{user_input}' and computer select 's'")
        print("computer wins 1 point")
        print(f"your point is '{human_point}' and computer point is '{computer_point}'")

    elif user_input == "p" and computer_input == "r":
        human_point = human_point + 1
        print(f"you select '{user_input}' and computer select 'r'")
        print("You wins 1 point")
        print(f"your point is '{human_point}' and computer point is '{computer_point}'")

    #if user paper -s

    elif user_input == "s" and computer_input == "r":
        computer_point = computer_point + 1
        print(f"you select '{user_input}' and computer select 'r' ")
        print("computer wins 1 point")
        print(f"your point is '{human_point}' and computer point is '{computer_point}'")

    elif user_input == "s" and computer_input == "p":
        human_point = human_point + 1
        print(f"you select '{user_input}' and computer select 'p'")
        print("You wins 1 point")
        print(f"your point is '{human_point}' and computer point is '{computer_point}'")

    else:
        print("Enter correct options r-Rock,p-paper,s-scissor")

    no_of_chance = no_of_chance+1
    print(f" you have '{chance - no_of_chance}' out of '{chance}' chances ")
    print("--------------------------------------")
print("GAME OVER")
if human_point == computer_point:
    print("TIE")
elif human_point > computer_point:
    print(f"""
    -------------------------------------------------------------------------------
     |                           |  YOU WON !!!  |                               |
     |                                                                           |
     |   Your point is '{human_point}' and computer point is '{computer_point}'                            |
     |                                                                           |
    -------------------------------------------------------------------------------
    """)
else:
    print("You lose")
    print(f"""
    -------------------------------------------------------------------------------
     |                           |  YOU LOSE !!!  |                               |
     |                                                                           |
     |   Your point is '{human_point}' and computer point is '{computer_point}'                            |
     |                                                                           |
    -------------------------------------------------------------------------------
    """)


