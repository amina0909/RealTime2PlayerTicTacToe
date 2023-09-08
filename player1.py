#this is the client
import gameboard
import socket
import sys

def get_move(player, a):
    '''takes row and column coordinates as input and checks if the move is valid'''
    while True:
        step = input("Enter your row and column coordinates separated by a comma. For row coordinate enter a number from 0-2 and for column coordinate enter a number from 0-2: ")
        move = step.split(",")
        listOfInts = ["0","1","2"]
        if (move[0] not in listOfInts or move[1] not in listOfInts):
            print("Invalid move, please try again.")
        elif a.updateGameBoard(int(move[0]), int(move[1]), player):
            return step

def updateMove(step, a, player):
    '''uses updateGameBoard function to apply the move to
       the game board'''
    move = step.split(",")
    updated_board = a.updateGameBoard(int(move[0]), int(move[1]), player)
    return updated_board

#Function that checks for win and prompts player 1  to play again after a win or tie
def checkWinOrTie(a, s, player):
    '''function checks for a win or a tie. prompts player to start a new game or end
       and send player's response to player 2
    '''
    if a.isWinner(player) or a.boardIsFull():
        choice = input("Do you want to play again? Enter 'y' or 'n': ")
        if choice.lower() == 'n':
            #print("Goodbye!")
            s.sendall("Fun Times!".encode())
            a.printStats1()
            return False
        else:
            s.sendall("Play Again".encode())
            a.resetGameBoard()
            return "restart the game"
    return True
    

def main():
    '''main function where host and port info is taken from user.
       socket connection is established and sent to player2 and username
       is also taken from user and send to player 2. receives player2's username.
       This function also includes the game loop which accepts moves from the
       player until player 1 decides to no longer play. the loop is the exited
       and the socket is closed.
    '''
    a = gameboard.BoardClass()
    HOST = input("Enter host name/IP address: ")
    PORT = int(input("Enter port to use: "))
    RECV_SIZE = 1024

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))   
            print("Establishing Connection to Player 2 HOST: {}, PORT: {}".format(HOST,PORT))
            break
        except:
            print("Connection Failed. Do you want to try again?")
            repeatHostInfo = input("Enter 'y' to input host and port information again and 'n' to end the program: ")
            if repeatHostInfo.lower() == 'y':
                HOST = input("Enter host name/IP address of player 2: ")
                PORT = int(input("Enter port to use: "))
            elif repeatHostInfo.lower() == 'n':
                print("Goodbye.")
                sys.exit()
                break
            else:
                print("That was not a valid answer")
                repeatHostInfo = input("Enter 'y' to input host and port information again and 'n' to end the program: ")
    #Send Player 1's username to player 2
    player1user = input("Enter your username: ")
    a.updateUsernameInput(player1user)
    s.sendall(player1user.encode())

    #Receive Player2's username
    player2user = s.recv(1024).decode()
    print("Player 2 username:", player2user)

    a.printBoard()
    #Game loop
    while True:
        step = get_move(player1user, a)
        #sending player 1's move to player 2
        s.sendall(step.encode())
        b = checkWinOrTie(a, s, player1user)
        if b is False:
            break
        elif b is True:
            #receving player 2's move
            move2 = s.recv(1024).decode()
            updateMove(move2, a, player2user)
            if checkWinOrTie(a, s, player1user) is False:
                break
        

    s.close()


if __name__ == "__main__":
    '''testing block
    '''
    main()




