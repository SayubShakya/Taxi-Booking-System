from tkinter import *   #this is the process to Import all tkinter (*) =aLL
from PIL import Image, ImageTk  # this is the process to import PIL module for image handling

class first:  #this is the first class
    def __init__(self, root):  # this is the Constructor
        self.root = root  # this is the process to store root 

        
        ################################################ Setting the window icon ############################################
        window_icon = PhotoImage(file="Images/SayuGoIcon.png")
        self.root.wm_iconphoto(True, window_icon)


        # ################################################# background image ################################################
        self.background_image = Image.open("Images/firstPage.jpg")
        self.background_image = self.background_image.resize((1560, 800))  # Resizing image
        self.background_image = ImageTk.PhotoImage(self.background_image)  # this is the process to convert Tkinter compatible format
        label_of_background_image = Label(self.root, image=self.background_image)  # this is the label for the background
        label_of_background_image.place(x=0, y=0, relwidth=1, relheight=1)  # this is the process to placing the background image


        ################################################## Customer Button ##################################################
        customer_button = Button(self.root, command=self.open_customer, text="Login as a Customer", font=("Times New Roman", 20, "bold"), bd=0, relief="flat", fg="black", bg="#84DCDB", activebackground="#84DCDB", highlightthickness=0)
        customer_button.place(x=200, y=20, width=300, height=50)  # Placing 


        ################################################## Driver Button ###################################################
        driver_button = Button(self.root, command=self.open_driver, text="Login as a Driver", font=("Times New Roman", 20, "bold"), bd=0, relief="flat", fg="black", bg="#84DCDB", activebackground="#84DCDB", highlightthickness=0)
        driver_button.place(x=650, y=20, width=300, height=50)  # Placing 




        ################################################## Admin Button ####################################################
        admin_button = Button(self.root, command=self.open_admin, text="Login as an Admin", font=("Times New Roman", 20, "bold"), bd=0, relief="flat", fg="black", bg="#84DCDB", activebackground="#84DCDB", highlightthickness=0)
        admin_button.place(x=1200, y=20, width=300, height=50)  # Placing 


    ###################################################### Methods #########################################################
    def open_customer(self):  # this is the method to open customer login page
        self.clearScreen()  # this is the process to Clearn screen
        from customerLogin import Login_Window  # this is the process to import customerLogin
        Login_Window(self.root)  # this is the process to call



    def open_admin(self):  # this is the method to open the admin login page
        self.clearScreen()  # this is the process to Clearn screen
        from adminLogin import adminWIn  # this is the process to import adminLogin
        adminWIn(self.root)  # this is the process to call



    def open_driver(self):  # this is the method to open the driver login page
        self.clearScreen()  # this is the process to Clearn screen
        from driverLogin import driver  # this is the process to import driverLogin
        driver(self.root)  #this is the process to call

        

    def clearScreen(self):  # this is the method to clear all widgets from the screen
        for widget in self.root.winfo_children():  # this is to Loop through all widgets
            widget.destroy()  # this is the process to Destroy widget

    ################################################ Finish ##################################################

