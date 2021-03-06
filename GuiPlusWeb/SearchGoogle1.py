#!/usr/bin/python
from Tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GUI(Frame):

    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initGUI()

    def initGUI(self):
        self.parent.title("Search Chrome")
        self.pack(fill=BOTH,expand=1)

        self.btn = Button(self,text="Open Chrome",
                          command=self.openChrome)
        #self.btn.place(x=25,y=200)
        self.btn.pack(side=RIGHT,padx=10,pady=10)
        
        self.clsbtn = Button(self,text="Close",
                             command=self.closeAll)
        #self.clsbtn.place(x=150,y=200)
        self.clsbtn.pack(side=RIGHT)

        self.entry = Entry(self,width=10)
        self.entry.place(x=10,y=10)
        
        self.srchbtn = Button(self,text="Search",
                              command=self.searchChrome)
        self.srchbtn.place(x=75, y=10)
        
    def openChrome(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.google.com")

    def closeAll(self):
        try:
            self.driver
        except:
            print("Later Dude")
            Frame.quit(self)
        else:
            print("bye")
            self.driver.close()
            Frame.quit(self)
            

    def searchChrome(self):
        try:
            self.driver
        except:
            print("Driver not made yet!")
            print(" Push the button to open Google!!!")
        else:
            search_bar=self.driver.find_element_by_name("q")
            self.query=self.entry.get()
            search_bar.send_keys(Keys.CONTROL+"a")
            search_bar.send_keys(Keys.DELETE)
            search_bar.send_keys(self.query+Keys.RETURN)
            

def main():
    root = Tk()
    Window = GUI(root)
    root.geometry("300x300+150+150")
    root.mainloop()

if __name__=='__main__':
    main()
