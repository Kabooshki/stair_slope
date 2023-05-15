import time
from pymata4 import pymata4
import tkinter as tk
import step_controler_2, step_controler_3

# num_steps = 32
# pins1 = [2, 4, 3, 5]
# pins2 = [6, 8, 7, 9]
# #pins3 = [10, 12, 11, 13]
# board = pymata4.Pymata4(com_port="COM6")

root = tk.Tk()
root.title("Smart Slopes Ver. 1.0")
root.geometry("450x500")
root.resizable(None, None)
root.configure(bg='#E1DCDC')

# create a canvas
canvas = tk.Canvas(root, width=220, height=270, bg='#E1DCDC', highlightbackground='#E1DCDC')
canvas.pack()

# create a circular button on canvas
button = canvas.create_oval(20, 20, 210, 210, fill='red', width=3)

# create a text label on button
button_text = canvas.create_text(112, 113, text="Deploy", fill='black',
                                 font=('Helvetica', '20', 'underline'))

# create "Active/Inactive" label
active_label = tk.Label(root, text="\u0332".join("Status:") + " Inactive", font=('Helvetica', '12'), bg='#E1DCDC')
active_label.pack(padx=10, pady=10)
#active_label.pack(side=tk.LEFT, padx=10, pady=10)

# define callback function for button click event
def on_button_click(event):
    current_color = canvas.itemcget(button, 'fill')
    if current_color == 'red':
        canvas.itemconfigure(button, fill='#F5C726')
        canvas.itemconfigure(button_text, text="Deploying...")
        canvas.itemconfigure(button, state='disabled')
        root.after(200, lambda: on_yellow_timeout_deploying())
    elif current_color == '#36F526':
        canvas.itemconfigure(button, fill='#F5C726')
        canvas.itemconfigure(button_text, text="Please wait...")
        canvas.itemconfigure(button, state='disabled')
        root.after(200, lambda: on_yellow_timeout_unfold())
    # do nothing if button color is yellow and it's disabled

def on_yellow_timeout_deploying():
    step_controler_3.main()
    canvas.itemconfigure(button, fill='#36F526')
    canvas.itemconfigure(button_text, text="GO!")
    canvas.itemconfigure(button, state='normal')
    active_label.config(text="\u0332".join("Status:") + " Active")  # set "Active" label when button is green

def on_yellow_timeout_unfold():
    step_controler_2.main()
    canvas.itemconfigure(button, fill='red')
    canvas.itemconfigure(button_text, text="Deploy")
    canvas.itemconfigure(button, state='normal')
    active_label.config(text="\u0332".join("Status:") + " Inactive")  # set "Inactive" label when button is red
    
# bind button click event to callback function
canvas.tag_bind(button, '<Button-1>', on_button_click)

root.mainloop()