#player 2 code
import tkinter as tk
from tkinter import ttk
from tkinter import font
import socket
import gameboard
import sys
from threading import Thread
from tkinter import messagebox
from tkinter import simpledialog

class UI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe Game")
        self.geometry("500x500")
        self.configure(background = 'lightblue')
        self.resizable(width=True, height=True)
        self.frame1 = Frame1(self)

class Frame1(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.heading = tk.Label(self, text="Tic Tac Toe", font=('Helvetica',50,'bold'), background='yellow')
        self.heading.grid()
        self.grid()
        self.createWidgets()
        self.a = gameboard.BoardClass()
        self.clicked = True

    def createWidgets(self):
        self.hostname = tk.Label(self, text="Enter Host Name", font=font.Font(size=18))
        self.hostname.grid()
        self.hostname_input = tk.Entry(self, bg="lightblue", width=18)
        self.hostname_input.grid(padx=5, pady=7)
        self.port = tk.Label(self, text="Enter Port Number", font=font.Font(size=18))
        self.port.grid(padx=5, pady=7)
        self.port_input = tk.Entry(self, bg="lightblue", width=18)
        self.port_input.grid(padx=5, pady=7)
        self.grid(padx=5, pady=7)
        self.connect_button = tk.Button(self, text="Connect", font=font.Font(size=10), command=self.connectToClient)
        self.connect_button.grid()
        

    def connectToClient(self):

        self.connect_button.config(state='disabled')
        self.hostname_input.config(state='disabled')
        self.port_input.config(state='disabled')
        
        #waiting_msg = tk.Label(self, text="Waiting for another player to connect", font=font.Font(size=13))
        #waiting_msg.pack()
        host = self.hostname_input.get()
        port = int(self.port_input.get())
        #port = self.port_input.get()
        recv_size = 1024

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)
        self.conn, addr = server_socket.accept()

        self.conn_message = tk.Label(self, text="Player 1 connected successfully", font=font.Font(size=14))
        self.conn_message.grid()
        
        

        self.heading.grid_forget()
        self.hostname.grid_forget()
        self.hostname_input.grid_forget()
        self.port.grid_forget()
        self.port_input.grid_forget()
        self.connect_button.grid_forget()
        self.recvPlayer1Username()
        #begin = self.conn.recv(1024).decode
        #recvPlayer1Username
    


    def recvPlayer1Username(self):
        player1username = self.conn.recv(1024).decode()
        self.player1Label = tk.Label(self, text="Player 1's Username: {}".format(player1username), font=font.Font(size=18))
        self.player1Label.grid()

        self.player2user_prompt = tk.Label(self, text="Enter Your Username", font=font.Font(size=18))
        self.player2user_prompt.grid(padx=5, pady=7)
        self.player2user = tk.Entry(self, bg="lightblue", width=18 )
        self.player2user.grid(padx=5, pady=7)
        self.submit_button = tk.Button(self, text="Submit", font=font.Font(size=10), command = self.sendPlayer2Username)
        self.submit_button.grid()

    def sendPlayer2Username(self):
        player2username = self.player2user.get()
        self.conn.sendall(player2username.encode())
        self.game()

    def checkWinOrTie(self, a, s, player):
        '''function checks for a win or a tie. prompts player to start a new game or end
           and send player's response to player 2
        '''
        if a.isWinner(player) or a.boardIsFull():
            #Checking if player 1 wants to play again
            data = s.recv(1024).decode()
            if data == "Fun Times!":
                #print("Goodbye!")
                a.printStats2()
                return False
            else:
                self.resetGameBoard()
                return "continue"
        return True

    def updateMove(self, step):
        if step == '0,0':
            self.b1["text"] = "X"
            self.b1.config(state='disabled')
        if step == '0,1':
            self.b2["text"] = "X"
            self.b2.config(state='disabled')
        if step == '0,2':
            self.b3["text"] = "X"
            self.b3.config(state='disabled')
        if step == '1,0':
            self.b4["text"] = "X"
            self.b4.config(state='disabled')
        if step == '1,1':
            self.b5["text"] = "X"
            self.b5.config(state='disabled')
        if step == '1,2':
            self.b6["text"] = "X"
            self.b6.config(state='disabled')
        if step == '2,0':
            self.b7["text"] = "X"
            self.b7.config(state='disabled')
        if step == '2,1':
            self.b8["text"] = "X"
            self.b8.config(state='disabled')
        if step == '2,2':
            self.b9["text"] = "X"
            self.b9.config(state='disabled')

    def resetGameBoard(self):
        self.b1.destroy()
        self.b2.destroy()
        self.b3.destroy()
        self.b4.destroy()
        self.b5.destroy()
        self.b6.destroy()
        self.b7.destroy()
        self.b8.destroy()
        self.b9.destroy()

        self.b1 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightblue", command=self.b1Clicked)
        self.b2 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightblue", command=self.b2Clicked)
        self.b3 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightblue", command=self.b3Clicked)
        self.b4 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightblue", command=self.b4Clicked)
        self.b5 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightblue", command=self.b5Clicked)
        self.b6 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightblue", command=self.b6Clicked)
        self.b7 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightblue", command=self.b7Clicked)
        self.b8 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightblue", command=self.b8Clicked)
        self.b9 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightblue", command=self.b9Clicked)

        self.b1.grid(row=0, column=0)
        self.b2.grid(row=0, column=1)
        self.b3.grid(row=0, column=2)
        self.b4.grid(row=1, column=0)
        self.b5.grid(row=1, column=1)
        self.b6.grid(row=1, column=2)
        self.b7.grid(row=2, column=0)
        self.b8.grid(row=2, column=1)
        self.b9.grid(row=2, column=2)

        self.clicked = True

        

    def game(self):
        self.conn_message.grid_forget()
        self.player1Label.grid_forget()
        self.player2user_prompt.grid_forget()
        self.player2user.grid_forget()
        self.submit_button.grid_forget()

        #create buttons for gameboard
        self.b1 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightblue", command=self.b1Clicked)
        self.b2 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightblue", command=self.b2Clicked)
        self.b3 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightblue", command=self.b3Clicked)
        self.b4 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightblue", command=self.b4Clicked)
        self.b5 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightblue", command=self.b5Clicked)
        self.b6 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightblue", command=self.b6Clicked)
        self.b7 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightblue", command=self.b7Clicked)
        self.b8 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightblue", command=self.b8Clicked)
        self.b9 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightblue", command=self.b9Clicked)

        self.b1.grid(row=0, column=0)
        self.b2.grid(row=0, column=1)
        self.b3.grid(row=0, column=2)
        self.b4.grid(row=1, column=0)
        self.b5.grid(row=1, column=1)
        self.b6.grid(row=1, column=2)
        self.b7.grid(row=2, column=0)
        self.b8.grid(row=2, column=1)
        self.b9.grid(row=2, column=2)

        step = self.conn.recv(1024).decode()
        if step:
            self.updateMove(step)
            if self.checkWinOrTie(a, self.conn, 'player2') is True:
                self.clicked = False
                checkWinOrTie(a, self.conn, 'player2')

        

    def b1Clicked(self):
        if self.b1["text"] == " " and self.clicked == False:
            self.b1["text"] = "O"
            self.b1.config(state='disabled')
            self.a.updateGameBoard(0, 0, 'player2')
            self.clicked = True
            coord = '0,0'
            self.conn.sendall(coord.encode())
            self.checkWinOrTie(self.a, self.conn, 'player2')
            step = self.conn.recv(1024).decode()
            if step:
                self.updateMove(step)
                if self.checkWinOrTie(self.a, self.conn, 'player1') is True:
                    self.clicked = False
                    

    def b2Clicked(self):
        if self.b2["text"] == " " and self.clicked == False:
            self.b2["text"] = "O"
            self.b2.config(state='disabled')
            self.a.updateGameBoard(0, 1, 'player2')
            self.clicked = True
            coord = '0,0'
            self.conn.sendall(coord.encode())
            checkWinOrTie(a, self.conn, 'player2')
            step = self.conn.recv(1024).decode()
            if step:
                self.updateMove(step)
                if self.checkWinOrTie(self.a, self.conn, 'player1') is True:
                    self.clicked = False

    def b3Clicked(self):
        if self.b3["text"] == " " and self.clicked == False:
            self.b3["text"] = "O"
            self.b3.config(state='disabled')
            self.a.updateGameBoard(0, 2, 'player2')
            self.clicked = True
            coord = '0,0'
            self.conn.sendall(coord.encode())
            checkWinOrTie(a, self.conn, 'player2')
            step = self.conn.recv(1024).decode()
            if step:
                self.updateMove(step)
                if self.checkWinOrTie(self.a, self.conn, 'player1') is True:
                    self.clicked = False

    def b4Clicked(self):
        if self.b4["text"] == " " and self.clicked == False:
            self.b4["text"] = "O"
            self.b4.config(state='disabled')
            self.a.updateGameBoard(1, 0, 'player2')
            self.clicked = True
            coord = '0,0'
            self.conn.sendall(coord.encode())
            checkWinOrTie(a, self.conn, 'player2')
            step = self.conn.recv(1024).decode()
            if step:
                self.updateMove(step)
                if self.checkWinOrTie(self.a, self.conn, 'player1') is True:
                    self.clicked = False

    def b5Clicked(self):
        if self.b5["text"] == " " and self.clicked == False:
            self.b5["text"] = "O"
            self.b5.config(state='disabled')
            self.a.updateGameBoard(1, 1, 'player2')
            self.clicked = True
            coord = '0,0'
            self.conn.sendall(coord.encode())
            checkWinOrTie(a, self.conn, 'player2')
            step = self.conn.recv(1024).decode()
            if step:
                self.updateMove(step)
                if self.checkWinOrTie(self.a, self.conn, 'player1') is True:
                    self.clicked = False

    def b6Clicked(self):
        if self.b6["text"] == " " and self.clicked == False:
            self.b6["text"] = "O"
            self.b6.config(state='disabled')
            self.a.updateGameBoard(1, 2, 'player2')
            self.clicked = True
            coord = '0,0'
            self.conn.sendall(coord.encode())
            checkWinOrTie(a, self.conn, 'player2')
            step = self.conn.recv(1024).decode()
            if step:
                self.updateMove(step)
                if self.checkWinOrTie(self.a, self.conn, 'player1') is True:
                    self.clicked = False

    def b7Clicked(self):
        if self.b7["text"] == " " and self.clicked == False:
            self.b7["text"] = "O"
            self.b7.config(state='disabled')
            self.a.updateGameBoard(2, 0, 'player2')
            self.clicked = True
            coord = '0,0'
            self.conn.sendall(coord.encode())
            checkWinOrTie(a, self.conn, 'player2')
            step = self.conn.recv(1024).decode()
            if step:
                self.updateMove(step)
                if self.checkWinOrTie(self.a, self.conn, 'player1') is True:
                    self.clicked = False

    def b8Clicked(self):
        if self.b8["text"] == " " and self.clicked == False:
            self.b8["text"] = "O"
            self.b8.config(state='disabled')
            self.a.updateGameBoard(2, 1, 'player2')
            self.clicked = True
            coord = '0,0'
            self.conn.sendall(coord.encode())
            checkWinOrTie(a, self.conn, 'player2')
            step = self.conn.recv(1024).decode()
            if step:
                self.updateMove(step)
                if self.checkWinOrTie(self.a, self.conn, 'player1') is True:
                    self.clicked = False

    def b9Clicked(self):
        if self.b9["text"] == " " and self.clicked == False:
            self.b9["text"] = "O"
            self.b9.config(state='disabled')
            self.a.updateGameBoard(2, 2, 'player2')
            self.clicked = True
            coord = '0,0'
            self.conn.sendall(coord.encode())
            checkWinOrTie(a, self.conn, 'player2')
            step = self.conn.recv(1024).decode()
            if step:
                self.updateMove(step)
                if self.checkWinOrTie(self.a, self.conn, 'player1') is True:
                    self.clicked = False

    
        

    '''def game(self):
        b1 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightpink", command=self.boxClicked)
        b2 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightpink", command=self.boxClicked)
        b3 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightpink", command=self.boxClicked)
        b4 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightpink", command=self.boxClicked)
        b5 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightpink", command=self.boxClicked)
        b6 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightpink", command=self.boxClicked)
        b7 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightpink", command=self.boxClicked)
        b8 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightpink", command=self.boxClicked)
        b9 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightpink", command=self.boxClicked)

        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)
        b4.grid(row=1, column=0)
        b5.grid(row=1, column=1)
        b6.grid(row=1, column=2)
        b7.grid(row=2, column=0)
        b8.grid(row=2, column=1)
        b9.grid(row=2, column=2)

    def boxClicked(self):
        pass

class Frame1(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()'''

            
def main():
    board = UI()
    board.mainloop()

if __name__ == "__main__":
    main()

