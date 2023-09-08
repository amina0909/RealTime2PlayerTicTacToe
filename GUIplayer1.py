#player 1 code
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
        self.configure(background = 'Pink')
        self.resizable(width=False, height=False)
        self.frame1 = Frame1(self)

class Frame1(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.heading = tk.Label(self, text="Tic Tac Toe", font=('Helvetica',50,'bold'), background='red')
        self.heading.grid()
        self.grid()
        self.createWidgets()
        self.a = gameboard.BoardClass()
        self.clicked = False

    def createWidgets(self):
        self.host_label = tk.Label(self, text="Enter Host Name", font=font.Font(size=18))
        #self.host_label.pack(expand=True, fill='both')
        self.host_label.grid()
        self.host_entry = tk.Entry(self, bg="lightpink", width=18)
        self.host_entry.grid(padx=5, pady=7)
        self.port_label = tk.Label(self, text="Enter Port Number", font=font.Font(size=18))
        self.port_label.grid(padx=5, pady=7)
        self.port_entry = tk.Entry(self, bg="lightpink", width=18)
        self.port_entry.grid(padx=5, pady=7)
        self.pack(padx=5, pady=7)
        self.connect_button = tk.Button(self, text="Connect", font=font.Font(size=10), command=self.connectToServer)
        self.connect_button.grid()
        

    def connectToServer(self):
        host = self.host_entry.get()
        port = int(self.port_entry.get())
        recv_size = 1024

        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((host, port))
            self.conn_success = tk.Label(self, text="Connected to The Server", font=font.Font(size=18))
            self.conn_success.grid()

            #self.connect_button.config(state='disabled')
            #self.host_entry.config(state='disabled')
            #self.port_entry.config(state='disabled')

            self.begin_button = tk.Button(self, text="Begin", font=font.Font(size=10), command=self.switchUsernameScreen)
            self.begin_button.grid()
            
           
            
                
        except: #Exception as e:
            #conn_error = tk.simpledialog.askstring("",)
            error_message = tk.Label(self, text="Connection Error", font=font.Font(size=18))
            error_message.grid()
            
            
    def switchUsernameScreen(self):
        #begin = self.client_socket.sendall("begin")
        self.heading.grid_forget()
        self.host_label.grid_forget()
        self.host_entry.grid_forget()
        self.port_label.grid_forget()
        self.port_entry.grid_forget()
        self.connect_button.grid_forget()
        self.conn_success.grid_forget()
        self.begin_button.grid_forget()
        
        
        self.player1user_prompt = tk.Label(self, text="Enter Username", font=font.Font(size=18))
        self.player1user_prompt.grid(padx=5, pady=7)
        self.player1user = tk.Entry(self, bg="lightblue", width=18 )
        self.player1user.grid(padx=5, pady=7)
        self.submit_button = tk.Button(self, text="Submit", font=font.Font(size=10), command = self.sendPlayer1Username)
        self.submit_button.grid()

    def sendPlayer1Username(self):
        player1username = self.player1user.get()
        self.client_socket.sendall(player1username.encode())
        self.recvPlayer2Username()

    def recvPlayer2Username(self):
        #self.player1user_prompt.forget()
        #self.player1user.forget()
        #self.submit_button.forget()
        player2username = self.client_socket.recv(1024).decode()
        self.player2Label = tk.Label(self, text="Player 2's Username: {}".format(player2username), font=font.Font(size=18))
        self.player2Label.grid()
        self.game()

    #Function that checks for win and prompts player 1  to play again after a win or tie
    def checkWinOrTie(self, a, s, player):
        '''function checks for a win or a tie. prompts player to start a new game or end
           and send player's response to player 2
        '''
        if a.isWinner(player) or a.boardIsFull():
            choice = messagebox.askyesno("Game Over", "Do you want to Play Again")
            choice.grid()
            if answer:
                s.sendall("Play Again".encode())
                self.resetGameBoard()
                return "restart the game"
            else:
                s.sendall("Fun Times!".encode())
                a.printStats1()
                return False
        return True

    def updateMove(self, step):
        if step == '0,0':
            self.b1["text"] = "O"
            self.b1.config(state='disabled')
        if step == '0,1':
            self.b2["text"] = "O"
            self.b2.config(state='disabled')
        if step == '0,2':
            self.b3["text"] = "O"
            self.b3.config(state='disabled')
        if step == '1,0':
            self.b4["text"] = "O"
            self.b4.config(state='disabled')
        if step == '1,1':
            self.b5["text"] = "O"
            self.b5.config(state='disabled')
        if step == '1,2':
            self.b6["text"] = "O"
            self.b6.config(state='disabled')
        if step == '2,0':
            self.b7["text"] = "O"
            self.b7.config(state='disabled')
        if step == '2,1':
            self.b8["text"] = "O"
            self.b8.config(state='disabled')
        if step == '2,2':
            self.b9["text"] = "O"
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
        self.player1user_prompt.grid_forget()
        self.player1user.grid_forget()
        self.submit_button.grid_forget()
        self.player2Label.grid_forget()

        
        #create buttons
        self.b1 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightpink", command=self.b1Clicked)
        self.b2 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightpink", command=self.b2Clicked)
        self.b3 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightpink", command=self.b3Clicked)
        self.b4 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightpink", command=self.b4Clicked)
        self.b5 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightpink", command=self.b5Clicked)
        self.b6 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightpink", command=self.b6Clicked)
        self.b7 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightpink", command=self.b7Clicked)
        self.b8 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightpink", command=self.b8Clicked)
        self.b9 = tk.Button(self, text=" ", font=font.Font(size=36, weight="bold"), fg="black", width=3, height=2,  highlightbackground="lightpink", command=self.b9Clicked)

        self.b1.grid(row=0, column=0)
        self.b2.grid(row=0, column=1)
        self.b3.grid(row=0, column=2)
        self.b4.grid(row=1, column=0)
        self.b5.grid(row=1, column=1)
        self.b6.grid(row=1, column=2)
        self.b7.grid(row=2, column=0)
        self.b8.grid(row=2, column=1)
        self.b9.grid(row=2, column=2)
    

    def b1Clicked(self):
        if self.b1["text"] == " " and self.clicked == False:
            self.b1["text"] = "X"
            #self.b1.config(state='disabled')
            self.a.updateGameBoard(0, 0, 'player1')
            self.clicked = True
            coord = '0,0'
            self.client_socket.sendall(coord.encode())
            if self.checkWinOrTie(self.a, self.client_socket, 'player1'):
                step = self.client_socket.recv(1024).decode()
                if step:
                    self.a.updateMove(step)
                    if self.a.checkWinOrTie(self.a, self.client_socket, 'player2') is True:
                        self.clicked = False
                        checkWinOrTie(a, self.client_socket, 'player2')


    def b2Clicked(self):
        if self.b2["text"] == " " and self.clicked == False:
            self.b2["text"] = "X"
            self.b2.config(state='disabled')
            self.a.updateGameBoard(0, 1, 'player1')
            self.clicked = True
            coord = '0,1'
            self.client_socket.sendall(coord.encode())
            if self.checkWinOrTie(self.a, self.client_socket, 'player1'):
                step = self.client_socket.recv(1024).decode()
                if step:
                    self.a.updateMove(step)
                    if self.a.checkWinOrTie(self.a, self.client_socket, 'player2') is True:
                        self.clicked = False
                        checkWinOrTie(a, self.client_socket, 'player2')

    def b3Clicked(self):
        if self.b3["text"] == " " and self.clicked == False:
            self.b3["text"] = "X"
            self.b3.config(state='disabled')
            self.a.updateGameBoard(0, 2, 'player1')
            self.clicked = True
            coord = '0,2'
            self.client_socket.sendall(coord.encode())
            if self.checkWinOrTie(self.a, self.client_socket, 'player1'):
                step = self.client_socket.recv(1024).decode()
                if step:
                    self.a.updateMove(step)
                    if self.a.checkWinOrTie(self.a, self.client_socket, 'player2') is True:
                        self.clicked = False
                        checkWinOrTie(a, self.client_socket, 'player2')

    def b4Clicked(self):
        if self.b4["text"] == " " and self.clicked == False:
            self.b4["text"] = "X"
            self.b4.config(state='disabled')
            self.a.updateGameBoard(1, 0, 'player1')
            self.clicked = True
            coord = '1,0'
            self.client_socket.sendall(coord.encode())
            if self.checkWinOrTie(self.a, self.client_socket, 'player1'):
                step = self.client_socket.recv(1024).decode()
                if step:
                    self.a.updateMove(step)
                    if self.a.checkWinOrTie(self.a, self.client_socket, 'player2') is True:
                        self.clicked = False
                        checkWinOrTie(a, self.client_socket, 'player2')

    def b5Clicked(self):
        if self.b5["text"] == " " and self.clicked == False:
            self.b5["text"] = "X"
            self.b5.config(state='disabled')
            self.a.updateGameBoard(1, 1, 'player1')
            self.clicked = True
            coord = '1,1'
            self.client_socket.sendall(coord.encode())
            if self.checkWinOrTie(self.a, self.client_socket, 'player1'):
                step = self.client_socket.recv(1024).decode()
                if step:
                    self.a.updateMove(step)
                    if self.a.checkWinOrTie(self.a, self.client_socket, 'player2') is True:
                        self.clicked = False
                        checkWinOrTie(a, self.client_socket, 'player2')

    def b6Clicked(self):
        if self.b6["text"] == " " and self.clicked == False:
            self.b6["text"] = "X"
            self.b6.config(state='disabled')
            self.a.updateGameBoard(1, 2, 'player1')
            self.clicked = True
            coord = '1,2'
            self.client_socket.sendall(coord.encode())
            if self.checkWinOrTie(self.a, self.client_socket, 'player1'):
                step = self.client_socket.recv(1024).decode()
                if step:
                    self.a.updateMove(step)
                    if self.a.checkWinOrTie(self.a, self.client_socket, 'player2') is True:
                        self.clicked = False
                        checkWinOrTie(a, self.client_socket, 'player2')

    def b7Clicked(self):
        if self.b7["text"] == " " and self.clicked == False:
            self.b7["text"] = "X"
            self.b7.config(state='disabled')
            self.a.updateGameBoard(2, 0, 'player1')
            self.clicked = True
            coord = '2,0'
            self.client_socket.sendall(coord.encode())
            if self.checkWinOrTie(self.a, self.client_socket, 'player1'):
                step = self.client_socket.recv(1024).decode()
                if step:
                    self.a.updateMove(step)
                    if self.a.checkWinOrTie(self.a, self.client_socket, 'player2') is True:
                        self.clicked = False
                        checkWinOrTie(a, self.client_socket, 'player2')

    def b8Clicked(self):
        if self.b8["text"] == " " and self.clicked == False:
            self.b8["text"] = "X"
            self.b8.config(state='disabled')
            self.a.updateGameBoard(2, 1, 'player1')
            self.clicked = True
            coord = '2,1'
            self.client_socket.sendall(coord.encode())
            if self.checkWinOrTie(self.a, self.client_socket, 'player1'):
                step = self.client_socket.recv(1024).decode()
                if step:
                    self.a.updateMove(step)
                    if self.a.checkWinOrTie(self.a, self.client_socket, 'player2') is True:
                        self.clicked = False
                        checkWinOrTie(a, self.client_socket, 'player2')

    def b9Clicked(self):
        if self.b9["text"] == " " and self.clicked == False:
            self.b9["text"] = "X"
            self.b9.config(state='disabled')
            self.a.updateGameBoard(2, 2, 'player1')
            self.clicked = True
            coord = '2,2'
            self.client_socket.sendall(coord.encode())
            if self.checkWinOrTie(self.a, self.client_socket, 'player1'):
                step = self.client_socket.recv(1024).decode()
                if step:
                    self.a.updateMove(step)
                    if self.a.checkWinOrTie(self.a, self.client_socket, 'player2') is True:
                        self.clicked = False
                        checkWinOrTie(a, self.client_socket, 'player2')
    
    
    
            
        
'''class Frame2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid()


    def game(self):
        #self.after(1000, self.player1user_prompt.forget())
        #self.after(1000, self.player1user.forget())
        #self.after(1000, self.self.submit_button.forget())
        #self.after(1000, self.player2Label.forget())
        #create buttons
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
    

    def boxClicked(self, b):
        pass'''

'''class Frame2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.turn = True'''
        
    
        

        
'''window=tk.Tk()
window.title("TiC-Tac-Toe Player1")
window.geometry("930x650+0+0")
window.resizable(width=False, height=False)
window.configure(background = 'Pink')

tops = tk.Frame(window, bg ='Cadet Blue', pady =2, width = 1350, height=100) #relief = RIDGE)
#header = tk.Label(master=tops, text="Tic Tac Toe", font=font.Font(size=18))
#header.grid()
tops.grid(row=0, column =0)

lblTitle = tk.Label(master=tops, font=('arial',50,'bold'),text="Tic Tac Toe Game", bd=21, bg='Light Pink',fg='Cornsilk')
lblTitle.configure(anchor="center")
lblTitle.grid(row=0,column = 0)

mainFrame = tk.Frame (window, bg = 'Powder Blue', bd=10,width = 1350, height=600) #relief=RIDGE) 
mainFrame.grid(row=1,column=0)

leftFrame = tk.Frame (mainFrame ,bd=10, width =750, height=500, pady=2, padx=10, bg="VioletRed1") #relief=RIDGE)
leftFrame.pack(side=tk.LEFT)

rightFrame = tk.Frame (mainFrame,bd=10, width =560, height=500, padx=10, pady=2, bg="HotPink1") #relief=RIDGE)
rightFrame.pack(side=tk.RIGHT)

rightFrame1 = tk.Frame(rightFrame ,bd=10, width=560, height=200, padx=10, pady=2, bg="Cadet Blue") #relief=RIDGE) 
rightFrame1.grid(row=0, column=0)

rightFrame2 = tk.Frame(rightFrame,bd=10, width =560, height=250, padx=10, pady=2, bg="Cadet Blue") #relief=RIDGE)
rightFrame2.grid(row=1,column=0)

rightFrame3 = tk.Frame(rightFrame ,bd=10, width=560, height=150, padx=10, pady=2, bg="Cadet Blue") #relief=RIDGE) 
rightFrame3.grid(row=2, column=0)'''


'''if __name__ == "__main__":
    run_client()'''


def main():
    board = UI()
    board.mainloop()


if __name__ == "__main__":
    main()
