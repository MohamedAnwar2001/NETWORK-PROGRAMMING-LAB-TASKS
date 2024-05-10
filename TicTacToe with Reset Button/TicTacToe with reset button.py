from tkinter import *
from tkinter import messagebox

# Create the main window
window = Tk()

# Set window title and geometry
window.title("Welcome to The Gaming world TIC-Tac-Toe ")
window.geometry("400x400")
window.configure(bg='lightblue')  # Set background color

# Label for the game
lbl = Label(window, text="Tic-tac-toe Game", font=('Helvetica', '15'), fg='#FFD700', bg='#212121')
lbl.grid(row=0, column=0, columnspan=3, pady=10)

# Labels for players
lbl = Label(window, text="Player 1: X", font=('Helvetica', '10'), fg='#FFD700', bg='#212121')
lbl.grid(row=1, column=0)
lbl = Label(window, text="Player 2: O", font=('Helvetica', '10'), fg='#FFD700', bg='#212121')
lbl.grid(row=2, column=0)

# Initialize player's turn
turn = 1

# Function to reset the game
def reset():
    global flag, turn
    flag = 1
    turn = 1
    # Reset button texts to empty
    btn1["text"] = " "
    btn2["text"] = " "
    btn3["text"] = " "
    btn4["text"] = " "
    btn5["text"] = " "
    btn6["text"] = " "
    btn7["text"] = " "
    btn8["text"] = " "
    btn9["text"] = " "
    # Reset button colors to black
    btn1.config(bg='#212121')
    btn2.config(bg='#212121')
    btn3.config(bg='#212121')
    btn4.config(bg='#212121')
    btn5.config(bg='#212121')
    btn6.config(bg='#212121')
    btn7.config(bg='#212121')
    btn8.config(bg='#212121')
    btn9.config(bg='#212121')
# Functions to handle button clicks for each grid cell
def clicked1():
    global turn
    if btn1["text"] == " ":
        if turn == 1:
            turn = 2;
            btn1["text"] = "X"
            btn1.config(fg='#FFD700', bg='#311B92')  # Change button colors
        elif turn == 2:
            turn = 1;
            btn1["text"] = "O"
            btn1.config(fg='#FFD700', bg='#FF6F00')
        check()

def clicked2():
    global turn
    if btn2["text"] == " ":
        if turn == 1:
            turn = 2;
            btn2["text"] = "X"
            btn2.config(fg='#FFD700', bg='#311B92')
        elif turn == 2:
            turn = 1;
            btn2["text"] = "O"
            btn2.config(fg='#FFD700', bg='#FF6F00')
        check()

def clicked3():
    global turn
    if btn3["text"] == " ":
        if turn == 1:
            turn = 2;
            btn3["text"] = "X"
            btn3.config(fg='#FFD700', bg='#311B92')
        elif turn == 2:
            turn = 1;
            btn3["text"] = "O"
            btn3.config(fg='#FFD700', bg='#FF6F00')
        check()

def clicked4():
    global turn
    if btn4["text"] == " ":
        if turn == 1:
            turn = 2;
            btn4["text"] = "X"
            btn4.config(fg='#FFD700', bg='#311B92')
        elif turn == 2:
            turn = 1;
            btn4["text"] = "O"
            btn4.config(fg='#FFD700', bg='#FF6F00')
        check()

def clicked5():
    global turn
    if btn5["text"] == " ":
        if turn == 1:
            turn = 2;
            btn5["text"] = "X"
            btn5.config(fg='#FFD700', bg='#311B92')
        elif turn == 2:
            turn = 1;
            btn5["text"] = "O"
            btn5.config(fg='#FFD700', bg='#FF6F00')
        check()

def clicked6():
    global turn
    if btn6["text"] == " ":
        if turn == 1:
            turn = 2;
            btn6["text"] = "X"
            btn6.config(fg='#FFD700', bg='#311B92')
        elif turn == 2:
            turn = 1;
            btn6["text"] = "O"
            btn6.config(fg='#FFD700', bg='#FF6F00')
        check()

def clicked7():
    global turn
    if btn7["text"] == " ":
        if turn == 1:
            turn = 2;
            btn7["text"] = "X"
            btn7.config(fg='#FFD700', bg='#311B92')
        elif turn == 2:
            turn = 1;
            btn7["text"] = "O"
            btn7.config(fg='#FFD700', bg='#FF6F00')
        check()

def clicked8():
    global turn
    if btn8["text"] == " ":
        if turn == 1:
            turn = 2;
            btn8["text"] = "X"
            btn8.config(fg='#FFD700', bg='#311B92')
        elif turn == 2:
            turn = 1;
            btn8["text"] = "O"
            btn8.config(fg='#FFD700', bg='#FF6F00')
        check()

def clicked9():
    global turn
    if btn9["text"] == " ":
        if turn == 1:
            turn = 2;
            btn9["text"] = "X"
            btn9.config(fg='#FFD700', bg='#311B92')
        elif turn == 2:
            turn = 1;
            btn9["text"] = "O"
            btn9.config(fg='#FFD700', bg='#FF6F00')
        check()

flag = 1

# Function to check for a win or tie
def check():
    global flag
    # Get text in each button
    b1 = btn1["text"]
    b2 = btn2["text"]
    b3 = btn3["text"]
    b4 = btn4["text"]
    b5 = btn5["text"]
    b6 = btn6["text"]
    b7 = btn7["text"]
    b8 = btn8["text"]
    b9 = btn9["text"]
    flag = flag + 1
    # Check for winning combinations
    if b1 == b2 and b1 == b3 and b1 == "O" or b1 == b2 and b1 == b3 and b1 == "X":
        win(btn1["text"])
    if b4 == b5 and b4 == b6 and b4 == "O" or b4 == b5 and b4 == b6 and b4 == "X":
        win(btn4["text"])
    if b7 == b8 and b7 == b9 and b7 == "O" or b7 == b8 and b7 == b9 and b7 == "X":
        win(btn7["text"])
    if b1 == b4 and b1 == b7 and b1 == "O" or b1 == b4 and b1 == b7 and b1 == "X":
        win(btn1["text"])
    if b2 == b5 and b2 == b8 and b2 == "O" or b2 == b5 and b2 == b8 and b2 == "X":
        win(btn2["text"])
    if b3 == b6 and b3 == b9 and b3 == "O" or b3 == b6 and b3 == b9 and b3 == "X":
        win(btn3["text"])
    if b1 == b5 and b1 == b9 and b1 == "O" or b1 == b5 and b1 == b9 and b1 == "X":
        win(btn1["text"])
    if b7 == b5 and b7 == b3 and b7 == "O" or b7 == b5 and b7 == b3 and b7 == "X":
        win(btn7["text"])
    if flag == 10:
        messagebox.showinfo("Tie", "Match Tied!!!  Try again :)")
        window.destroy()

# Function to handle win condition
def win(player):
    ans = "Game complete " + player + " wins "
    messagebox.showinfo("Congratulations", ans)
    window.destroy()

# Create buttons for the game
# Button grid positions are set using grid layout manager
btn1 = Button(window, text=" ", width=6, height=2, font=('Helvetica', '20'), command=clicked1, bg='#212121', fg='red', borderwidth=1)
btn1.grid(column=1, row=1)
btn2 = Button(window, text=" ", width=6, height=2, font=('Helvetica', '20'), command=clicked2, bg='#212121', fg='#FFD700', borderwidth=1)
btn2.grid(column=2, row=1)
btn3 = Button(window, text=" ", width=6, height=2, font=('Helvetica', '20'), command=clicked3, bg='#212121', fg='#FFD700', borderwidth=1)
btn3.grid(column=3, row=1)
btn4 = Button(window, text=" ", width=6, height=2, font=('Helvetica', '20'), command=clicked4, bg='#212121', fg='#FFD700', borderwidth=1)
btn4.grid(column=1, row=2)
btn5 = Button(window, text=" ", width=6, height=2, font=('Helvetica', '20'), command=clicked5, bg='#212121', fg='#FFD700', borderwidth=1)
btn5.grid(column=2, row=2)
btn6 = Button(window, text=" ", width=6, height=2, font=('Helvetica', '20'), command=clicked6, bg='#212121', fg='#FFD700', borderwidth=1)
btn6.grid(column=3, row=2)
btn7 = Button(window, text=" ", width=6, height=2, font=('Helvetica', '20'), command=clicked7, bg='#212121', fg='#FFD700', borderwidth=1)
btn7.grid(column=1, row=3)
btn8 = Button(window, text=" ", width=6, height=2, font=('Helvetica', '20'), command=clicked8, bg='#212121', fg='#FFD700', borderwidth=1)
btn8.grid(column=2, row=3)
btn9 = Button(window, text=" ", width=6, height=2, font=('Helvetica', '20'), command=clicked9, bg='#212121', fg='#FFD700', borderwidth=1)
btn9.grid(column=3, row=3)

# Button to reset the game
reset_btn = Button(window, text="Reset", width=8, height=2, font=('Helvetica', '12'), command=reset, bg='#FFD700', fg='#212121')
reset_btn.grid(column=1, row=4, columnspan=3, pady=10)

# Start the main event loop
window.mainloop()

