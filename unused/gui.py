from tkinter import *
from random import *

window = Tk()
window.title('Game Of Life')


def key(event):
    print("pressed", repr(event.char))


def callback(event):
    print("clicked at", event.x, event.y)


def create_grid(window):
    width = 800
    height = 600
    canvas = Canvas(window, background='white', width=width, height=height)

    for line in range(0, width, 100):  # range(start, stop, step)
        canvas.create_line([(line, 0), (line, height)], fill='black', tags='grid_line_w')

    for line in range(0, height, 100):
        canvas.create_line([(0, line), (width, line)], fill='black', tags='grid_line_h')

    canvas.grid(row=0, column=0)
    canvas.bind("<Button-1>", callback)


create_grid(window)

window.mainloop()
