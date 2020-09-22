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
    # use the globally declared 'score' and 'play' variables
    global score
    global timeleft

    # if game is currently in play
    if timeleft > 0:

        # make the text entry box active
        e.focus_set()

        # if the color typed is correct
        if e.get().lower() == colors[1].lower():
            score += 1

        # clear the text entry box
        e.delete(0, tkinter.END)

        random.shuffle(colors)

        # change the color to type, by changing the text and the color to a random color value
        label.config(fg=str(colors[1]), text=str(colors[0]))

        # update the score
        scoreLabel.config(text='Score: ', str(score))

# countdown timer function
def countdown():
    global timeleft

    # if game is in play
    if timeleft > 0:
        # decrement the timer
        timeleft -= 1

        # update the time left label
        timeLabel.after(1000, countdown)

# driver code
# create a GUI window
root = tkinter.TK()

# set the title
root.title('Color Game')

# set the size
root.geometry('375x200')

# add the instruction label
instructions = tkinter.Label(root, text='Type the color of the words, and not the word text!',
                             font=('Helvetica', 12))
instructions.pack()

# add the score label
scoreLabel = tkinter.Label(root, text='Press enter to start',
                           font=('Helvetica', 12))
scoreLabel.pack()

# add a time label