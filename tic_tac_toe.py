
"""
 Tic Tac Toe Game Using Python Lang.. & Random and tkinter model

 **Created by Abdullah EL-Yamany**


 Channal => Korsat X programming - كوريات فى البرمجه
 Video Link ==> https://youtu.be/vVJJfJLIvL4
 Video Name => python projects - tic tac toe X O game | عمل لعبه كامله بلغة بايثون
"""

#================================

from tkinter import *
import random as rd


def next_turn(row, col):

    global player

    if game_btns[row][col]['text'] == "" and check_winner() == False :

        if player == players[0] :
            game_btns[row][col]['text'] = player


            if check_winner() == False :
                player =players[1]
                label.config(text=("[ " + players[1] + " ] turn"))

            elif check_winner() == True :
                label.config(text=("[ " + players[0] + " ] Wins!"))

            elif check_winner() == 'tie' :
                label.config(text=("Tie, No Winner"))

        elif player == players[1] :
            game_btns[row][col]['text'] = player


            if check_winner() == False :
                player =players[0]
                label.config(text=("[ " + players[0] + " ] turn"))

            elif check_winner() == True :
                label.config(text=("[ " + players[1] + " ] wins!"))

            elif check_winner() == 'tie' :
                label.config(text=("Tie, No Winner!"))



def check_winner():

    for row in range (3):
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] != "" :
            game_btns[row][0].config(bg='cyan')
            game_btns[row][1].config(bg='cyan')
            game_btns[row][2].config(bg='cyan')
            return True

    for col in range (3):
        if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] != "" :
            game_btns[0][col].config(bg='cyan')
            game_btns[1][col].config(bg='cyan')
            game_btns[2][col].config(bg='cyan')
            return True

    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] != "" :
        game_btns[0][0].config(bg='cyan')
        game_btns[1][1].config(bg='cyan')
        game_btns[2][2].config(bg='cyan')
        return True

    elif game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] != "" :
        game_btns[0][2].config(bg='cyan')
        game_btns[1][1].config(bg='cyan')
        game_btns[2][0].config(bg='cyan')
        return True

    if check_empty_spaces() == False :
        for row in range(3):
            for col in range(3):
                game_btns[row][col].config(bg='red')
        return 'tie'

    else:
        return False



def check_empty_spaces():

    spaces = 9

    for row in range(3):
        for col in range(3):
            if game_btns[row][col]['text'] != "" :
                spaces -= 1

    if spaces == 0 :
        return False
    else :
        return True



def start_new_game():

    global player
    player = rd.choice(players)

    label.config(text=("[ " + player + " ] turn"))

    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text='', bg='#f0f0f0')




window = Tk()
window.title("Tic-Tac-Toe")


players = ['x', 'o']
player = rd.choice(players)


game_btns = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


label = Label(text=("[ " + player + " ] turn"), font=("consolas", 25), fg='white', bg='black')
label.pack(fill=X)


restart_btn = Button(text="Restart",
                  font=("consolas", 25),
                  command=start_new_game
              )
restart_btn.pack()


btns_frame = Frame(window)
btns_frame.pack(pady=13)


for row in range(3):
    for col in range(3):
        game_btns[row][col] = Button(btns_frame,
                                  text="",
                                  font=("consolas", 25),
                                  width=7,
                                  height=3,
                                  command=lambda row=row, col=col : next_turn(row, col)
                              )
        game_btns[row][col].grid(row=row, column=col)


window.mainloop()
