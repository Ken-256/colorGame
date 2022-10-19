import tkinter
import random

setTime = 0
time = 0
score = 0

colours = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown', 'pink', 'black', 'white']

def setTimer30():
    global setTime
    global time
    setTime = 30
    time = 30
    update()

def setTimer60():
    global setTime
    global time
    setTime = 60
    time = 60
    update()

def setTimer90():
    global setTime
    global time
    setTime = 90
    time = 90
    update()

def update():
    global time
    global score
    timeLabel.config(text="Time left: " + str(time))
    scoreLabel.config(text="Score: " + str(score))

def startGame(event):
    if time == setTime:
        startTimer()
    nextColour()

def nextColour():
    global score
    global time
    if time > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score: " + str(score))

def startTimer():
    global time
    if time > 0:
        time -= 1
        timeLabel.config(text="Time left: " + str(time))
        timeLabel.after(1000, startTimer)

root = tkinter.Tk()
root.title("Colour Game")
root.geometry("575x400")

instructions = tkinter.Label(root, text="Type in the colour of the words, and not the word text!", font = ('Arial 18'))
instructions.pack()

instructions2 = tkinter.Label(root, text="Select a time limit", font = ('Arial 18'))
instructions2.pack()

scoreLabel = tkinter.Label(root, text="Press enter to start", font = ('Arial 18'))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text="Time left: " + str(time), font = ('Arial 18'))
timeLabel.pack()

e4 = tkinter.Button(root, text ="90 sec timer", command = setTimer90, font = ('Arial 18'))
e4.place(x=400, y=300)

e3 = tkinter.Button(root, text ="60 sec timer", command = setTimer60, font = ('Arial 18'))
e3.place(x=200, y=300)

e2 = tkinter.Button(root, text ="30 sec timer", command = setTimer30, font = ('Arial 18'))
e2.place(x=0, y=300)

label = tkinter.Label(root, font = ('Arial 32'), borderwidth=2, relief='solid')
label.pack()

e = tkinter.Entry(root, width = 575, font = ('Arial 24'))
e.pack(side = tkinter.LEFT)

root.bind('<Return>', startGame)
e.focus_set()

root.mainloop()
