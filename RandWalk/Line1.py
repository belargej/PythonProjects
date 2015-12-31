#!/usr/bin/python

from Tkinter import Tk, Canvas, Frame, BOTH
import random


class Ex(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.x1 = 20
        self.x2 = 20
        self.initUI()
        self.runRandWalk(5)

    def initUI(self):
        self.parent.title("Random Walk Lines 1")
        self.pack(fill=BOTH,expand=1)
        
        self.canvas = Canvas(self)
        self.canvas.create_line(10,10,390,10)
        self.canvas.create_line(10,10,10,390)
        self.canvas.create_line(10,390,390,390)
        self.canvas.create_line(390,10,390,390)
        self.canvas.pack(fill=BOTH,expand=1)

    def RandWalk(self):
        print("hellow")

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
