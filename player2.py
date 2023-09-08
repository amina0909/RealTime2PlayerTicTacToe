#this is the server
import gameboard
import socket


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

def checkWinOrTie(a, conn, player):
    '''function checks for a win or a tie. player2 receives player1's response to
       whether or not they want to start a new game or end and responds accordingly
    '''
    if a.isWinner(player) or a.boardIsFull():
        #Checking if player 1 wants to play again
        data = conn.recv(1024).decode()
        if data == "Fun Times!":
            #print("Goodbye!")
            a.printStats2()
            return False
        else:
            a.resetGameBoard()
            return "continue"
    return True

def run_server():
    '''takes player 2's host and port info and receives player 1's host and port info.
       socket is connected and then player1's username is recevived and player2's username
       is sent (not a custom username though). This function includes the game loop
       which receives player1's moves and sends back player2's moves.
       calls the checkWinOrTie after each move to determine if game has resulted in win or tie.
       socket is closed after receiving message from player1 to stop playing game.
     
    '''
    a = gameboard.BoardClass()
    HOST = input("Enter host name/IP address: ")
    PORT = int(input("Enter port: "))

    RECV_SIZE = 1024

    print("Setting up server HOST: {}, PORT: {}".format(HOST,PORT))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print("Player 1 connected from:", addr)

    #Receive player1's username
    player1user = conn.recv(1024).decode()
    print("Player 1 username:", player1user)
    #print(f"Player 1 username: {player1user}")

    #Sending player2's username to player1
    player2user = "Player 2"
    conn.sendall(player2user.encode())

    #Game Loop
    while True:
        #Receive player 1's move
        step = conn.recv(1024).decode()
        if step:
            updateMove(step, a, player1user)
            c = checkWinOrTie(a, conn, player2user)
            if c is False:
                break

            #Player 2's turn
            elif c is True:
                move2 = get_move(player2user, a)
                conn.sendall(move2.encode())
                b = checkWinOrTie(a, conn, player2user)
                if b is False:
                    break

    conn.close()
    s.close()
    

if __name__ == "__main__":
    run_server()
