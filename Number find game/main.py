# for UBUNTU 

# Now its Gui:- 
from tkinter import *
import tkinter
import random as rd

# =======================================================

win = Tk()
win.config(bg="yellow")
win.attributes("-topmost", True)
win.title("Number Game")
win.geometry("1200x1200")

# =======================================================

# bg = PhotoImage(file="/mnt/Common Drive/Projects/PYTHON PROJECTS/Git Python Projects/Number find game/guess.png")
# mylabel = Label(win,image=bg,)
# mylabel.place(x=0, y=0, relwidth=1, relheight=1)

                        # or 

bg = PhotoImage(file="/mnt/Common Drive/Projects/PYTHON PROJECTS/GIT PYTHON PROJECTS/Number find game/guess.png")
mylabel = Label(win,image=bg,)
# mylabel.place(anchor='center')
mylabel.place(x=0, y=0, relwidth=1, relheight=1)

# =======================================================

rand_num = rd.randint(1, 10)
# print(rand_num)

chance_left = 5
guess = 0
user_guess = None
wrong_guess = None

# =====================================================================================
# Program Ending Methods:- 

def end_game():
    check_button.config(state="disabled")
    info_label.config(text="Game Over! You Won.")

def end_game2():
    check_button.config(state="disabled")
    compliment_message2 = Label(win, font=("Times New Roman",15), text="😔😔😔 Better luck next time \n")
    compliment_message2.place(x=15, y=335,height=50, width=470)

    # info_label.config(text="Game Over! You've used all your chances.")

    game_message = Label(win, text="Game Over! You've used all your chances.", font=("Times New Roman", 15, "bold"))
    game_message.place(x=15, y=400, height=50, width=470)

# =====================================================================================
# Method for check user guess is right or not:- 
    
def check_method():
    global chance_left
    chance_left -= 1
    
    global guess 
    guess += 1
    
    global user_guess
    global wrong_guess
 
    user_guess = inputt_label.get()
    user_guess = int(user_guess)

    if user_guess == rand_num:
        guess_result = Label(win, font=("Times New Roman",15),text="Burrah!!🍾🍾🍾🍾🎉🎉...You won")
        guess_result.place(x=200, y=435, height=50, width=800)
        chance_count(guess)

        end_game()

        # ----------------------------------------------------------------------------------------------------------------
# Replay Button:- 
        
        # replay_button = Button(win, text="Replay Again ", font=("Times New Roman", 15), command=check_method)
        # replay_button.place(x=200, y=400, height=25, width=110)

        # ----------------------------------------------------------------------------------------------------------------

    elif chance_left ==0:
            end_game2()

    else:
        if user_guess > rand_num :
            guess_result = Label(win, font=("Times New Roman",15),text="No ! ❌❌❌, please guess little small. ")
            guess_result.place(x=200, y=900, height=50, width=700)

        elif user_guess < rand_num:
            guess_result = Label(win, font=("Times New Roman",15),text="No ! ❌❌❌, please guess little large. ")
            guess_result.place(x=200, y=900, height=50, width=700)

        # -----------------------------------------------------------------------------------------------------

        # guess_result = Label(win, font=("Times New Roman",15),text="You guessed wrong! ❌❌❌")
        # guess_result.place(x=58, y=280, height=50, width=400)

# =====================================================================================

def chance_count(guess):
    if guess == 1 :
        compliment_message = Label(win,  font=("Times New Roman",15),text="Bang On! You hit right one, in one guess:- 🫡  😎 👌 ✌️")

    elif guess == 2 :
        compliment_message = Label(win,  font=("Times New Roman",15),text=" Smart! You hit right one, in two guesses:- 😎 👌 ✌️")

    elif guess == 3 :
        compliment_message = Label(win,  font=("Times New Roman",15),text=" Good! You hit right one, in three guesses:- 👌 ✌️")
        
    elif guess == 4 :
        compliment_message = Label(win,  font=("Times New Roman",15),text="Finally!!! 😮 😗 after 4 guessess, You are right.")

    elif guess == 5 :
        compliment_message = Label(win,  font=("Times New Roman",15),text="Babes In last chance !!! You are right. 🫣 🫣")

    compliment_message.place(x=150, y=900, height=50, width=900)
        
# =====================================================================================


firstlabel = Label(win, text="Number Finding Game. 😛 ", font=("Times New Roman", 17, "bold"))
firstlabel.place(x=350, y=10, height=50, width=550)


inst_label = Label(win, text="-:Hey User lets satrt the game:- ", font=("Times New Roman", 13, "bold"))
inst_label.place(x=275, y=100, height=50, width=650)
inst_label2 = Label(win, text="Guess the correct number between 1 and 10 in 5 chances.", font=("Times New Roman", 11, "bold"))
inst_label2.place(x=210, y=145, height=40, width=780)


info_label = Label(win, text="Enter your number here:- 👉 👉", font=("Times New Roman", 15, "bold"))
info_label.place(x=100, y=300, height=50, width=600) 


inputt_label = StringVar()
rl_inputt_label = Entry(text=" ", font=("Times New Roman", 17, "bold"), textvariable=inputt_label)
rl_inputt_label.place(x=800, y=300, height=50, width=90)


check_button = Button(win, text="Check It. ", font=("Times New Roman", 20), command=check_method)
check_button.place(x=315, y=570, height=50, width=410)

win.mainloop()


