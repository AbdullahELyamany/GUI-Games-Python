
"""
 Tic Tac Toe Game Using Python Lang.. & Random and tkinter model
 
 **Created by Abdullah EL-Yamany**
"""

from tkinter import *
import random



def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and check_winner() is False :
        if player == players[0]:
            buttons[row][column]["text"] = player

            if check_winner() is False:
                player = players[1]
                label.config(text =(f"[{players[1]}] Turn"))
    
            elif check_winner() is True:
                label.config(text = (f"{players[0]} Is Wins"))
    
            elif check_winner() == "Tie":
                label.config(text = "Tie!")

        else:
            buttons[row][column]["text"] = player
    
            if check_winner() is False:
                player = players[0]
                label.config(text =(f"[{players[0]}] Turn"))
    
            elif check_winner() is True:
                label.config(text = (f"{players[1]} Is Wins"))
    
            elif check_winner() == "Tie":
                label.config(text = "Tie!")


def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg = "green")
            buttons[row][1].config(bg = "green")
            buttons[row][2].config(bg = "green")
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg = "green")
            buttons[1][column].config(bg = "green")
            buttons[2][column].config(bg = "green")
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
         buttons[0][0].config(bg = "green")
         buttons[1][1].config(bg = "green")
         buttons[2][2].config(bg = "green")
         return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg = "green")
        buttons[1][1].config(bg = "green")
        buttons[2][0].config(bg = "green")
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg = "yellow")
        return "Tie"
    else:
        return False


def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True


def new_game():
    global player
    player = random.choice(players)
    label.config(text = f"[{player}] Turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text = "", bg = "#F0F0F0")



root = Tk()
root.geometry("1000x700")
#root.title("Music Player")
root.configure(background = "gray")
#root.resizeable(False, False)

players = ['X', 'O']
player = random.choice(players)

buttons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

top_frame = Frame(root, bg = "#5D6D7E", width = 1000, height = 250)
top_frame.place(x = 0, y = 0)


game_title = Label(top_frame, text = "Tic Tac Toe Using Python", bg = "#5D6D7E", fg = "white", font = ("", 20))
game_title.place(x = 135, y = 0)


reset_button = Button(top_frame, text = "Restart Game", bg = "#5D6D7E", fg = "white", font = ("arial", 15), command = new_game)
reset_button.place(x = 340, y = 93)

label = Label(top_frame, text = f"[{player}] Turn", font = ('arial', 15), bg = "#5D6D7E", fg = "white")
label.place(x = 410, y = 180)


btm_frame = Frame(root, bg = "#FFFFFF", width = 600, height = 580)
btm_frame.place(x = 170, y = 290)


for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(btm_frame,
                                      text = "",
                                      font = ("arial", 20),
                                      width = 5,
                                      height = 2,
                                      command = lambda row = row, column = column: next_turn(row, column)
                               )
        buttons[row][column].grid(row = row, column = column)




root.mainloop()
