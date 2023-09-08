'''from tkinter import * 
from tkinter import messagebox

root = Tk()
root.geometry("300x200")

w = Label(root, text ='This is an example text', font = "50")'''

import tkinter as tk

class Frame1(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.display = tk.Label(self, text="Welcome to Tic Tac Toe", font=font.Font(size=28, weight="bold"),)
        self.display.pack()
        begin = tk.Button(self, text="Begin Game", font=font.Font(size=10)) #command=lambda:changeToFrame1)
        begin.pack()
        self.pack()
        

class Frame2(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        hostname = tk.Label(self, text="Enter Host Name", font=font.Font(size=18))
        hostname.pack()
        self.pack()

class CurrentFrame(tk.Frame):
    def __init__(self, master):
        curr_frame = tk.Frame(master)
        curr_frame.pack(fill='both', expand=1)

        self.ListOfFrames = [Frame1(mainframe),Frame2(mainframe)]
        self.ListOfFrames[1].forget

        other_frame = tk.Frame(master)
        other_frame.pack()

        shift_frame = tk.Button(other_frame, text="swap frames")
        

'''def connect_frames():
    frame2.grid(row=0, column=1, padx=10)  # Align frame2 next to frame1

def switch_frames():
    frame2.grid(row=0, column=0)

root = tk.Tk()

# Create frame 1
frame1 = tk.Frame(root, width=200, height=200, bg="red")
frame1.grid(row=0, column=0)

# Create frame 2
frame2 = tk.Frame(root, width=200, height=200, bg="blue")

# Button to connect frames
#connect_button = tk.Button(root, text="Connect Frames", command=connect_frames)
#connect_button.grid(row=1, column=0, pady=10)

switch_button = tk.Button(root, text="Switch Frames", command=switch_frames)
switch_button.grid(row=1, column=0, pady=15)

root.mainloop()
'''
