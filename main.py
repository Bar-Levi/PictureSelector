# pip3 install pyautogui
# pip3 install Pillow
# pip3 install opencv-python
# pip3 install pygame
import os
from tkinter import *
from PIL import Image, ImageTk
import shutil
import pygame

BACKGROUND_COLOR = 'pink'

# Images:
arrows_right_image = Image.open('Assets/fast-forward.png')
arrows_left_image = arrows_right_image.rotate(180)
choose_image = Image.open('Assets/choices.png')
finish_image = Image.open('Assets/finish-line.png')

# Creating the window:
window = Tk()
try:
    pygame.init()
except Exception as e:
    print(e)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
window.title("Pictures Selector - by Bar Levi")
window.resizable(True, True)
window.config(bg=BACKGROUND_COLOR)
picture_index = 0
chosen_indexes = set()
images_already_calculated = {}


def CenterWindow(win):
    center_x = (win.winfo_screenwidth() - SCREEN_WIDTH) // 2
    center_y = (win.winfo_screenheight() - SCREEN_HEIGHT) // 2
    window.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}+{center_x}+{center_y}')
    return f'+{center_x}+{center_y}'  # Placing the window at the middle of the screen.


def CreateDirectory():
    directory_name = 'new_directory'
    try:
        shutil.rmtree(directory_name)
    except Exception as e:
        print(e)
    finally:
        os.mkdir(directory_name)


def ChoosePictures(path, directory):
    global chosen_indexes, BACKGROUND_COLOR
    window.geometry(CenterWindow(window))

    if ".DS_Store" in directory:
        directory.remove(".DS_Store")

    def HandleBackground():
        global BACKGROUND_COLOR
        if picture_index in chosen_indexes:
            BACKGROUND_COLOR = 'pink'
        else:
            BACKGROUND_COLOR = 'light green'

    def AddPicture(event=None):
        new_file_name = "ChosenPicture_" + str(picture_index) + "." + image_path.split('.')[-1].lower()
        destination_directory = os.getcwd() + "/new_directory"
        if new_file_name not in os.listdir(destination_directory):
            try:
                shutil.copy(image_path, destination_directory)
                os.rename(destination_directory+'/'+directory[picture_index], destination_directory+'/'+new_file_name)
                chosen_indexes.add(picture_index)
            except:
                print("Failed passing the image")
        ChoosePictures(path, directory)

    def RemovePicture(event=None):
        new_file_name = "ChosenPicture_" + str(picture_index) + "." + image_path.split('.')[-1].lower()
        destination_directory = os.getcwd() + "/new_directory"
        os.remove(destination_directory+'/'+new_file_name)
        chosen_indexes.remove(picture_index)
        ChoosePictures(path, directory)

    def ReturnPicture(event=None):
        global picture_index
        picture_index = max(0, picture_index-1)
        ChoosePictures(path, directory)

    def SkipPicture(event=None):
        global picture_index
        picture_index = min(len(directory) - 1, picture_index + 1)
        ChoosePictures(path, directory)

    def TakeAChoice(event=None):
        if picture_index in chosen_indexes:
            RemovePicture(event)
        else:
            AddPicture(event)

    while True:
        for feature in window.winfo_children():
            feature.pack_forget()
            feature.place_forget()
        HandleBackground()
        window.config(bg=BACKGROUND_COLOR)
        image_path = path + '/' + directory[picture_index]
        if picture_index in images_already_calculated.keys():
            real_image = images_already_calculated[picture_index]
        else:
            image_instance = Image.open(image_path).resize((1000, 600))
            real_image = ImageTk.PhotoImage(image_instance)
            images_already_calculated[picture_index] = real_image
        Label(window, image=real_image).pack()
        finish_picture = ImageTk.PhotoImage(finish_image)
        Button(window, image=finish_picture, command=quit).place(x=150, y=610)
        choices_picture = ImageTk.PhotoImage(choose_image)
        Button(window, image=choices_picture, command=TakeAChoice).place(x=250, y=610)
        arrows_right = ImageTk.PhotoImage(arrows_right_image)
        Button(window, image=arrows_right, command=SkipPicture).place(x=450, y=610)
        arrows_left = ImageTk.PhotoImage(arrows_left_image)

        if picture_index in chosen_indexes:
            l1 = Label(window, text="Picture was already chosen.", fg='red', font=('David', 30, 'underline'))
            l1.place(x=550, y=630)
        else:
            l2 = Label(window, text="You can choose it!", fg='green', font=('David', 40, 'underline'))
            l2.place(x=550, y=630)

        Button(window, image=arrows_left, command=ReturnPicture).place(x=350, y=610)
        window.bind('<Right>', SkipPicture)
        window.bind('<Left>', ReturnPicture)
        window.bind('<space>', TakeAChoice)
        window.focus_set()




        window.mainloop()


def ChooseDirectory():
    for feature in window.winfo_children():
        feature.pack_forget()
    center_x = (window.winfo_screenwidth() - SCREEN_WIDTH) // 2
    center_y = (window.winfo_screenheight() - SCREEN_HEIGHT) // 2
    window.geometry(f'+{center_x}+{center_y}')
    Label(window, text="Welcome to Pictures Selector!", font=('David', 30, 'underline'), bg=BACKGROUND_COLOR).pack()
    Label(window, text="Please enter the directory's path:", font=('David', 15, 'underline'), bg=BACKGROUND_COLOR).pack()
    directory_path = Entry(window, bg="white", highlightbackground=BACKGROUND_COLOR)
    directory_path.pack()

    def GetDirectoryPath(event=None):
        path = directory_path.get()
        directory = os.listdir(path)
        ChoosePictures(path, directory)

    open_button = Button(window, text="Open", command=GetDirectoryPath, highlightbackground=BACKGROUND_COLOR)
    open_button.pack()
    window.bind('<Return>', GetDirectoryPath)


CreateDirectory()
ChooseDirectory()
window.mainloop()