import random

new_board=[[" 1", " 2", " 3"],
           [" 4"," 5"," 6"],
           [" 7"," 8"," 9"]]
first_ruond=0
board = [i[:] for i in new_board]
available_moves=[1, 2, 3, 4, 5, 6, 7, 8, 9]
player = random.choice(["❌","⚪"])

def new_game():
    global player,rounds,board,available_moves,new_board
    rounds += 1
    board=[[" 1", " 2", " 3"],
           [" 4"," 5"," 6"],
           [" 7"," 8"," 9"]]
    available_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player = random.choice(["❌", "⚪"])

o_win= x_win= 0
rounds=1
choice=None

print(f"\n welcome to x&o game !"
      f"\n the first player is {player}")

def print_bord():
    global first_ruond
    if first_ruond:
        print(f"player {player}, choose a num..\n")
    for i in range(3):
        print("\t", board[i][0], " | ", board[i][1], " | ", board[i][2])
        if i<2:
            print("\t","-"*3,"+","-"*4,"+","-"*3)
    print(f"rownd: {rounds} \t o:{o_win} VS x:{x_win}")
    print("to exit the game press Q")
    first_ruond = 1

def inputt():
    global choice
    choice=input("\n").lower()
    if choice== "q":
        print("thank you for playing x&o !")
        exit()
    elif choice== "" or ord(choice)>57 or ord(choice)<49 :      #not choos.isdigit() or not 1 <= int(choos) <= 9:
        print("enter a num between 1-9")
        inputt()
    elif not (int(choice) in available_moves):
        print("that is already chosen..")
        inputt()
    else:
        available_moves.remove(int(choice))
        board [(int(choice) - 1) // 3] [(int(choice) - 1) % 3]=player

def check_win():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]: # בדיקת שורות
            return 1
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:  # בדיקת עמודות
            return 1
    if board[0][0] == board[1][1] == board[2][2]:  # בדיקת אלכסון
        return 1
    if board[0][2] == board[1][1] == board[2][0]:  # בדיקת אלכסון
        return 1

def print_if_win(flg):
    global player,x_win,o_win,rounds
    if flg:
        print(f"\t! {player} ! won ! {player} !\n")
        if player=="❌":
            x_win+=1
        else:
            o_win+=1
        return 1
    elif len(available_moves)==0:          # בדיקת תיקו
        print("\tno one won...")
        return 1
    player = "❌" if player == "⚪" else "⚪"
    return 0

while choice!= "q":
    print_bord()
    inputt()
    if print_if_win(check_win()):
        first_ruond = 0
        print_bord()
        new_game()
        choice=input("press Y to another round .\n").lower()



