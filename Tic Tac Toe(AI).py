import random

board = ['0', '1', '2',
         '3', '4', '5',
         '6', '7', '8']

def printboard():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

def player_1():
    while True:
        p1 = int(input("P1 Which? "))
        i = int(p1)
        if board[i] == "X" or board[i] == "O":
            print("Already have")
        else:
            del board[p1]
            board.insert(p1, "X")
            printboard()
            return False
        
def player_2():
    while True:
        p2 = random.randint(0,8)
        i = int(p2)
        if board[i] == "O" or board[i] == "X":
            pass
        else:
            del board[p2]
            board.insert(p2, "O")
            printboard()
            return False
def win():
    for i in range(3): # column
        if board[i] == board[i+3] == board[i+6] :
            if board[i] == "X":
                print("Player 1 win")
                return False
            elif board[i] == "O":
                print("PC win")
                return False
            
    for i in range(3): # row
        if board[i*3] == board[i*3+1] == board[i*3+2] :
            if board[i*3] == "X":
                print("Player 1 win")
                return False
            elif board[i*3] == "O":
                print("PC win")
                return False
            
    if (board[0] == board[4] == board[8]) or (board[6] == board[4] == board[2]):
        if board[4] == "X":
            print("Player 1 win")
            return False
        elif board[4] == "O":
            print("PC win")
            return False
        

def game():
    printboard()
    print("Input 0 to 8 ")
    for i in range(9):
        board[i] = " "
    count = 0
    print("")
    while True:
        player_1()        
        count += 1      
        if win() == False:
            break
        elif count == 5:
            print("Draw")
            break
            
        player_2()
        if win() == False:
            break

def restart():
    while True:
        for i in range(9):
            board[i] = f'{i}'
        say = input("Play again? Yes / No ")
        if say.lower() == "yes":
            print("")
            game()
        elif say.lower() == "no":
            print("Thank you for playing")
            break
        else:
            print("Don't understand")
        
if __name__ == "__main__":
    game()
    restart()


