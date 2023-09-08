class BoardClass:
    def __init__(self): 
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.player1user = ""
        self.player2user = "Player 2"
        self.lastPlayer = None
        self.winsPlayer1 = 0
        self.winsPlayer2 = 0
        self.lossesPlayer1 = 0
        self.lossesPlayer2 = 0
        self.ties = 0
        self.gamesPlayed = 0
        
    def printBoard(self):
        '''prints the board'''
        for row in range(3):
            print(" | ".join(self.board[row]))
            if row != 2:
                print("----------")
        print(" ")
        print(" ")

    def updateUsernameInput(self, name):
        '''assigns player1user to name (which is inputted in player 1 file from the user) '''
        self.player1user =  name
        print(self.player1user)

    def updateGamesPlayed(self):
        '''increments the number of games played'''
        self.gamesPlayed += 1
        return self.gamesPlayed

    def resetGameBoard(self):
        '''resets the gameboard for a new game'''
        self.lastPlayer = None
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        #return self.board
        for row in range(3):
            print(" | ".join(self.board[row]))
            if row != 2:
                print("----------")
        print(" ")
        print(" ")

    def updateGameBoard(self, row, column, player):
        '''updates a board coordinate with the symbol of the player (X/O) who input the coordinate'''
        if self.board[row][column] == " ":
            if player == self.player2user:
                self.board[row][column] = "O"
                self.lastPlayer = player
                self.printBoard()
                return True
            #if player == self.player1user:
            else:
                self.board[row][column] = "X"
                self.lastPlayer = player
                self.printBoard()
                return True
                
        else:
            print("This spot is already filled.")
            return False

    def isWinner(self, player):
        '''checks all the possible combinations that result in a win
           if there is a tie it displays the "tie" message
           if there is a win it displays "won" or "lost" to the corresponding players'''
        #horizontal wins
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                if self.board[row][0] == "X":
                    if player == self.player1user:
                        print("You win!")
                    else:
                        print("You lose")
                    self.winsPlayer1 += 1
                    self.lossesPlayer2 += 1
                elif self.board[row][0] == "O":
                    if player == self.player2user:
                        print("You win!")
                    else:
                        print("You lose")
                    self.winsPlayer2 += 1
                    self.lossesPlayer1 += 1
                self.updateGamesPlayed()
                return True
        #vertical wins
        for column in range(3):
            if self.board[0][column] == self.board[1][column] == self.board[2][column] != " ":
                if self.board[0][column] == "X":
                    if player == self.player1user:
                        print("You win!")
                    else:
                        print("You lose")
                    self.winsPlayer1 += 1
                    self.lossesPlayer2 += 1
                elif self.board[0][column] == "O":
                    if player == self.player2user:
                        print("You win!")
                    else:
                        print("You lose")
                    self.winsPlayer2 += 1
                    self.lossesPlayer1 += 1
                self.updateGamesPlayed()
                return True

        #diagonal wins
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            if self.board[0][0] == "X":
                if player == self.player1user:
                    print("You win!")
                else:
                    print("You lose")
                self.winsPlayer1 += 1
                self.lossesPlayer2 += 1
            elif self.board[0][0] == "O":
                if player == self.player2user:
                    print("You win!")
                else:
                    print("You lose")
                self.winsPlayer2 += 1
                self.lossesPlayer1 += 1
            self.updateGamesPlayed()
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            if self.board[0][2] == "X":
                if player == self.player1user:
                    print("You win!")
                else:
                    print("You lose")
                self.winsPlayer1 += 1
                self.lossesPlayer2 += 1
            elif self.board[0][2] == "O":
                if player == self.player2user:
                    print("You win!")
                else:
                    print("You lose")
                self.winsPlayer2 += 1
                self.lossesPlayer1 += 1
            self.updateGamesPlayed()
            return True

        return False
            

    def boardIsFull(self):
        '''checks if there are any empty spaces in the board and if not determines a tie'''
        for row in self.board:
            if " " in row:
                return False
        self.ties += 1
        self.updateGamesPlayed()
        print("Tie!")
        return True

    def printStats1(self):
        ''' stats for player 1 to be displayed on player1's terminal (client)'''
        print("Player 1 username : ", self.player1user)
        print("Last player: ", self.lastPlayer)
        print("Games played: ", self.gamesPlayed)
        print("Wins: ", self.winsPlayer1)
        print("Losses: ", self.lossesPlayer1)
        print("Ties: ", self.ties)


    def printStats2(self):
        ''' stats for player 2 to be displayed on player2's terminal (server)'''
        print("Player 2 username : ", self.player2user)
        print("Last player: ", self.lastPlayer)
        print("Games played: ", self.gamesPlayed)
        print("Wins: ", self.winsPlayer2)
        print("Losses: ", self.lossesPlayer2)
        print("Ties: ", self.ties)

        
