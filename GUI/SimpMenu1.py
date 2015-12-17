#!/usr/bin/python
from Tkinter import *

class Men1(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initGUI()

    def initGUI(self):
        self.parent.title("Simple Menu 1")
        
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit",command=self.onExit)
        menubar.add_cascade(label="File",menu=fileMenu)

        printMenu = Menu(menubar)
        printMenu.add_command(label="Open",command=self.onOpen)
        printMenu.add_command(label="Print",command=self.onPrint)
        menubar.add_cascade(label="ToScreen",menu=printMenu)


    def onExit(self):
        self.quit()
    
    def onOpen(self):
        print("Open a thing!!")
        
    def onPrint(self):
        print("This message!!")

def main():
    root = Tk()
    root.geometry("300x300+150+150")
    ex = Men1(root)
    root.mainloop()

if __name__ =='__main__':
    main()
    

