# Change your start page? … 
# Currently it's set to Home. You can change it at any time in Settings.

import cv2
from tkinter import *
from PIL import Image, ImageTk
import os 
import time

# logic design method code:-
def resizing_method():
    file = machine_ask_input_file.get()

    destination = f"Final {file}"
    scale_percent = 50
    src = cv2.imread(file, cv2.IMREAD_UNCHANGED)

    # calculate the 50 percent of original dimensions.
    new_width = int(src.shape[1] * scale_percent / 100)
    new_height = int(src.shape[0] * scale_percent / 100)

    output = cv2.resize(src, (new_width, new_height))
    cv2.imwrite(destination, output)

    final_file_output.config(text=destination)

    # Output Label code:- 
    # output label placement:-
    final_file.place(x=100, y=600, height=100, width=600)

    # output's file name label placement:-
    final_file_output.place(x=800, y=600, height=100, width=400)

# exit button method:-  
def exit_method():
    win.destroy()
    
 
# base design:-
win = Tk()
win.title("Image Size precizor")
win.attributes("-topmost", True)
win.config(bg="pink")
win.geometry("1400x900")

# # ===================================================================
# Create a canvas widget
canvas = Canvas(win, width=1400, height=900)
canvas.pack()

# Load the background image
file = "/mnt/Common Drive/Projects/PYTHON PROJECTS/Git Python Projects/Image Cropper D/resizer.png"
image = Image.open(file)

# Resize the image to the size of the canvas
photo_image = ImageTk.PhotoImage(image.resize((1600, 1200), Image.LANCZOS))

# Create an image object and display it on the canvas
canvas.create_image(0, 0, image=photo_image, anchor="nw")
# # ===================================================================

# our app intro label:-
tittlee = Label(win, text="Welcome to image precisor:- ", font=("Times New Roman", 25, "bold"))
tittlee.place(x=225, y=50, height=100, width=900)

# our app intro label:-
tittlee2 = Label(win,text="'Image precisor' exclusively processes images found within its application directory:",font=("Times New Roman", 12, "bold"))
tittlee2.place(x=70, y=170, width=1200)

# machine say user to give input:-
machine_ask = Label(text="Enter your file name here 👉👉 ", font=("Times New Roman", 15, "bold"))
machine_ask.place(x=100, y=350, height=100, width=600)

# machine taking input from user:-
machine_ask_input_file = StringVar()
op = Entry(text=" ", font=("Times New Roman", 15, "bold"), textvariable=machine_ask_input_file)
op.place(x=800, y=350, height=100, width=400)

# output label:-
final_file = Label(text="Here is your resized file 👉 👉", font=("Times New Roman", 15, "bold"))

# output's file name label:-
final_file_output = Label(text=" ", font=("Times new Roman", 15, "bold"))

# Done button code:-
done_button = Button(win, text="Done", font=("Times New Roman", 20), command=resizing_method)
done_button.place(x=650, y=500, height=50, width=200)

# exit button code:-
exit_button = Button(win, text="exit", font=("Times New Roman", 20), command=exit_method, bg="yellow", fg="green")
exit_button.place(x=700, y=790, height=50, width=100)

win.mainloop() 


