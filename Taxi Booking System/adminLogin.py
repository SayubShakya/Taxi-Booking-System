from tkinter import *  #this is importing all tkinter (*) =aLL
from tkinter import ttk   #this is importing widgets_like_combobox
from PIL import Image, ImageTk #this is importing images
from tkinter import messagebox  #this is importing show pop-up messages
import re #this is the importing check_patterns
import mysql.connector as MyConn  #this is importing MySQL_connector_to_interact_with_database
from adminDashboard import helloAdmin 
import Global  #this is to import globle varible for id
from db import Db as Database #this is importing Database from db

class adminWIn:
    def __init__(self, root):
        self.root = root
        
        window_icon = PhotoImage(file ="Images/SayuGoIcon.png")
        self.root.wm_iconphoto(True, window_icon)

        self.background_image = Image.open("Images/AdminLogin.jpg")
        self.background_image = self.background_image.resize((1560, 800))
        self.bg = ImageTk.PhotoImage(self.background_image)



        ############################################ Label_of_background_image ###########################################
        label_of_background_image = Label(self.root, image=self.bg)
        label_of_background_image.place(x=0, y=0, relwidth=1, relheight=1)



        ############################################ frame ###########################################
        my_frame = Frame(self.root, bg="#f0f0f0")  # Off-white_color
        my_frame.place(x=70, y=120, width=400, height=580)



        ############################################ Icon_image ###########################################
        icon_image = Image.open("Images/AdminIconLogo.png")
        icon_image = icon_image.resize((100, 100))
        self.photoimage1 = ImageTk.PhotoImage(icon_image)



        ############################################ label_inside_frame ###########################################
        label_inside_frame = Label(my_frame, image=self.photoimage1, bg="#f0f0f0", borderwidth=0)
        label_inside_frame.place(x=150, y=20, width=100, height=100)



        ############################################ Labels and Entries ###########################################
        get_started = Label(my_frame, text="Start your journey", font=("Times New Roman", 12), fg="black", bg="#f0f0f0")
        get_started.place(x=120, y=125, width=160, height=30)

        sign_up = Label(my_frame, text="Sign In to SayGo", font=("Times New Roman", 14, "bold"), fg="black", bg="#f0f0f0")
        sign_up.place(x=120, y=160, width=160, height=30)

        msg = Label(my_frame, text="Welcome, Admin", font=("Times New Roman", 20), fg="black", bg="#f0f0f0")
        msg.place(x=100, y=225)



        ############################################ Email ###########################################
        email_label = Label(my_frame, text="Email: ", font=("Times New Roman", 14, "bold"), fg="black", bg="#f0f0f0")
        email_label.place(x=120, y=280, width=160, height=30)

        self.email = ttk.Entry(my_frame, font=("Times New Roman", 14))
        self.email.place(x=120, y=310, width=160, height=30)



        ############################################ Password ###########################################
        password_label = Label(my_frame, text="Password: ", font=("Times New Roman", 14, "bold"), fg="black", bg="#f0f0f0")
        password_label.place(x=120, y=350, width=160, height=30)



        self.password = ttk.Entry(my_frame, font=("Times New Roman", 14), show="*")
        self.password.place(x=120, y=380, width=160, height=30)



        ############################################ Login_Button ###########################################
        login_button = Button(my_frame, text="Login", font=("Times New Roman", 14, "bold"), bd=3, relief="ridge", fg="white", bg="blue", activebackground="blue", activeforeground="white", command=self.admin_login)
        login_button.place(x=120, y=480, width=160, height=40)



        ############################################ Back Button ###########################################
        back_Button = Button(my_frame, text="Back", borderwidth=0, cursor="hand2", font=("Times New Roman", 10, "bold"), command=self.backButton, bd=3, relief="ridge", fg="white", bg="red", activebackground="red", activeforeground="white",)
        back_Button.place(x=120, y=530, width=160, height=30)


    def backButton(self):
        self.clearScreen()
        from firstPage import first 
        first(self.root)  
 

    ########################################### clearScreen ###########################################
    def clearScreen(self):
        # Loop
        for widget in self.root.winfo_children():
            widget.destroy()


    ########################################### admin_login ###########################################
    def admin_login(self):
        # this is for email regex pattern for validation
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        email = self.email.get()  # this is to get email input from user
        password = self.password.get()  # this is to get password input from user

        # this is to Check if email or password is empty
        if email == "" or password == "":
            messagebox.showerror("Error", "All fields are required")

        # this is to validate email format using regex
        elif not re.match(email_pattern, email):
            messagebox.showerror("Invalid Email", "Please enter a valid email address (e.g., example@example.com)")
        else:
            try:
                #this is to connection to database
                connection = MyConn.connect(
                    host="localhost",
                    user="root",
                    password="9828807288",  
                    database="tbs"
                )
                my_cursor = connection.cursor()
                # this is to Check if the email and password match a user in the database

                my_cursor.execute("SELECT * FROM users WHERE email = %s and password = %s", (email, password))
                row = my_cursor.fetchone()  # Fetch result
                
                # If no matching row is found, show error
                if row is None:
                    messagebox.showerror("Error", "Invalid email or password")
                else:
                    messagebox.showinfo("Success", "Login successful!")  # get success message
                    # this is to Store user ID in a global variable
                    Global.id = row[0]
                    print(Global.id) 
                    
                    #this is to new window for the admin dashboard
                    self.new_window = Toplevel(self.root)
                    self.adminDashboard()

                #this is to Close connection
                connection.close()
            except Exception as e:
                # this is to Handle any database connection errors
                messagebox.showerror("Error", f"Database Error: {e}")

    def adminDashboard(self):
        # this is to Clears the current screen 
        self.clearScreen()
        from adminDashboard import helloAdmin
        helloAdmin(self.root)

    ################################################ Finish ##################################################