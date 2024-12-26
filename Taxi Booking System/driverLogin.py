from tkinter import * #this is the process to Import all tkinter (*) =aLL
from tkinter import ttk  # this is the process to import tkinter ttk
from PIL import Image, ImageTk  # this is the process to import PIL module for image handling
from tkinter import messagebox #this is to import tkinter messagebox
import re   #this is to import re for email validation
import mysql.connector as MyConn  #this is to import mysql.connector for database
import Global #this is to import globle varible for id
from db import Db as Database #this is importing Database from db

class driver:
    def __init__(self, root):
        self.root = root


        ################################################## window_icon #################################################
        window_icon = PhotoImage(file="Images/SayuGoIcon.png")  # this is the Icon of my logo
        self.root.wm_iconphoto(True, window_icon)



        ################################################## background_image #################################################
        self.background_image = Image.open("Images/driverLogin.jpg")  #  this is the Load background
        self.background_image = self.background_image.resize((1560, 800))  #  this is the Resizing background
        self.bg = ImageTk.PhotoImage(self.background_image)



        ################################################## Label_of_background_image #################################################
        label_of_background_image = Label(self.root, image=self.bg)  #  this is the Display background
        label_of_background_image.place(x=0, y=0, relwidth=1, relheight=1)



        ################################################## frame #################################################
        my_frame = Frame(self.root, bg="#f0f0f0")  #  this is for the main frame
        my_frame.place(x=70, y=120, width=400, height=580)



        ################################################## Icon_image #################################################
        icon_image = Image.open("Images/AdminIconLogo.png")  #  this is the load icon image
        icon_image = icon_image.resize((100, 100))  #  this is the resize icon image
        self.photoimage1 = ImageTk.PhotoImage(icon_image)



        ################################################## label_inside_frame #################################################
        label_inside_frame = Label(my_frame, image=self.photoimage1, bg="#f0f0f0", borderwidth=0)  #  this is the icon inside frame
        label_inside_frame.place(x=150, y=20, width=100, height=100)



        ################################################## label #################################################
        get_started = Label(my_frame, text="Start your journey", font=("Times New Roman", 12), fg="black", bg="#f0f0f0")  
        get_started.place(x=120, y=125, width=160, height=30)



        ################################################## Sign_up_label #################################################
        sign_up = Label(my_frame, text="Sign In to SayGo", font=("Times New Roman", 14, "bold"), fg="black", bg="#f0f0f0") 
        sign_up.place(x=120, y=160, width=160, height=30)



        ################################################## Message_and_Sign-Up #################################################
        msg = Label(my_frame, text="Don't have an account yet?", font=("Times New Roman", 10), fg="black", bg="#f0f0f0")  
        msg.place(x=100, y=230)

        sign_up_button = Button(my_frame, text="Sign Up", command=self.driver_register_window, font=("Times New Roman", 10, "bold", "underline"), fg="blue", cursor="hand2", borderwidth=0, bg="#f0f0f0", activeforeground="black")  
        sign_up_button.place(x=255, y=230)



        ################################################## Email_label #################################################
        email = Label(my_frame, text="Email: ", font=("Times New Roman", 14, "bold"), fg="black", bg="#f0f0f0")  
        email.place(x=120, y=280, width=160, height=30)
        ################################################## Email_entry #################################################
        self.email = ttk.Entry(my_frame, font=("Times New Roman", 14))  
        self.email.place(x=120, y=310, width=160, height=30)

        ################################################## Email_icon #################################################
        email_icon = Image.open("Images/customerUsernameIcon.png") 
        email_icon = email_icon.resize((25, 25))
        self.photoimage2 = ImageTk.PhotoImage(email_icon)

        email_label = Label(my_frame, image=self.photoimage2, bg="#f0f0f0", borderwidth=0)  #  this is the icon 
        email_label.place(x=85, y=310, width=25, height=25)



        ################################################## Password_label #################################################
        password = Label(my_frame, text="Password: ", font=("Times New Roman", 14, "bold"), fg="black", bg="#f0f0f0")  # Password label
        password.place(x=120, y=350, width=160, height=30)

        ################################################## Password_entry #################################################
        self.password = ttk.Entry(my_frame, font=("Times New Roman", 14), show="*")  # Password input
        self.password.place(x=120, y=380, width=160, height=30)

        ################################################## Password_icon #################################################
        password_icon = Image.open("Images/customerPasswordIcon.png")  # Password icon
        password_icon = password_icon.resize((25, 25))
        self.photoimage3 = ImageTk.PhotoImage(password_icon)

        password_label = Label(my_frame, image=self.photoimage3, bg="#f0f0f0", borderwidth=0)  # Icon for password input
        password_label.place(x=85, y=380, width=25, height=25)



        ################################################## Login_button #################################################
        login_button = Button(my_frame, text="Login", font=("Times New Roman", 14, "bold"), bd=3, relief="ridge", fg="white", bg="blue", activebackground="blue", activeforeground="blue", command=self.driverlogin)  # Login button
        login_button.place(x=120, y=480, width=160, height=40)


        ################################################## Forgot_password_button #################################################
        forgot_password_button = Button(my_frame, text="Forgot Password", font=("Times New Roman", 10, "bold"), borderwidth=0, fg="black", bg="#f0f0f0", activeforeground="black")  # Forgot password link
        forgot_password_button.place(x=120, y=440, width=160, height=30)

        ############################################ Back Button ###########################################
        back_Button = Button(my_frame, text="Back", borderwidth=0, cursor="hand2", font=("Times New Roman", 10, "bold"), command=self.backButton, bd=3, relief="ridge", fg="white", bg="red", activebackground="red", activeforeground="white",)
        back_Button.place(x=120, y=530, width=160, height=30)


    def backButton(self): # this is to go back to first page
        self.clearScreen()
        from firstPage import first 
        first(self.root)


    ################################################## driver_register_window ##################################################
    def driver_register_window(self):
        self.clearScreen() # this is the process to clear screen
        from driverReg import driverReg  # # this is the process to Import driverReg  
        driverReg(self.root)  # this is the process to open registration window

    def clearScreen(self):
        for widget in self.root.winfo_children():  # this is the process to loop through all widgets
            widget.destroy()  # this is the process to remove each widget 


    ################################################## driverlogin ##################################################
    def driverlogin(self):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # Email format regex
        email = self.email.get()  
        password = self.password.get()  

        if email == "" or password == "":  # this is the process to check if fields are empty
            messagebox.showerror("Error", "All fields are required")
        elif not re.match(email_pattern, email):  # this is the process to validate email format
            messagebox.showerror("Invalid Email", "Please enter a valid email address (e.g., example@example.com)")
        else:
            try:
                # this is the process to Connect to database
                connection = MyConn.connect(
                    host="localhost",
                    user="root",
                    password="9828807288",
                    database="tbs"
                )
                my_cursor = connection.cursor()  

                #this is the process the SQL query
                my_cursor.execute("SELECT * FROM users WHERE email = %s and password = %s", (email, password))
                row = my_cursor.fetchone()  # this is the process to Fetch one
                
                if row is None: 
                    messagebox.showerror("Error", "Invalid email or password")
                else:
                    messagebox.showinfo("Success", "Login successful!")  # get success message
                    Global.id = row[0]  # this is the to store user ID globally
                    print(Global.id)  # Print
                    self.new_window = Toplevel(self.root)  # this is the process to open new window
                    self.driverDashboard()  # this is the process to redirect to dashboard

                connection.close()  # this is the process to close database connection
            except Exception as e:  # this is the process to handle database errors
                messagebox.showerror("Error", f"Database Error: {e}")

    def driverDashboard(self):
        self.clearScreen() # this is the process to Clear screen
        from driverDash import driverDashboard  #  this is the process to Import driverDash (dashboard)
        driverDashboard(self.root)  # this is the process to open dashboard window


################################################ Finish ##################################################

