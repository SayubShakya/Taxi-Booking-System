from tkinter import * #this is the process to Import all tkinter (*) =aLL
from tkinter import ttk  # this is the process to import tkinter ttk
from tkinter import messagebox #this is to import tkinter messagebox
from PIL import Image, ImageTk  # this is the process to import PIL module for image handling
import re #this is to import re for email validation
import mysql.connector as MyConn #this is to import mysql.connector for database
from db import Db as Database #this is importing Database from db

class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1560x800+0+0")  # this is the fix the size to full screen


        ################################################### Window Icon ##################################################
        window_icon = PhotoImage(file="Images/SayuGoIcon.png")  #this is the window icon
        self.root.wm_iconphoto(True, window_icon)  # this is the window icon


        ################################################### Variables ##################################################
        self.var_first_name = StringVar()
        self.var_last_name = StringVar()
        self.var_phone_no = StringVar()
        self.var_address = StringVar()
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_confirm_password = StringVar()
        self.var_gender = StringVar()
        self.var_agree_terms = IntVar() 


        ################################################### Background Image ##################################################
        self.background_image = Image.open("Images/BackgroundRegester.jpg")
        self.background_image = self.background_image.resize((1560, 800))
        self.background_image = ImageTk.PhotoImage(self.background_image)
        label_of_background_image = Label(self.root, image=self.background_image)
        label_of_background_image.place(x=0, y=0, relwidth=1, relheight=1)


        ################################################### Background Image ##################################################
        self.background_image1 = Image.open("Images/customerBoardPhoto.jpg")
        self.background_image1 = self.background_image1.resize((470, 600))
        self.background_image1 = ImageTk.PhotoImage(self.background_image1)
        label_of_background_image1 = Label(self.root, image=self.background_image1)
        label_of_background_image1.place(x=65, y=100, width=470, height=600)



        ################################################### Frame ##################################################
        my_frame = Frame(self.root, bg="#f0f0f0")
        my_frame.place(x=520, y=100, width=950, height=600)



        ################################################### Register Label ##################################################
        label_register = Label(my_frame, text="Sign-Up", font=("Times New Roman", 24, "bold"), fg="black", bg="#f0f0f0")
        label_register.place(x=350, y=50, width=250, height=40)


        # Input Fields and Labels
        self.create_input_fields(my_frame)  # this is to Call



        ################################################### Check Box ##################################################
        self.check_box = Checkbutton(my_frame, text="I Agree The Terms & Conditions:", variable=self.var_agree_terms,font=("Times New Roman", 12), onvalue=1, offvalue=0, fg="black", bg="#f0f0f0")
        self.check_box.place(x=50, y=420)



        ################################################### Register Button ##################################################
        icon_image_register = Image.open("Images/RegisterButton.png")
        icon_image_register = icon_image_register.resize((100, 100))
        self.photoimage_register = ImageTk.PhotoImage(icon_image_register)
        b_register = Button(my_frame, image=self.photoimage_register, borderwidth=0, cursor="hand2",font=("Times New Roman", 12, "bold"), command=self.register)
        b_register.place(x=200, y=439, width=300)



        ################################################### Login Button ##################################################
        icon_image_login = Image.open("Images/LoginButton.png")
        icon_image_login = icon_image_login.resize((100, 100))
        self.photoimage_login = ImageTk.PhotoImage(icon_image_login)
        b_login = Button(my_frame, image=self.photoimage_login, borderwidth=0, cursor="hand2",font=("Times New Roman", 12, "bold"), command=self.Login)
        b_login.place(x=400, y=446, width=400)



    ################################################### Login ###################################################
    def Login(self):
        self.clearScreen()  # this is the process to Clear screen
        from customerLogin import Login_Window  # this is the process to import customerLogin class
        Login_Window(self.root)  # this is the process to login window

    def create_input_fields(self, frame):
        """Creates input fields with labels.""" 
        labels = ["First Name", "Last Name", "Phone Number", "Address", "Email", "Password", "Confirm Password"]
        variables = [self.var_first_name, self.var_last_name, self.var_phone_no, self.var_address, self.var_email,self.var_password, self.var_confirm_password]
        y_positions = [150, 200, 250, 300, 150, 200, 250]
        x_positions = [10, 10, 10, 10, 465, 475, 455]

        for i in range(len(labels)):
            label = Label(frame, text=f"{labels[i]}:", font=("Times New Roman", 14, "bold"), fg="black", bg="#f0f0f0")
            label.place(x=x_positions[i], y=y_positions[i], width=200, height=35)  # Position label
            entry = ttk.Entry(frame, textvariable=variables[i], font=("Times New Roman", 14),show="*" if "Password" in labels[i] else "")  # Entry field with password masking if needed
            entry.place(x=180 if i < 4 else 640, y=y_positions[i], width=270 if i < 4 else 300, height=35)  # Position entry



        ##################################### Gender Label and Radio Buttons ############################################
        gender_label = Label(frame, text="Gender:", font=("Times New Roman", 14, "bold"), fg="black", bg="#f0f0f0")
        gender_label.place(x=10, y=360, width=200, height=35)  # Position

        self.var_gender.set("Male")  # Default gender 
        genders = [("Male", 180), ("Female", 290), ("Other", 400), ("Prefer not to say", 510)]
        for gender, x_pos in genders:
            Radiobutton(frame, text=gender, value=gender, variable=self.var_gender, font=("Times New Roman", 14),fg="black", bg="#f0f0f0").place(x=x_pos, y=360, width=100 if "Prefer" not in gender else 200,height=35)  # gender radio buttons




    ################################################### Register ################################################################
    def register(self):
        # this is the process to Check if all fields are filled
        if not all([self.var_first_name.get().strip(), self.var_last_name.get().strip(), self.var_phone_no.get().strip(),
                    self.var_address.get().strip(), self.var_email.get().strip(), self.var_password.get().strip(),
                    self.var_confirm_password.get().strip(), self.var_gender.get().strip()]):
            messagebox.showerror("Error", "All fields are required")  # this is to Show error if any field is empty
            return

        if self.var_password.get() != self.var_confirm_password.get():  #this is to Check if passwords match
            messagebox.showerror("Error", "Passwords do not match")  # this is to Show error if passwords don't match
            return

        if not self.var_agree_terms.get():  # this is the process to if terms are agreed
            messagebox.showerror("Error", "Please agree to the terms and conditions")  # this is the process to show error if not agreed
            return
        
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', self.var_email.get()):
            messagebox.showerror("Error", "Invalid email format")  # this is the process to show error if email is invalid
            return

        if not re.match(r'^\d{10}$', self.var_phone_no.get()):
            messagebox.showerror("Error", "Invalid phone number format. It should be 10 digits")  # this is to show error if phone is invalid
            return

        try:
            connection = MyConn.connect(host="localhost", user="root", password="9828807288", database="tbs")
            cursor = connection.cursor()

            # this is the process to Check if user already exists
            cursor.execute("SELECT * FROM users WHERE email = %s", (self.var_email.get(),))
            if cursor.fetchone():  # this is to show error
                messagebox.showerror("Error", "User already exists, Please try another email")
                return

            cursor.execute(
                "INSERT INTO users (email, password, role_id) VALUES (%s, %s, %s)",
                (self.var_email.get(), self.var_password.get(), 1)
            )
            user_id = cursor.lastrowid  # this is to Get the last inserted user ID

            cursor.execute("""
                INSERT INTO customer_profiles (first_name, last_name, address, phone_number, gender, user_id) VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                self.var_first_name.get(), self.var_last_name.get(), self.var_address.get(),
                self.var_phone_no.get(), self.var_gender.get(), user_id
            ))
            connection.commit()  # this is to commit changes 

            messagebox.showinfo("Success", "Registration successful!")  # get success message
            self.clearScreen()  # this is to clear the screen 
            from customerLogin import Login_Window
            Login_Window(self.root)  # Show login window after registration

        except MyConn.Error as e:  # this is the process to handle database connection errors
            messagebox.showerror("Database Error", f"Error connecting to database: {str(e)}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()  # this is to Close cursor
                connection.close()  # this is to Close database connection

    def clear_fields(self):
        """Clears all input fields after successful registration.""" 
        self.var_first_name.set("")  
        self.var_last_name.set("") 
        self.var_phone_no.set("") 
        self.var_address.set("")  
        self.var_email.set("")  
        self.var_password.set("")  
        self.var_confirm_password.set("")  
        self.var_gender.set("Male")  
        self.var_agree_terms.set(0)  

    def clearScreen(self):
        for widget in self.root.winfo_children():  
            widget.destroy()  #this is to destroy each widget 


    ################################################ Finish ##################################################