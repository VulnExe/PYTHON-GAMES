board = ["-" for i in range(9)]
print("""
 ----------------------------
  |      TIC TAC TOE       |
 ----------------------------
""")
# or
# board =["-","-","-","-","-","-","-","-","-"]
def displayboard():
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("|", board[6], "|", board[7], "|", board[8], "|")

player_1 = "X"
player_2 = "O"

def check_conditions(player):
    condition = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [2, 4, 6],[0,4,8]
    ]
    for check in condition:
        if board[check[0]] == player and board[check[1]] == player and board[check[2]] == player:
            return 1
    else:
        return 0

def startgame():
    displayboard()
    ranges = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while True:
        while True:
            player1_option = (input(f"{player_1},Enter your position :"))
            if player1_option not in ranges:
                print("Please Enter (1-9)")
                continue
            if board[int(player1_option) - 1] == "-":
                board[int(player1_option) - 1] = player_1
                displayboard()
                if check_conditions(player_1):
                    return f"Winner :{player_1}"
                break
            else:
                print("This is not  Empty!")
        if len([i for i in board if i == '-']) == 0:
            return ''

        while True:
            player2_option = (input(f"{player_2},Enter your position :"))
            if player2_option not in ranges:
                print("Please Enter (1-9)")
                continue
            if board[int(player2_option) - 1] == "-":
                board[int(player2_option) - 1] = player_2
                displayboard()
                if check_conditions(player_2):
                    return f"Winner :{player_2}"
                break
            else:
                print("This is not  Empty!")

print(startgame())
while True:
    play_again= input("Do you want play again [y/n]?:")
    if play_again in "yY":
        board = ["-" for i in range(9)]
        print(startgame())
    else:
        print("Thank for Playing!!!")
        exit()
 #game ends
