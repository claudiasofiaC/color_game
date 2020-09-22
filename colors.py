# import modules
import tkinter
import random

# list of possible colors
colors = ['Red', 'Cyan', 'Green', 'Pink', 'Fuchsia', 'Lime', 'Orange',
          'Yellow', 'White', 'Black', 'Purple']

score = 0

# the game time left, intiallly 30secs
timeleft =60

# function that will start the game
def startGame(event):
    if timeleft == 60:
        # start the countdown timer
        countdown()

    # run the function to choose the next color
    nextColor()

# function to choose and display the next color
def nextColor():
    # use the globally declared 'score'
