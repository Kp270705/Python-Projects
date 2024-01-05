import random as rd

rand_num = rd.randint(1, 10)
user_guess = None

guess = 0
print(rand_num)

print("\n\t-:Hey User lets satrt the game:- ")
print("You will have only 5 chances to identify the correct number b/w 1-10:-")
print("\n\t.....So lets start it.....🎉🎉🎉")

# ------------------------------------------------------------------------------------------

for i in range(1, 6):
    # while(user_guess != rand_num):

    # while(guess != 5):
    user_guess = int(input("Enter your guess:- "))
    guess = guess + 1

    if user_guess == rand_num:
        print("\nBurrah!!🍾🍾🍾🍾🎉🎉")
        print(rand_num," is the right number.")
        break

    else:
        if user_guess > rand_num:
            # print("You guessed wrong! Enter a samller number:- ")
            print("You guessed wrong! ❌❌❌")
        else:
            # print("Wrong Number! Enter a greater number.")
            print("You guessed Wrong! ❌❌❌")

# --------------------------------Break................. Part- 2---------------------------------

# while(user_guess != rand_num):

# # while(guess != 5):
#     user_guess = int(input("Enter your guess:- "))
#     guess = guess +1;

#     if user_guess == rand_num:
#         print("Burrah!!🍾🍾🍾🍾🎉🎉")
#         print("You enter the right number:- ")

#     else:
#         if(user_guess > rand_num):
#             print("You guessed wrong! Enter a samller number:- ")
#         else:
#             print("Wrong Number! Enter a greater number.")

# -----------------------------------------------------------------------------------------------
if guess == 1 and user_guess == rand_num:
    print("Bang On! You hit right one, in one guess:- 🫡  😎 👌 ✌️")

elif guess == 2 and user_guess == rand_num:
    print(" Smart! You hit right one, in two guesses:- 😎 👌 ✌️")

elif guess == 3 and user_guess == rand_num:
    print(" Good! You hit right one, in three guesses:- 👌 ✌️")

elif guess == 4 and user_guess == rand_num:
    print("Finally!!! 😮‍💨 after ", guess, " guessess, You are right.")

elif guess == 5 and user_guess == rand_num:
    print("Babes In last chance !!! You are right. 🌜 🌜")

else:
    print("\nProgram Finishes.....")
    print("😔😔😔 Better luck next time \n")

# with open("Hiscore.txt","r") as f:
