#!/usr/bin/python
from Tkinter import *

def Call():
    lab = Label(root,text='You Pressed\nthe button.')
    lab.pack()
    button['bg']='blue'
    button['fg']='white'

root = Tk()
root.geometry('100x100+350+70')
button = Button(root, text='Press Me', command = Call)
button.pack()
root.mainloop()
