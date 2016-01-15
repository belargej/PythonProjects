#!/usr/bin/python

from Tkinter import Tk, Canvas, Frame, BOTH, RIGHT,RAISED
from ttk import Frame, Button, Style,Entry
import random

ADDVAL = 15
ADDVAL_X = 15
XSTEP = 5
STEPS = 1000

class Ex(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.x_before = 400
        self.x_current = 400
        self.y_before = 400
        self.y_current = 400
        self.FirstRun = True
        self.AddVal = ADDVAL
        self.AddVal_X = ADDVAL_X
        self.initUI()
        self.runRandWalk(STEPS)
        self.FirstRun = False
        self.Steps = STEPS
        self.newSteps = STEPS
        self.XStep = XSTEP

    def initUI(self):
        self.parent.title("Random Walk Lines 1")
        self.pack(fill=BOTH,expand=1)
        
        self.style = Style()
        self.style.theme_use("default")
        frame = Frame(self,relief=RAISED,borderwidth=2)
        frame.pack(fill=BOTH,expand=True)

        self.canvas = Canvas(frame)
        self.canvas.create_line(10,400,790,400,dash=(4,2), width=2)
        self.canvas.create_line(400,10,400,790,dash=(4,2), width=2)
        self.canvas.pack(fill=BOTH,expand=1)
        
        self.newWalkButton = Button(self,text="New Walk",
                                   command=self.newWalk)
        self.closeButton   = Button(self,text="Close",
                                    command=self.closeAll)
        self.stepsButton   = Button(self,text="Send Steps",
                                    command=self.sendSteps)
        self.xSizeButton   = Button(self,text="Set X Step",
                                    command=self.xSize)
        self.ySizeButton   = Button(self,text="Set Y Step",
                                    command=self.ySize)
        self.xSizeBox      = Entry(self,width=10)
        self.ySizeBox      = Entry(self,width=10)
        self.stepsBox      = Entry(self,width=10)
        

        # pack the buttons here
        self.closeButton.pack(side=RIGHT,padx=5,pady=5)
        self.newWalkButton.pack(side=RIGHT)
        self.stepsButton.pack(side=RIGHT)
        self.stepsBox.pack(side=RIGHT)
        self.xSizeButton.pack(side=RIGHT)
        self.xSizeBox.pack(side=RIGHT)
        self.ySizeButton.pack(side=RIGHT)
        self.ySizeBox.pack(side=RIGHT)
        
    def ySize(self):
        self.AddVal = int(self.ySizeBox.get())

    def xSize(self):
        self.AddVal_X = int(self.xSizeBox.get())

    def sendSteps(self):
        self.newSteps = int(self.stepsBox.get())
        
    def newWalk(self):
        for x in range(0,self.Steps):
            getTag = "step"+str(x)
            self.canvas.coords(getTag,(0,0,0,0))

        self.Steps = self.newSteps
        self.x_current = 400
        self.x_before  = 400
        self.y_current = 400
        self.y_before  = 400
        self.runRandWalk(self.Steps)
        
    def closeAll(self):
        Frame.quit(self)

    def RandWalk(self,whichStep):
        r = random.randint(0,1)
        rx = random.randint(0,1)
        addval = 0;
        addval_x = 0;
        toTag = "step"+str(whichStep)
        if r == 0:
            addval = (self.AddVal)
        else:
            addval = -(self.AddVal)

        if rx==0:
            addval_x = (self.AddVal_X)
        else:
            addval_x = -(self.AddVal_X)
            
        self.y_current = self.y_before + addval
        self.x_current = self.x_before + addval_x
                
        if self.y_current < 200:
            if self.y_before == 200:
                if self.FirstRun == True:
                    self.canvas.create_line(self.x_before,self.y_before,
                                            self.x_current,self.y_current,
                                            fill = "green", width = 5,
                                            tags=toTag)
                else:
                    self.canvas.coords(toTag,(self.x_before,self.y_before,
                                              self.x_current,self.y_current),)
                    self.canvas.itemconfig(toTag,fill="green")
            else:
                if self.FirstRun == True:
                    self.canvas.create_line(self.x_before,self.y_before,
                                            self.x_current,self.y_current,
                                            fill = "green", width = 5,
                                            tags=toTag)
                else:                    
                    self.canvas.coords(toTag,(self.x_before,self.y_before,
                                             self.x_current,self.y_current))
                    self.canvas.itemconfig(toTag,fill="green")
        else:
            if self.y_before<200:
                if self.FirstRun==True:
                    self.canvas.create_line(self.x_before,self.y_before,
                                            self.x_current,self.y_current,
                                            fill = "green", width = 5,
                                            tags=toTag)
                else:
                    self.canvas.coords(toTag,(self.x_before,self.y_before,
                                             self.x_current,self.y_current))
                    self.canvas.itemconfig(toTag,fill="green")
            else:
                if self.FirstRun==True:
                    self.canvas.create_line(self.x_before,self.y_before,
                                            self.x_current,self.y_current,
                                            fill = "red", width = 5,
                                            tags=toTag)
                else:
                    self.canvas.coords(toTag,(self.x_before,self.y_before,
                                             self.x_current,self.y_current))
                    self.canvas.itemconfig(toTag,fill="red")

                
        self.canvas.pack(fill=BOTH,expand=1)
        self.x_before = self.x_current
        self.y_before = self.y_current
                    

    def runRandWalk(self,steps):
        for x in range(0,steps):
            self.RandWalk(x)
        

def main():
    root = Tk()
    examp = Ex(root)
    root.geometry("800x800+300+300")
    root.mainloop()

if __name__=='__main__':
    main()
