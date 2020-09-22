# import modules
import tkinter
import random

# list of possible colors
colors = ['Red', 'Cyan', 'Green', 'Pink', 'Fuchsia', 'Lime', 'Orange',
          'Yellow', 'Grey', 'Black', 'Purple']

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
        scoreLabel.config(text='Score: ' + str(score))

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
root = tkinter.Tk()

# set the title
root.title('Color Game')

# set the size
root.geometry('700x300')

# add the instruction label
instructions = tkinter.Label(root, text='Type the color of the words, and not the word text!',
                             font=('Garamond', 30))
instructions.pack()

# add the score label
scoreLabel = tkinter.Label(root, text='Press enter to start',
                           font=('Garamond', 20))
scoreLabel.pack()

# add a time left label
timeLabel = tkinter.Label(root, text='Time Left: ' + str(timeleft),
                          font=('Garamond', 30))
timeLabel.pack()

# add a label for displaying the colors
label = tkinter.Label(root, font=('Garamond', 55))
label.pack()

# add a text entry box for typing in colors
e = tkinter.Entry(root)

# run the 'startGame' function when Return is pressed
root.bind('<Return>', startGame)
e.pack()

# start the GUI
root.mainloop()