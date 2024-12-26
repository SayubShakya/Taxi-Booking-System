from tkinter import *  #this is the process to Import all tkinter (*) =aLL

class Main:  #this is Main class
    def __init__(self, root):  # this is the constructor
        self.root = root  # this is the process to Store root 
        self.root.title("Taxi Booking System")  #this is the title
        self.root.geometry("1560x800+0+0")  #this is the process to fix size and position
        self.mainPage()  # this is the process of Calling mainPage


    def mainPage(self):  #this is the process to display main page
        self.clearScreen()  # this is the process to Clear screen
        from firstPage import first  # this is the process to Import firstPage 
        first(self.root)  # This is a process to call



    def clearScreen(self):  # this is the process to clear root
        for widget in self.root.winfo_children():   #for loop
            widget.destroy()  # this is the process to destroy widget

          

if __name__=="__main__":  #
    root = Tk()  # this is the process to open main window
    Main = Main(root)  # this is the main class
    root.mainloop()  # this is the process to Start Tkinter loop


################################################ Finish ##################################################

