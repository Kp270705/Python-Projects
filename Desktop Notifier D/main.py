import time
from plyer import notification

if __name__ == "__main__":

    # print("\nThis is the notification system for your machine, which will reminds you to drink water, in every one hour.")
    # print("\nIf you type anything as input, this program will run in background for next one hour. \nAnd for exiting the program, you can only manually kill the terminal or command line.")
    # print("\nSo to exit the program:-")
    # print("Type 'bye' to exit the program. ")

    while True:

        # inp = input("Enter choice:- ")
        # if inp == "bye":
        #     break

        # else:
        notification.notify(title = "Uncle ji paani pee lijiye",     
            message = "Drinking water is essential for life. It helps to regulate body temperature, transport nutrients, and remove waste products. It is also important for maintaining healthy skin, hair, and nails. Aim to drink at least 8 glasses of water per day.",

            app_icon = "/mnt/Common Drive/Projects/PYTHON PROJECTS/Git Python Projects/Desktop Notifier D/water.ico",
            timeout=10
            )

        time.sleep(60*60)
