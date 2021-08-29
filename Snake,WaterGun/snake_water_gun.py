import random
#game begins
print("""
           :::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::
           ::                                                       ::
           ::           SNAKE       WATER        GUN                ::
           ::                                                       ::
           :::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::
            """)

print("""
                                  s => Snake
                                  w => Water
                                  g => Gun
""")

turns = 10
no_of_turns = 0
computer_point = 0
player_point = 0

list = ["s", "w", "g"]

while no_of_turns < turns:
    player_input = input("Snake(s), Water(w), Gun(g):")
    computer_input = random.choice(list)

    if player_input == computer_input:
        print("""
                      TIE 
                Both gets 0 points
                """)
    # snake
    elif player_input == "s" and computer_input == "w":
        player_point = player_point + 1
        print(f"You select '{player_input}' and computer select '{computer_input}'")
        print("You win 1 point")
        print(f"your point is:{player_point} and computer point is:{computer_point}")

    elif player_input == "s" and computer_input == "g":
        computer_point = computer_point + 1
        print(f"You select '{player_input}' and computer select '{computer_input}'")
        print("Computer win 1 point")
        print(f"Your point is:{player_point} and computer point is:{computer_point}")

    # water
    elif player_input == "w" and computer_input == "s":
        computer_point = computer_point + 1
        print(f"You select '{player_input}' and computer select '{computer_input}'")
        print("Computer win 1 point")
        print(f"Your point is:{player_point} and computer point is:{computer_point}")

    elif player_input == "w" and computer_input == "g":
        player_point = player_point + 1
        print(f"You select '{player_input}' and computer select '{computer_input}'")
        print("You win 1 point")
        print(f"your point is:{player_point} and computer point is:{computer_point}")

    # gun
    elif player_input == "g" and computer_input == "s":
        player_point = player_point + 1
        print(f"You select '{player_input}' and computer select '{computer_input}'")
        print("You win 1 point")
        print(f"your point is:{player_point} and computer point is:{computer_point}")

    elif player_input == "g" and computer_input == "w":
        computer_point = computer_point + 1
        print(f"You select '{player_input}' and computer select '{computer_input}'")
        print("Computer win 1 point")
        print(f"your point is:{player_point} and computer point is:{computer_point}")

    else:
        print("Enter the correct choice!")

    no_of_turns = no_of_turns + 1
    print(f"You have '{turns - no_of_turns}' turns out of '{turns}' turns")
    print(".......................................")
print("                                       --- GAME  OVER ---  ")
if player_point == computer_point:
    print("""
           :::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*::: 
           ::                                                                       ::                   
           ::                       !!!THE GAME IS TIE!!!                           ::
           ::                                                                       ::
           :::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::
                                   """)
elif player_point < computer_point:
    print(f"""
           :::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::
           ::                                                                       ::
           ::                            !!!YOU LOSE!!!                             ::
           ::               Your point is '{player_point}' and computer_point '{computer_point}'                ::
           ::                                                                       ::
           :::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::
    """)
else:
    print(f"""
           :::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::
           ::                                                                       ::
           ::                          !!!YOU WON!!!                                ::
           ::               Your point is '{player_point}' and computer_point '{computer_point}'                ::
           ::                                                                       ::
           :::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::*:::
    """)
