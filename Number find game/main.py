# for UBUNTU 

# Now its Gui:- 
from tkinter import *
import tkinter
import random as rd

# =======================================================
# Tkinter widget Objects :- 

win = Tk()
win.config(bg="yellow")
win.attributes("-topmost", True)
win.title("Number Game")
win.geometry("1200x1200")

# Image Setting in Bg :-

bg = PhotoImage(file="/mnt/Common Drive/Projects/PYTHON PROJECTS/GIT PYTHON PROJECTS/Number find game/guess.png")
mylabel = Label(win,image=bg,)
mylabel.place(x=0, y=0, relwidth=1, relheight=1)

# =======================================================

# Some Important variables for storing random generated number, counting user chances, guesses. 

rand_num = rd.randint(1, 10)
chance_left = 5
guess = 0
user_guess = None
wrong_guess = None

# print(rand_num)

# =====================================================================================

# Program Ending Methods:- 

# Exit Method, when user Won:- 
def end_game():
    game_ovr_label = Label(win, font=("Times New Roman",15), text="🥳 🥳  😇 😇  🤗 🤗")
    game_ovr_label.place(x=315, y=765, height=50, width=510)
    
# Exit Method, when user did not won:-
def end_game2():
    check_button.config(state="disabled")

    wrong_guess.config(text="😔😔😔 Better luck next time.")

    game_message = Label(win, text="Game Over! You've used all your chances.", font=("Times New Roman", 15, "bold"))
    game_message.place(x=200, y=600, height=50, width=800)


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

# if player gusses right:- 
    if user_guess == rand_num:
        guess_result = Label(win, font=("Times New Roman",15),text="Burrah!!🍾🍾🍾🍾🎉🎉...You won")
        guess_result.place(x=200, y=500, height=50, width=800)
        chance_count(guess)

        # After 1 or more chances when player wins we hides the previous "wrong" message label with this message.
        # If Player wins in 1st chance then also we display this message.
        wrong_guess.config(text="Game Over You won!  😇 🤗") 
        wrong_guess.place(x=200, y=900, height=50, width=700)

        end_game()

# if player didn't able to guess in given chances:- 
    elif chance_left ==0:
            end_game2()

# when user guess wrong number:- 
    else:
        if user_guess > rand_num :
            wrong_guess = Label(win, font=("Times New Roman",15),text="No ! ❌❌❌, please guess little small. ")
            wrong_guess.place(x=200, y=900, height=50, width=700)

        elif user_guess < rand_num:
            wrong_guess = Label(win, font=("Times New Roman",15),text="No ! ❌❌❌, please guess little large. ")
            wrong_guess.place(x=200, y=900, height=50, width=700)

# =====================================================================================
            
# Count the Chance of Player:- 
            
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

    compliment_message.place(x=150, y=600, height=50, width=900)
        
# =====================================================================================

# Initial Labels and their placement:- 

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
check_button.place(x=315, y=600, height=50, width=410)

win.mainloop()


#  🥳 🥳 😇 😇 😇 😇 🤗 🤗 🤗 🤗
# (x=150, y=800, height=50, width=900)
