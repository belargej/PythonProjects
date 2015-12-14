#!/usr/bin/python
from Tkinter import *

def Pressed():               # Define a function
    print 'Push it real good'

bkg = Tk()
button = Button(bkg,text='Press',command=Pressed)
button.pack(pady=30,padx=50)
#Pressed()
bkg.mainloop()

