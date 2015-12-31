#!/usr/bin/python

from Tkinter import Tk, Canvas, Frame, BOTH
import random

ADDVAL = 5
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
        
        self.canvas = Canvas(self)
        self.canvas.create_line(10,10,390,10)
        self.canvas.create_line(10,10,10,390)
        self.canvas.create_line(10,390,390,390)
        self.canvas.create_line(390,10,390,390)
        self.canvas.create_line(10,200,390,200,dash=(4,2), width=2)
        self.canvas.pack(fill=BOTH,expand=1)

    def RandWalk(self):
        r = random.randint(0,1)
        addval = 0;
        if r == 0:
            addval = ADDVAL
        else:
            addval = -ADDVAL

        self.y_current = self.y_before + addval
        self.x_current = self.x_before + XSTEP
        if self.y_current > 200:
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
