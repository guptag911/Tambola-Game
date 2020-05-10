import os
import random
import time
import cv2
import threading
import tkinter
import tkinter.messagebox
from PIL import Image
from playsound import playsound

# 	Used to Save audio of numbers in audio folder...Saves Time..Took 3 min to run!!
"""from gtts import gTTS
for i in range(91):
    mytext = str(i)
    speaker = gTTS(text=mytext,lang='en',slow=False)
    speaker.save(path + mytext + ".mp3")
"""

'''from gtts import gTTS
my_text = "Only_number"
speaker = gTTS(text="Only number",lang='en',slow=False)
speaker.save(path + my_text + ".mp3")
'''

path = r"/home/abhay/Desktop/House_Number_picker/audio/"

#cv2.namedWindow('board')
img = cv2.imread(r'/home/abhay/Desktop/House_Number_picker/board2.png')

numbers = [] 	# Maintaing for numbers till 90.
numbers1 = []	# Maintaing for checking of no repetition.

for i in range(1,91):
    numbers.insert(i,i)

count = 90
color = (0, 0, 255)

flag=False

def start():
    global flag, count
    if(flag == False):
        flag = True
        game_begins = threading.Thread(target=my_game, name='game_begins')
        game_begins.start()

def pauser():
    global flag
    flag= False

def pause():

    pause_game = threading.Thread(target=pauser, name='pause_game')
    pause_game.start()

    global board_img, last_no, number_img
    board_img = tkinter.PhotoImage(file=r'/home/abhay/Desktop/House_Number_picker/current_board.png')
    my_board.configure(image=board_img)
    number_img = tkinter.PhotoImage(file=r"/home/abhay/Desktop/House_Number_picker/numbers/" + str(last_no) + ".png")
    my_number.configure(image=number_img)

def end():
    exit(0)

last_no = 0

def my_game():
    global count, my_board, my_number, last_no, my_delay, rem_numbers, prev_number
    time.sleep(0.5)
    try:
        while(flag and count!=0):
            n = random.choice(numbers)
            numbers1.insert(n,count)
            x = 18 + (n%10)*82
            y = 100 + (int(n/10))*82
            if(n%10==0):
                x=838
                y=y-82
            image = cv2.circle(img, (x+42,y+42), 32, color, 4)
            #cv2.destroyAllWindow()
            #cv2.imshow('board',image)
            cv2.imwrite(r'/home/abhay/Desktop/House_Number_picker/current_board.png',image)
            time.sleep(1)

            prev_number.config(text="Previous Number: " + str(last_no))
            board_img = tkinter.PhotoImage(file=r'/home/abhay/Desktop/House_Number_picker/current_board.png')
            my_board.configure(image=board_img)

            number_img = tkinter.PhotoImage(file=r"/home/abhay/Desktop/House_Number_picker/numbers/" + str(n) + ".png")
            my_number.configure(image = number_img)

            if (n < 10):
                playsound(r"" + path + "Only_number.mp3")
                # os.system(r"mpg321 " + path + "Only_number.mp3")
            playsound(r"" + path + str(n) + ".mp3")
            # os.system(r"mpg123 " + path + str(n) + ".mp3")
            #my_board.image(board_img)

            numbers.remove(n)
            count-=1

            rem_numbers.config(text="Remaining Numbers: " + str(count))
            if(count <=10):
                rem_numbers.config(fg = 'red')

            last_no = n
            if(len(my_delay.get())==0):
                delay_time = 2
            else:
                delay_time = int(my_delay.get())
            time.sleep(delay_time)
        if (count == 0):
            tkinter.messagebox.showinfo("Game Over!", "Game Over! All numbers have been called out!")
    except:
        print("Some Error has eccoured!!")

window = tkinter.Tk()
window.geometry('1500x1500')
window.config(bg = 'white')
window.title("Tambola")

board_frame = tkinter.Frame(window).pack(side = 'left')
functional_frame = tkinter.Frame(window).pack(side = 'right')
board_img = tkinter.PhotoImage(file = r'/home/abhay/Desktop/House_Number_picker/board2.png')
my_board = tkinter.Label(board_frame, image = board_img)
my_board.pack(side = 'left')

number_img = tkinter.PhotoImage(file = r"/home/abhay/Desktop/House_Number_picker/numbers/start.png")
my_number = tkinter.Label(functional_frame, image = number_img)
my_number.pack(side = 'top')

exit_button = tkinter.Button(functional_frame,text = "EXIT",command=lambda: end(), bd=5, width=30, height=2, activebackground='orange')
exit_button.place(x=1150, y=870)
pause_button = tkinter.Button(functional_frame,text = "PAUSE",command=lambda: pause(), bd=5, width=30, height=2, activebackground='orange')
pause_button.place(x=1150, y=810)
start_button = tkinter.Button(functional_frame,text = "START",command=lambda:  start(), bd=5, width=30, height=2, activebackground='orange')
start_button.place(x=1150, y=750)
time_label = tkinter.Label(functional_frame, text="Enter Delay Time: ", font=('Candara 13 bold'), bg = 'white')
time_label.place(x=1150, y=650)
my_delay = tkinter.Entry(functional_frame, width = 10)
my_delay.place(x=1340, y=650)
my_delay.insert(0, '2')

rem_numbers = tkinter.Label(functional_frame, text = "Remaining Numbers: 90", font=('Candara 15 bold'), bg = 'white')
rem_numbers.place(x = 1150, y = 550)
prev_number = tkinter.Label(functional_frame, text = "Previous Number: ", font=('Candara 15 bold'), bg = 'white')
prev_number.place(x = 1150, y = 600)

name_label = tkinter.Label(functional_frame, text = "© Made By- Abhay Gupta, Designed By- Shubham Kalra ©",font = ('Candara 10 bold')).pack(side = 'bottom')
window.mainloop()
