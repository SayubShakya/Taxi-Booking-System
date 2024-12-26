from tkinter import * #this is the process to Import all tkinter (*) =aLL
from PIL import Image, ImageTk  # this is the process to import PIL module for image handling
from tkinter import ttk  # this is the process to import tkinter ttk
from tkinter import messagebox #this is to import tkinter messagebox
import re #this is to import re for email validation
import mysql.connector as MyConn #this is to import mysql.connector for database
from db import Db as Database #this is importing Database from db

class driverReg:
    def __init__(self, root):
        self.root = root
       
        ################################################# window_icon ################################################
        window_icon = PhotoImage(file="Images/SayuGoIcon.png")
        self.root.wm_iconphoto(True, window_icon)

        ################################################# Variables ################################################
        self.var_first_name = StringVar()
        self.var_last_name = StringVar()
        self.var_phone_no = StringVar()
        self.var_address = StringVar()
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_confirm_password = StringVar()
        self.var_license_no = StringVar()
        self.var_gender = StringVar()
        self.var_agree_terms = IntVar()

        ################################################# Background_image ################################################
        self.background_image = Image.open("Images/BackgroundRegester.jpg")
        self.background_image = self.background_image.resize((1560, 800))  # Resize to fit the window
        self.background_image = ImageTk.PhotoImage(self.background_image)
        label_of_background_image = Label(self.root, image=self.background_image)
        label_of_background_image.place(x=0, y=0, relwidth=1, relheight=1)

        ################################################# Background_image1 ################################################
        self.background_image1 = Image.open("Images/driverPoster.jpg")
        self.background_image1 = self.background_image1.resize((470, 600))  # Resizing the frame
        self.background_image1 = ImageTk.PhotoImage(self.background_image1)
        label_of_background_image1 = Label(self.root, image=self.background_image1)
        label_of_background_image1.place(x=65, y=100, width=470, height=600)

        ################################################## Frame #################################################
        my_frame = Frame(self.root, bg="#f0f0f0")  # Off-white color
        my_frame.place(x=520, y=100, width=950, height=600)


        ################################################## Register_label ##############################################
        label_register = Label(my_frame, text="Sign-Up", font=("Times New Roman", 24, "bold"), fg="black", bg="#f0f0f0")
        label_register.place(x=350, y=50, width=250, height=40)


        ################################################## First_name_label and entry #####################################
        first_name = Label(my_frame, text="First Name:", font=("Times New Roman", 14, "bold"), fg="black", bg="#f0f0f0")
        first_name.place(x=10, y=150, width=200, height=35)
        self.first_name_entry = ttk.Entry(my_frame, textvariable=self.var_first_name, font=("Times New Roman", 14,))
        self.first_name_entry.place(x=180, y=150, width=270, height=35)

        ################################################## Last_name_label and entry #################################################
        last_name = Label(my_frame, text="Last Name:", font=("Times New Roman", 14,"bold"), fg="black", bg="#f0f0f0")
        last_name.place(x=10, y=200, width=200, height=35)
        self.last_name_entry = ttk.Entry(my_frame, textvariable=self.var_last_name, font=("Times New Roman", 14,))
        self.last_name_entry.place(x=180, y=200, width=270, height=35)

        ################################################## Phone_number_label and entry #################################################
        phone_no = Label(my_frame, text="Phone Number:", font=("Times New Roman", 14, "bold"), fg="black", bg="#f0f0f0")
        phone_no.place(x=10, y=250, width=200, height=35)
        self.phone_no_entry = ttk.Entry(my_frame, textvariable=self.var_phone_no, font=("Times New Roman", 14,))
        self.phone_no_entry.place(x=180, y=250, width=270, height=35)

        ################################################## Address_label and entry #################################################
        address = Label(my_frame, text="Address:", font=("Times New Roman", 14,"bold"), fg="black", bg="#f0f0f0")
        address.place(x=10, y=300, width=200, height=35)
        self.address_entry = ttk.Entry(my_frame, textvariable=self.var_address, font=("Times New Roman", 14,))
        self.address_entry.place(x=180, y=300, width=270, height=35)

        ################################################## Email_label and entry #################################################
        email = Label(my_frame, text="Email:", font=("Times New Roman", 14,"bold"), fg="black", bg="#f0f0f0")
        email.place(x=465, y=150, width=200, height=35)
        self.email_entry = ttk.Entry(my_frame, textvariable=self.var_email, font=("Times New Roman", 14,))
        self.email_entry.place(x=640, y=150, width=300, height=35)

        ################################################## Password_label and entry #################################################
        password = Label(my_frame, text="Password:", font=("Times New Roman", 14,"bold"), fg="black", bg="#f0f0f0")
        password.place(x=475, y=200, width=200, height=35)
        self.password_entry = ttk.Entry(my_frame, textvariable=self.var_password, font=("Times New Roman", 14,), show="*")
        self.password_entry.place(x=640, y=200, width=300, height=35)

        ################################################## Confirm_password label and entry ########################################
        confirm_password = Label(my_frame, text="Confirm Password:", font=("Times New Roman", 14,"bold"), fg="black", bg="#f0f0f0")
        confirm_password.place(x=455, y=250, width=200, height=35)
        self.confirm_password_entry = ttk.Entry(my_frame, textvariable=self.var_confirm_password, font=("Times New Roman", 14,), show="*")
        self.confirm_password_entry.place(x=640, y=250, width=300, height=35)

        ################################################## License_number_label and entry ############################################
        license_no = Label(my_frame, text="License Number:", font=("Times New Roman", 14, "bold"), fg="black", bg="#f0f0f0")
        license_no.place(x=455, y=300, width=200, height=35)
        self.license_no_entry = ttk.Entry(my_frame, textvariable=self.var_license_no, font=("Times New Roman", 14,))
        self.license_no_entry.place(x=640, y=300, width=300, height=35)


        ################################################## Gender_label ##############################################################
        gender_label = Label(my_frame, text="Gender:", font=("Times New Roman", 14,"bold"), fg="black", bg="#f0f0f0")
        gender_label.place(x=10, y=360, width=200, height=35)

        ################################################## Gender_radio_buttons #################################################
        self.var_gender.set("Male")  # this is to default value

        male_radio = Radiobutton(my_frame, text="Male", value="Male", variable=self.var_gender, font=("Times New Roman", 14), fg="black", bg="#f0f0f0")
        male_radio.place(x=180, y=360, width=100, height=35)

        female_radio = Radiobutton(my_frame, text="Female", value="Female", variable=self.var_gender, font=("Times New Roman", 14), fg="black", bg="#f0f0f0")
        female_radio.place(x=290, y=360, width=100, height=35)

        other_radio = Radiobutton(my_frame, text="Other", value="Other", variable=self.var_gender, font=("Times New Roman", 14), fg="black", bg="#f0f0f0")
        other_radio.place(x=400, y=360, width=100, height=35)

        prefer_not_to_say_radio = Radiobutton(my_frame, text="Prefer not to say", value="Prefer not to say", variable=self.var_gender, font=("Times New Roman", 14), fg="black", bg="#f0f0f0")
        prefer_not_to_say_radio.place(x=510, y=360, width=200, height=35)

        ################################################## Check_Box #################################################
        self.check_box = Checkbutton(my_frame, text="I Agree The Terms & Conditions:", variable=self.var_agree_terms, font=("Times New Roman", 12,), onvalue=1, offvalue=0, fg="black", bg="#f0f0f0")
        self.check_box.place(x=50, y=420)

        ################################################## Register_Icon_image #################################################
        icon_image_register = Image.open("Images/RegisterButton.png")
        icon_image_register = icon_image_register.resize((100, 100))
        self.photoimage_register = ImageTk.PhotoImage(icon_image_register)
        b_register = Button(my_frame, image=self.photoimage_register, borderwidth=0, cursor="hand2", font=("Times New Roman", 12, "bold"), command=self.register)
        b_register.place(x=200, y=439, width=300)

        ################################################## Login Button #################################################
        icon_image_login = Image.open("Images/LoginButton.png")
        icon_image_login = icon_image_login.resize((100, 100))
        self.photoimage_login = ImageTk.PhotoImage(icon_image_login)
        b_login = Button(my_frame, image=self.photoimage_login, borderwidth=0, cursor="hand2",font=("Times New Roman", 12, "bold"),command=self.driverLogin)
        b_login.place(x=400, y=446, width=400)
        
    

    ################################################## register #################################################
    def register(self):
        if (self.var_first_name.get().strip() == "" or 
            self.var_last_name.get().strip() == "" or 
            self.var_phone_no.get().strip() == "" or 
            self.var_address.get().strip() == "" or 
            self.var_email.get().strip() == "" or
            self.var_password.get().strip() == "" or 
            self.var_confirm_password.get().strip() == "" or
            self.var_license_no.get().strip() == "" or
            self.var_gender.get().strip() == ""):
            messagebox.showerror("Error", "All fields are required")
            return

        if self.var_password.get() != self.var_confirm_password.get():
            messagebox.showerror("Error", "Passwords do not match")
            return

        if self.var_agree_terms.get() == 0:
            messagebox.showerror("Error", "Please agree to the terms and conditions")
            return

        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_pattern, self.var_email.get()):
            messagebox.showerror("Error", "Invalid email format")
            return

        phone_pattern = r'^\d{10}$'
        if not re.match(phone_pattern, self.var_phone_no.get()):
            messagebox.showerror("Error", "Invalid phone number format. It should be 10 digits")
            return

        try:
            connection = MyConn.connect(
                host="localhost", 
                user="root", 
                password="9828807288", 
                database="tbs"
            )
            my_cursor = connection.cursor()

            # this is to Email check
            my_cursor.execute("SELECT * FROM users WHERE email = %s", (self.var_email.get(),))
            if my_cursor.fetchone() is not None:
                messagebox.showerror("Error", "User already exists, Please try another email")
                return

            # this is to Insert user
            my_cursor.execute(
                "INSERT INTO users (email, password, role_id) VALUES (%s, %s, %s)",
                (self.var_email.get(), self.var_password.get(), 2)  
            )
            connection.commit()
            user_id = my_cursor.lastrowid  

            # this is to Insert driver profile
            my_cursor.execute(
                """
                INSERT INTO driver_profiles (first_name, last_name, address, phone_number, gender, license_no, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    self.var_first_name.get().strip(),
                    self.var_last_name.get().strip(),
                    self.var_address.get().strip(),
                    self.var_phone_no.get().strip(),
                    self.var_gender.get().strip(),
                    self.var_license_no.get().strip(),
                    user_id
                )
            )
            connection.commit()

            messagebox.showinfo("Success", "Registration successful!")
            self.driverLogin()
            
        except MyConn.Error as e:
            messagebox.showerror("Database Error", f"Error connecting to database: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
        finally:
            if connection.is_connected():
                my_cursor.close()
                connection.close()
                
    def clearScreen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def clear_fields(self):
        """Clears all input fields after successful registration."""
        self.var_first_name.set("")
        self.var_last_name.set("")
        self.var_phone_no.set("")
        self.var_address.set("")
        self.var_email.set("")
        self.var_password.set("")
        self.var_confirm_password.set("")
        self.var_license_no.set("")
        self.var_gender.set("Male")
        self.var_agree_terms.set(0)

    def driverLogin(self):
        self.clearScreen()
        from driverLogin import driver
        driver(self.root)


################################################ Finish ##################################################


