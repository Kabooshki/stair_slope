import time
from pymata4 import pymata4
from tkinter import *
import tkinter as tk

num_steps = 32
pins1 = [8,9,10,11]
pins2 = [4,5,6,7]
board = pymata4.Pymata4()

root = Tk()
root.title("Arduino Controller")

def RotateClockwise():
    motorSpeed = slider.get()
    angle = int(angleSet.get())
    board.set_pin_mode_stepper(num_steps, pins1)
    board.stepper_write(motorSpeed * 50, int(angle*5.625))
    board.set_pin_mode_stepper(num_steps, pins2)
    board.stepper_write(motorSpeed * 50, int(angle*(-5.625)))
    
def RotateAntiClockwise():
    motorSpeed = slider.get()
    angle = int(angleSet.get())
    angle *= (-1)
    board.set_pin_mode_stepper(num_steps, pins1)
    board.stepper_write(motorSpeed * 50, int(angle*5.625))
    board.set_pin_mode_stepper(num_steps, pins2)
    board.stepper_write(motorSpeed * 50, int(angle*(-5.625)))

# #canvas
# canvas = Canvas(width = 350, height=255)
# canvas.grid(row = 0, column = 0, columnspan= 2)
# confirm_text = canvas.create_text(175, 128, text = "", fill = "red", font = ("Courier", 20, "bold"))

#slider
speedLabel = Label(root, text = "Speed (in RPM)")
speedLabel.grid(row = 1, column = 0)
slider = Scale(root, from_= 1, to = 9, length = 300, tickinterval = 1, orient = "horizontal")
slider.set(7)
slider.grid(row = 2, column = 0, columnspan= 2)

#angle label
angleLabel = Label(root, text = "Angle (in deg)")
angleLabel.grid(row = 3, column = 0)
angleSet = Entry(root, width = 10)
#angleSet.insert(0, 90)
angleSet.grid(row = 3, column = 1)

#text box for no angle input
textAngle = Label(root, text = "", fg = "red")
textAngle.grid(row = 4, column = 1)

#buttons
btn_forward = tk.Button(root, text = "Clockwise", command = RotateClockwise)
btn_forward.grid(row = 5, column = 0)

btn_backward = tk.Button(root, text = "Anticlockwise", command = RotateAntiClockwise)
btn_backward.grid(row = 5, column = 1)

#size of window
root.geometry("1000x2000")
root.mainloop()