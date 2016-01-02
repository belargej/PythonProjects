#!/usr/bin/python

from Tkinter import Tk, Canvas, Frame, BOTH, RIGHT,RAISED
from ttk import Frame, Button, Style
import random

ADDVAL = 15
XSTEP = 5

class Ex(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.x_before = 20
        self.x_current = 20
        self.y_before = 200
        self.y_current = 200
        self.initUI()
        self.runRandWalk(70)

    def initUI(self):
        self.parent.title("Random Walk Lines 1")
        self.pack(fill=BOTH,expand=1)
        
        self.style = Style()
        self.style.theme_use("default")
        frame = Frame(self,relief=RAISED,borderwidth=2)
        frame.pack(fill=BOTH,expand=True)

        self.canvas = Canvas(frame)
        self.canvas.create_line(10,200,390,200,dash=(4,2), width=2)
        self.canvas.pack(fill=BOTH,expand=1)
        
        self.newWalkButton = Button(self,text="New Walk",
                                   command=self.newWalk)
        self.closeButton   = Button(self,text="Close",
                                    command=self.closeAll)
        self.closeButton.pack(side=RIGHT,padx=5,pady=5)
        self.newWalkButton.pack(side=RIGHT)


    def newWalk(self):
        print("Walk anew")

    def closeAll(self):
        Frame.quit(self)

    def RandWalk(self):
        r = random.randint(0,1)
        addval = 0;
        if r == 0:
            addval = ADDVAL
        else:
            addval = -ADDVAL

        self.y_current = self.y_before + addval
        self.x_current = self.x_before + XSTEP
        
        if self.y_current < 200:
            if self.y_before == 200:
                self.canvas.create_line(self.x_before,self.y_before,
                                        self.x_current,self.y_current,
                                        fill = "green", width = 5)
            else:
                self.canvas.create_line(self.x_before,self.y_before,
                                        self.x_current,self.y_current,
                                        fill = "green", width = 5)
        else:
            if self.y_before<200:
                self.canvas.create_line(self.x_before,self.y_before,
                                        self.x_current,self.y_current,
                                        fill = "green", width = 5)
            else:
                self.canvas.create_line(self.x_before,self.y_before,
                                        self.x_current,self.y_current,
                                        fill = "red", width = 5)

        self.canvas.pack(fill=BOTH,expand=1)
        self.x_before = self.x_current
        self.y_before = self.y_current

    def runRandWalk(self,steps):
        for x in range(0,steps):
            self.RandWalk()
        

def main():
    root = Tk()
    examp = Ex(root)
    root.geometry("400x400+300+300")
    root.mainloop()

if __name__=='__main__':
    main()
