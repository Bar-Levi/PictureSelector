# PictureSelector
Picture Selector is a program that allows you to easily select and organize your pictures in a user-friendly interface.<br>
It provides a simple and intuitive way to browse and select your photos, making it easy to manage and organize your digital photo collection.

# Project Title
Pictures Selector is a Python application that lets you browse a directory of pictures, choose which ones you like, and create a new directory with the chosen pictures.<br>
The user interface is implemented with tkinter and the pictures are displayed using Pillow and OpenCV.<br>
Pygame is used to handle keyboard events.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Installation

To run the program, install the necessary dependencies (pyautogui, Pillow, opencv-python, and pygame) and run the script. When prompted, select the directory containing the pictures you want to browse.<br>
You can navigate through the pictures using the arrow keys, and select or unselect them by pressing the space bar as well as using the mouse.<br>
The chosen pictures will be saved to a new directory named 'new_directory' in the current working directory.

## Usage

When you run the program, a window will show up on your screen.<br>
You should enter the path of the pictures' directory into the textbox and press the "open" button.<br>
The pictures window shows up, and you should be able to pass through the pictures and choose/unchoose pictures.<br>
**After you finish choosing and closing the program** -
Make sure you move the new_directory to a different place in your computer, or else it would initialize itself on the next time you run the program.

## Dependencies
- Make sure to install all of the relevant modules and libraries from the requirements.txt file.<br>
- Make sure the directory you're working with doesn't include sub-directories.
