# for ubuntu:- 


from tkinter import *
from tkinter import ttk
import PIL
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import PhotoImage

# import weather_details by requesting to weather api
import requests


weather_to_emoji = {
    "Clear": "☀️",
    "Clouds": "☁️",
    "moderate rain": "🌦️",
    "Rain": "🌧️",
    "Thunderstorm": "⛈️",
    "Snow": "❄️",
    "Mist": "🌫️",
    "Fog": "🌫️",
    "humidity": "🌡️",
    "Haze": "🌫️"

    # Add more weather conditions and corresponding emojis as needed
}

win = tk.Tk()
win_width = win.winfo_width()
win_height = win.winfo_height()
win.title("Graphian App")
win.attributes("-topmost", True)
win.config(bg="blue")
win.geometry("1100x1000")

# ================================== start of get weather data method =================================
def get_Weather_data():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" +city+ "&appid=8e256899b0c3ae224ca393085e8c5e15").json()
    
# this will show temperature of our city from above api in data variable.
    temperature_label1.config(text=(data["main"]["temp"]) - 273.15) # this will convert our weather from kelvin to degree celsius.

# this will show climate of our city from above api in data variable.
    weather_condition = data["weather"][0]["main"] #this line gets information of climate from api and store in 'weather_condition'.

    # Update the weather emoji label based on the weather condition
    if weather_condition in weather_to_emoji:
        weather_emoji = weather_to_emoji[weather_condition]
        climate_label1.config(text=f"{weather_condition} {weather_emoji}")
    else:
        climate_label1.config(text=(data["weather"][0]["main"]))


# this will show pressure of our city from above api in data variable.
    pressure_label1.config(text=data["main"]["pressure"])

# ================================== end of get weather data method ===================================

# exit button method:-  
def exit_method():
    win.destroy()

# # ===================================================================

# Create a canvas widget
canvas = Canvas(win, width=1400, height=1400)
canvas.pack()

# Load the background image
file = "/mnt/Common Drive/Projects/PYTHON PROJECTS/Git Python Projects/Weather App D/weath6.png"
image = Image.open(file)

# Resize the image to the size of the canvas
photo_image = ImageTk.PhotoImage(image.resize((1600, 1200), Image.LANCZOS))

# Create an image object and display it on the canvas
canvas.create_image(0, 0, image=photo_image, anchor="nw")

# # ===================================================================

# list of state for climatic location:-
state_list = [
    "Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar",
    "Chhattisgarh","Goa","Gujarat","Haryana",
    "Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka",
    "Kerala","Madhya Pradesh","Maharashtra","Manipur",
    "Meghalaya","Mizoram","Nagaland","Odisha",
    "Punjab","Rajasthan","Sikkim","Tamil Nadu",
    "Telangana","Tripura","Uttar Pradesh","Uttarakhand",
    "West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli",
    "Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry",
]


# label code:-
nam_label = Label(
    win, text="Graphian weather App", font=("Times New Roman", 25, "bold") 
)
nam_label.place(x=210, y=50, height=75, width=680)


# combox code:-
# it (Combobox) is used to create a dropdown box.
city_name = StringVar()
com = ttk.Combobox(text=" ", values=state_list, font=("Times New Roman", 15), textvariable=city_name )
com.place(x=310, y=175, height=75, width=480)  # this place method is used to place the combox() in our webapp. It is used to set line and length of our drop down box from both x, y and z axis.


# temp. label value:-
temperature_label = Label(win, text="Temperature in ( ° C )", font=("Times New Roman", 20))
temperature_label.place(x=30, y=500, height=50, width=490)

# temp. value label:-
temperature_label1 = Label(win, text=" ", font=("Times New Roman", 20))
temperature_label1.place(x=625, y=500, height=50, width=445)


# climate label:-
climate_label = Label(win, text="Climate", font=("Times New Roman", 20))
climate_label.place(x=30, y=590, height=50, width=490)

# climate label value:-
climate_label1 = Label(win, text=" ", font=("Times New Roman", 20))
climate_label1.place(x=625, y=590, height=50, width=445)


# pressure label:-
pressure_label = Label(win, text="Pressure", font=("Times New Roman", 20))
pressure_label.place(x=30, y=680, height=50, width=490)

# pressure label value:-
pressure_label1 = Label(win, text=" ", font=("Times New Roman", 20))
pressure_label1.place(x=625, y=680, height=50, width=445)


# Done Button code:-
done_button = Button(win, text="Done", font=("Times New Roman", 20),command=get_Weather_data)
done_button.place(x=475, y=350, height=50, width=150)

# Exit Button code:-
done_button = Button(win, text="close", font=("Times New Roman", 20), fg="black", bg="light blue", command=exit_method)
done_button.place(x=475, y=840, height=50, width=150)

win.mainloop()


