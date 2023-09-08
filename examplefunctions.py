
board = [[' ', ' ', ' ',],[' ', ' ', ' ',],[' ', ' ', ' ',]]

'''def printBoard(board):
    print("---------")
    for row in board:
        print("|", end = '')
        for el in row:
            print(f'{el}|')
        print("---------")'''

def printBoard():
    for row in range(3):
        print(" | ".join(board[row]))
        if row != 2:
            print("----------")

if __name__ == "__main__":
    printBoard()
