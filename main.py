import sys
from tkinter import *
import time

def tick():
    time_string=time.strftime("%H:%M:%S"+'\n'+"%j.%m.%Y")
    clock.config(text=time_string)
    clock.after(200, tick)

root=Tk()
clock=Label(root, font=("times",200,"bold"),bg="white")
clock.grid(row=0, column=1)
tick()
root.mainloop()