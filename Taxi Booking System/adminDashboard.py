from tkinter import * #this is importing all tkinter (*) =aLL
from tkinter import messagebox  #this is importing show pop-up messages
from tkinter import ttk  #this is importing widgets_like_combobox
from PIL import Image, ImageTk  #this is importing images
import mysql.connector as MyConn  #this is importing MySQL_connector_to_interact_with_database
import re  #this is the importing check_patterns
from db import Db as Database #this is importing Database from db

class helloAdmin:
    def __init__(self, root):
        self.root = root  # this is to root window
        self.root.configure(bg="gray")  # this is background color to gray



        # ##################################################  background_Image  ##################################################
        self.background_image = Image.open("Images/adminDashboard.jpg")  # this is to background image
        self.background_image = self.background_image.resize((1560, 800))  # Resize
        self.bg = ImageTk.PhotoImage(self.background_image)  # to Convert image to Tkinter format



        # ##################################################  Background_Label  ##################################################
        bg_label = Label(self.root, image=self.bg)  # label background image
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # this is to background image 



        # ##################################################  Gray_Top_Frame_  ##################################################
        top_frame = Frame(self.root, height=100, bg="gray")  # this is to top frame with gray background
        top_frame.place(x=0, y=0, width=1560, height=100)  #this is to position and size top frame



        # ##################################################  Title_Labe ##################################################
        title_Label = Label(top_frame, text="TAXI BOOKING SYSTEM", font=("Times New Roman", 30, "bold"), bg="gray")  # title label
        title_Label.place(x=20, y=20)  # this is to positing



        # ##################################################  Left_Frame  ##################################################
        left_frame = Frame(self.root, width=300, bg="gray")  #this is to left frame for the buttons
        left_frame.place(x=0, y=100, width=350, height=700)  #position 



        # ##################################################  Dashboard_Label  ##################################################
        Dashboard = Label(left_frame, text="Admin Dashboard", font=("Times New Roman", 25, "bold"), width=20, bg="gray", cursor="hand2")  #dashboard label
        Dashboard.place(x=-20, y=50)  # Position 

        # ################################################## Buttons ##################################################
        assign_driver_button = Button(left_frame, text="View Request", font=("Times New Roman", 16), width=20, bg="#cccccc", cursor="hand2", command=self.assignDriver)  # button to assign driver
        assign_driver_button.place(x=50, y=130)  # Position 

        add_customer_button = Button(left_frame, text="Add Customer", font=("Times New Roman", 16), width=20, bg="#cccccc", cursor="hand2", command=self.addCustomer)  # button to add customer
        add_customer_button.place(x=50, y=200)  # Position 

        add_driver_button = Button(left_frame, text="Add Driver", font=("Times New Roman", 16), width=20, bg="#cccccc", cursor="hand2", command=self.addDriver)  # button to add driver
        add_driver_button.place(x=50, y=270)  # Position 

        view_all_bookings_button = Button(left_frame, text="View All Bookings", font=("Times New Roman", 16), width=20, bg="#cccccc", cursor="hand2", command=self.viewAllBookings)  # button to add driver
        view_all_bookings_button.place(x=50, y=340)  # Position 

        change_password_button = Button(left_frame, text="Change Password", font=("Times New Roman", 16), width=20, bg="#cccccc", cursor="hand2", command=self.change_password_admin)  # button to change password
        change_password_button.place(x=50, y=410)  # Position 

        logout_button = Button(left_frame, text="Logout", font=("Times New Roman", 16), width=20, bg="#cccccc", cursor="hand2", command=self.admin_logout)  # button to log out
        logout_button.place(x=50, y=480)  # Position 




    ##################################################  Assign Drive  r####################################################
    def assignDriver(self):
        #this is frame for booking view
        my_frame = Frame(self.root, bg="#a6a6a6")
        my_frame.place(x=350, y=100, width=1300, height=700)

        # this is to display background image
        self.booking_bg_image = Image.open("Images/dashboardBg.jpg")
        self.booking_bg_image = self.booking_bg_image.resize((1300, 700))  # Resize image 
        self.booking_bg_image = ImageTk.PhotoImage(self.booking_bg_image)  # this is to Convert image for Tkinter

        bg_label = Label(my_frame, image=self.booking_bg_image)  # label to display image
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Position of background label

        # label for "Assign Driver"
        label_register = Label(my_frame,text="Assign Driver",font=("Times New Roman", 24, "bold"),fg="black",bg="#a6a6a6")
        label_register.place(x=350, y=50, width=300, height=40)

        # this is to treeview for displaying bookings
        columns = ("Bid", "Pickup Address", "Drop Off Address", "Pickup Date", "Pickup Time", "Booking Status")
        self.treeview = ttk.Treeview(my_frame, columns=columns, show="headings")

        # this is for headings 
        for col in columns:
            self.treeview.heading(col, text=col)

        # this is for column widths 
        self.treeview.column("Bid", width=100)
        self.treeview.column("Pickup Address", width=200)
        self.treeview.column("Drop Off Address", width=200)
        self.treeview.column("Pickup Date", width=150)
        self.treeview.column("Pickup Time", width=150)
        self.treeview.column("Booking Status", width=150)

        # this is to Place 
        self.treeview.place(x=10, y=150, width=1200, height=300)

        # this is to Fetch 
        data = self.fetch_assignBook_info()  # Get data for pending bookings
        for row in data:
            self.treeview.insert("", "end", values=row)  # Insert 

        #this is to Bind 
        self.treeview.bind("<ButtonRelease-1>", self.on_select_assignDriver)

    def on_select_assignDriver(self, event):
        selected_item = self.treeview.selection()

        if selected_item:
            selected_values = self.treeview.item(selected_item[0], "values")
            booking_id = selected_values[0]

            window = Tk()
            window.geometry("300x200")
            window.title("Assign")

            # Display booking ID
            Label(window, text="Book ID", font=("Arial", 14, "bold")).place(x=10, y=10)
            self.bidEntry = Entry(window, width=20)
            self.bidEntry.place(x=100, y=10)
            self.bidEntry.insert(0, booking_id)

            # Fetch drivers
            driver_data = self.fetch_driver_info()
            self.driver_map = {name: id for id, name in driver_data}  # Map name to ID
            driver_names = list(self.driver_map.keys())

            # ComboBox for driver selection
            self.combo = ttk.Combobox(window, values=driver_names, state="readonly")
            self.combo.place(x=10, y=50, width=200)
            self.combo.set("Select Name:")
            self.combo.bind("<<ComboboxSelected>>", self.on_combo_select)

            # Assign button
            Button(window,text="Assign",command=self.assignId,font=("Times New Roman", 12, "bold"),fg="black",bg="green",bd=0,relief="flat",height=2,width=12).place(x=90, y=110)

    def on_combo_select(self, event):
        # this is to get selected driver ID from ComboBox
        self.selected_value = self.combo.get()

    def assignId(self):
        bid = self.bidEntry.get()
        driver_name = self.combo.get()

        # Retrieve driver ID from the map
        did = self.driver_map.get(driver_name)

        if not did:
            messagebox.showerror("Error", "Invalid driver selection!")
            return

        try:
            mydb = MyConn.connect(
                host="localhost",
                user="root",
                password="9828807288",
                database="tbs"
            )
            cursor = mydb.cursor()

            # Update booking with driver ID
            query = "UPDATE bookings SET driver_id=%s, status='ASSIGN' WHERE id=%s"
            cursor.execute(query, (did, bid))

            # Update driver status
            query1 = "UPDATE driver_profiles SET status=%s WHERE user_id=%s"
            cursor.execute(query1, ('INACTIVE', did))

            mydb.commit()
            messagebox.showinfo("Success", "Driver Assign successfull!")
            self.assignDriver()

        except MyConn.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

        finally:
            if mydb.is_connected():
                mydb.close()


    def fetch_assignBook_info(self):
        try:
            connection = MyConn.connect(
                host="localhost",
                user="root",
                password="9828807288",
                database="tbs"
            )
            my_cursor = connection.cursor()
            
            # this is to Query 
            query = "SELECT id, pick_up_address, drop_off_address, pick_up_date, pick_up_time, status FROM bookings WHERE status = 'PENDING'"
            my_cursor.execute(query)
            
            rows = my_cursor.fetchall()  # this is to Fetch all the rows
            return rows  # this is to Return list of rows

        except MyConn.Error as e:
            # this is to show error 
            messagebox.showerror("Database Error", f"Error connecting to database: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                my_cursor.close()
                connection.close()

    def fetch_driver_info(self):
        try:
            connection = MyConn.connect(
                host="localhost",
                user="root",
                password="9828807288",
                database="tbs"
            )
            my_cursor = connection.cursor()

            # Fetch driver IDs and full names of drivers who are ACTIVE
            query = "SELECT user_id, CONCAT(first_name, ' ', last_name) AS full_name FROM driver_profiles WHERE status = 'ACTIVE'"
            my_cursor.execute(query)

            # Fetch all active driver details
            data = [(row[0], row[1]) for row in my_cursor.fetchall()]  # List of tuples (id, full_name)
            return data  # Return list of tuples

        except MyConn.Error as e:
            messagebox.showerror("Database Error", f"Error fetching driver details: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                my_cursor.close()
                connection.close()






    ###################################################  addCustomer  #################################################
    def addCustomer(self): 
        # Variables
        self.var_first_name = StringVar()
        self.var_last_name = StringVar()
        self.var_address = StringVar()
        self.var_phone_no = StringVar()
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_confirm_password = StringVar()
        self.var_gender = StringVar()

        my_frame = Frame(self.root, bg="#a6a6a6")
        my_frame.place(x=350, y=100, width=1300, height=700)

        self.booking_bg_image = Image.open("Images/dashboardBg.jpg")
        self.booking_bg_image = self.booking_bg_image.resize((1300, 700))
        self.booking_bg_image = ImageTk.PhotoImage(self.booking_bg_image)

        bg_label = Label(my_frame, image=self.booking_bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Register Label
        label_register = Label(my_frame, text="Sign-Up Customer", font=("Times New Roman", 24, "bold"), fg="black", bg="#a6a6a6")
        label_register.place(x=350, y=50, width=250, height=40)

        # First Name
        first_name = Label(my_frame, text="First Name:", font=("Times New Roman", 14, "bold"), fg="black", bg="#a6a6a6")
        first_name.place(x=10, y=150, width=200, height=35)
        self.first_name_entry = ttk.Entry(my_frame, textvariable=self.var_first_name, font=("Times New Roman", 14,))
        self.first_name_entry.place(x=180, y=150, width=270, height=35)

        # Last_name_label and entry
        last_name = Label(my_frame, text="Last Name:", font=("Times New Roman", 14,"bold"), fg="black", bg="#a6a6a6")
        last_name.place(x=10, y=200, width=200, height=35)
        self.last_name_entry = ttk.Entry(my_frame, textvariable=self.var_last_name, font=("Times New Roman", 14,))
        self.last_name_entry.place(x=180, y=200, width=270, height=35)

        # Phone_number_label and entry
        phone_no = Label(my_frame, text="Phone Number:", font=("Times New Roman", 14, "bold"), fg="black", bg="#a6a6a6")
        phone_no.place(x=10, y=250, width=200, height=35)
        self.phone_no_entry = ttk.Entry(my_frame, textvariable=self.var_phone_no, font=("Times New Roman", 14,))
        self.phone_no_entry.place(x=180, y=250, width=270, height=35)

        # Address_label and entry
        address = Label(my_frame, text="Address:", font=("Times New Roman", 14,"bold"), fg="black", bg="#a6a6a6")
        address.place(x=10, y=300, width=200, height=35)
        self.address_entry = ttk.Entry(my_frame, textvariable=self.var_address, font=("Times New Roman", 14,))
        self.address_entry.place(x=180, y=300, width=270, height=35)

        # Email_label and entry
        email = Label(my_frame, text="Email:", font=("Times New Roman", 14,"bold"), fg="black", bg="#a6a6a6")
        email.place(x=465, y=150, width=200, height=35)
        self.email_entry = ttk.Entry(my_frame, textvariable=self.var_email, font=("Times New Roman", 14,))
        self.email_entry.place(x=640, y=150, width=300, height=35)

        # Password_label and entry
        password = Label(my_frame, text="Password:", font=("Times New Roman", 14,"bold"), fg="black", bg="#a6a6a6")
        password.place(x=465, y=200, width=200, height=35)
        self.password_entry = ttk.Entry(my_frame, textvariable=self.var_password, font=("Times New Roman", 14,), show="*")
        self.password_entry.place(x=640, y=200, width=300, height=35)

        # Confirm_password label and entry
        confirm_password = Label(my_frame, text="Confirm Password:", font=("Times New Roman", 14,"bold"), fg="black", bg="#a6a6a6")
        confirm_password.place(x=465, y=250, width=200, height=35)
        self.confirm_password_entry = ttk.Entry(my_frame, textvariable=self.var_confirm_password, font=("Times New Roman", 14,), show="*")
        self.confirm_password_entry.place(x=640, y=250, width=300, height=35)

        self.var_gender.set("Male")  # Default value
        gender_label = Label(my_frame, text="Gender:", font=("Times New Roman", 14, "bold"), fg="black", bg="#a6a6a6")
        gender_label.place(x=10, y=360, width=200, height=35)

        Radiobutton(my_frame, text="Male", value="Male", variable=self.var_gender, font=("Times New Roman", 14), bg="#a6a6a6").place(x=180, y=360, width=100, height=35)
        Radiobutton(my_frame, text="Female", value="Female", variable=self.var_gender, font=("Times New Roman", 14), bg="#a6a6a6").place(x=290, y=360, width=100, height=35)
        Radiobutton(my_frame, text="Other", value="Other", variable=self.var_gender, font=("Times New Roman", 14), bg="#a6a6a6").place(x=400, y=360, width=100, height=35)

        # Register Button
        b_register = Button(my_frame, text = "Register", borderwidth=0, cursor="hand2", font=("Times New Roman", 12, "bold"), command=self.registerCustomer, fg="black", bg="green", bd=0, relief="flat", height=2, width=12)
        b_register.place(x=80, y=500, width=250)

         # Back Button
        back_Button = Button(my_frame, text="Back", borderwidth=0, cursor="hand2", font=("Times New Roman", 12, "bold"), command=self.adminBackButton, fg="black", bg="red", bd=0, relief="flat", height=2, width=12)
        back_Button.place(x=350, y=500, width=200, height=50)


    def adminBackButton(self):
        self.clearScreen()
        from adminDashboard import helloAdmin 
        helloAdmin(self.root)  




    ################################################## register ##################################################
    def registerCustomer(self):
        if any(field.get().strip() == "" for field in [self.var_first_name, self.var_last_name, self.var_phone_no, self.var_address, self.var_email, self.var_password, self.var_confirm_password]):
            messagebox.showerror("Error", "All fields are required")
            return

        if self.var_password.get() != self.var_confirm_password.get():
            messagebox.showerror("Error", "Passwords do not match")
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

            # this is to Check if email exists
            my_cursor.execute("SELECT * FROM users WHERE email = %s", (self.var_email.get(),))
            if my_cursor.fetchone() is not None:
                messagebox.showerror("Error", "User already exists, please try another email")
                return

            # this is to Insert user
            my_cursor.execute("INSERT INTO users (email, password, role_id) VALUES (%s, %s, %s)", (self.var_email.get(), self.var_password.get(), 1))
            connection.commit()
            user_id = my_cursor.lastrowid

            # this is to Insert customer profile
            my_cursor.execute("""INSERT INTO customer_profiles (first_name, last_name, address, phone_number, gender, user_id) VALUES (%s, %s, %s, %s, %s, %s)""",
                (
                self.var_first_name.get().strip(),
                self.var_last_name.get().strip(),
                self.var_address.get().strip(),
                self.var_phone_no.get().strip(),
                self.var_gender.get().strip(),
                user_id
            ))
            connection.commit()

            messagebox.showinfo("Success", "Registration successful!")
        except MyConn.Error as e:
            messagebox.showerror("Database Error", f"Error connecting to database: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
        finally:
            if 'connection' in locals() and connection.is_connected():
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
            self.var_gender.set("Male")



    ################################################# addDriver #################################################
    def addDriver(self): 

        # Variables
        self.var_first_name = StringVar()
        self.var_last_name = StringVar()
        self.var_phone_no = StringVar()
        self.var_address = StringVar()
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_confirm_password = StringVar()
        self.var_license_no = StringVar()
        self.var_gender = StringVar()

        my_frame = Frame(self.root, bg="#a6a6a6")
        my_frame.place(x=350, y=100, width=1300, height=700)

        self.booking_bg_image = Image.open("Images/dashboardBg.jpg")
        self.booking_bg_image = self.booking_bg_image.resize((1300, 700))
        self.booking_bg_image = ImageTk.PhotoImage(self.booking_bg_image)

        bg_label = Label(my_frame, image=self.booking_bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Register_label
        label_register = Label(my_frame, text="Sign-Up Driver", font=("Times New Roman", 24, "bold"), fg="black", bg="#a6a6a6")
        label_register.place(x=350, y=50, width=250, height=40)

        # First_name_label and entry
        first_name = Label(my_frame, text="First Name:", font=("Times New Roman", 14, "bold"), fg="black", bg="#a6a6a6")
        first_name.place(x=10, y=150, width=200, height=35)
        self.first_name_entry = ttk.Entry(my_frame, textvariable=self.var_first_name, font=("Times New Roman", 14,))
        self.first_name_entry.place(x=180, y=150, width=270, height=35)

        # Last_name_label and entry
        last_name = Label(my_frame, text="Last Name:", font=("Times New Roman", 14,"bold"), fg="black", bg="#a6a6a6")
        last_name.place(x=10, y=200, width=200, height=35)
        self.last_name_entry = ttk.Entry(my_frame, textvariable=self.var_last_name, font=("Times New Roman", 14,))
        self.last_name_entry.place(x=180, y=200, width=270, height=35)

        # Phone_number_label and entry
        phone_no = Label(my_frame, text="Phone Number:", font=("Times New Roman", 14, "bold"), fg="black", bg="#a6a6a6")
        phone_no.place(x=10, y=250, width=200, height=35)
        self.phone_no_entry = ttk.Entry(my_frame, textvariable=self.var_phone_no, font=("Times New Roman", 14,))
        self.phone_no_entry.place(x=180, y=250, width=270, height=35)

        # Address_label and entry
        address = Label(my_frame, text="Address:", font=("Times New Roman", 14,"bold"), fg="black", bg="#a6a6a6")
        address.place(x=10, y=300, width=200, height=35)
        self.address_entry = ttk.Entry(my_frame, textvariable=self.var_address, font=("Times New Roman", 14,))
        self.address_entry.place(x=180, y=300, width=270, height=35)

        # Email_label and entry
        email = Label(my_frame, text="Email:", font=("Times New Roman", 14,"bold"), fg="black", bg="#a6a6a6")
        email.place(x=465, y=150, width=200, height=35)
        self.email_entry = ttk.Entry(my_frame, textvariable=self.var_email, font=("Times New Roman", 14,))
        self.email_entry.place(x=650, y=150, width=300, height=35)

        # Password_label and entry
        password = Label(my_frame, text="Password:", font=("Times New Roman", 14,"bold"), fg="black", bg="#a6a6a6")
        password.place(x=465, y=200, width=200, height=35)
        self.password_entry = ttk.Entry(my_frame, textvariable=self.var_password, font=("Times New Roman", 14,), show="*")
        self.password_entry.place(x=650, y=200, width=300, height=35)

        # Confirm_password label and entry
        confirm_password = Label(my_frame, text="Confirm Password:", font=("Times New Roman", 14,"bold"), fg="black", bg="#a6a6a6")
        confirm_password.place(x=465, y=250, width=200, height=35)
        self.confirm_password_entry = ttk.Entry(my_frame, textvariable=self.var_confirm_password, font=("Times New Roman", 14,), show="*")
        self.confirm_password_entry.place(x=650, y=250, width=300, height=35)

        # License_number_label and entry
        license_no = Label(my_frame, text="License Number:", font=("Times New Roman", 14, "bold"), fg="black", bg="#a6a6a6")
        license_no.place(x=465, y=300, width=200, height=35)
        self.license_no_entry = ttk.Entry(my_frame, textvariable=self.var_license_no, font=("Times New Roman", 14,))
        self.license_no_entry.place(x=650, y=300, width=300, height=35)

        self.var_gender.set("Male")  # Default value
        gender_label = Label(my_frame, text="Gender:", font=("Times New Roman", 14, "bold"), fg="black", bg="#a6a6a6")
        gender_label.place(x=10, y=360, width=200, height=35)

        Radiobutton(my_frame, text="Male", value="Male", variable=self.var_gender, font=("Times New Roman", 14), bg="#a6a6a6").place(x=180, y=360, width=100, height=35)
        Radiobutton(my_frame, text="Female", value="Female", variable=self.var_gender, font=("Times New Roman", 14), bg="#a6a6a6").place(x=290, y=360, width=100, height=35)
        Radiobutton(my_frame, text="Other", value="Other", variable=self.var_gender, font=("Times New Roman", 14), bg="#a6a6a6").place(x=400, y=360, width=100, height=35)

        # Register Button
        b_register = Button(my_frame, text = "Register", borderwidth=0, cursor="hand2", font=("Times New Roman", 12, "bold"), command=self.registerDriver, fg="black", bg="green", bd=0, relief="flat", height=2, width=12)
        b_register.place(x=80, y=500, width=250)

        # Back Button
        back_Button = Button(my_frame, text="Back", borderwidth=0, cursor="hand2", font=("Times New Roman", 12, "bold"), command=self.adminBackButton, fg="black", bg="red", bd=0, relief="flat", height=2, width=12)
        back_Button.place(x=350, y=500, width=200, height=50)


    def registerDriver(self):
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
            # self.driverLogin()
            
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




    ####################################################### viewAllBookings #######################################
    def viewAllBookings(self):
        # frame 
        my_frame = Frame(self.root, bg="#a6a6a6")
        my_frame.place(x=350, y=100, width=1300, height=700)

        # background image
        self.booking_bg_image = Image.open("Images/dashboardBg.jpg")
        self.booking_bg_image = self.booking_bg_image.resize((1300, 700))
        self.booking_bg_image = ImageTk.PhotoImage(self.booking_bg_image)

        bg_label = Label(my_frame, image=self.booking_bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # label
        label_register = Label(my_frame, text="View All Booking History", font=("Times New Roman", 24, "bold"), fg="black", bg="#a6a6a6")
        label_register.place(x=350, y=50, width=500, height=40)

        # treeview
        columns = ("Booking ID", "Pickup Location", "Drop Off Location", "Pickup Date", "Pickup Time", "Status", "Customer Name", "Driver Name")
        self.treeview = ttk.Treeview(my_frame, columns=columns, show="headings")

        for col in columns:
            self.treeview.heading(col, text=col)

        self.treeview.column("Booking ID", width=100)
        self.treeview.column("Pickup Location", width=200)
        self.treeview.column("Drop Off Location", width=200)
        self.treeview.column("Pickup Date", width=150)
        self.treeview.column("Pickup Time", width=150)
        self.treeview.column("Status", width=150)
        self.treeview.column("Customer Name", width=200)
        self.treeview.column("Driver Name", width=200)

        # this is for treeview
        self.treeview.place(x=10, y=150, width=1200, height=300)

        # this is to Fetch  data
        data = self.fetch_viewAllBookingHistory_info()
        for row in data:
            self.treeview.insert("", "end", values=row)

    def fetch_viewAllBookingHistory_info(self):
        try:
            connection = MyConn.connect(
                host="localhost",
                user="root",
                password="9828807288",
                database="tbs"
            )
            my_cursor = connection.cursor()
            query = """
                SELECT b.id AS booking_id, b.pick_up_address, b.drop_off_address, b.pick_up_date, b.pick_up_time, b.status, CONCAT(c.first_name, ' ', c.last_name) AS customer_name,CONCAT(d.first_name, ' ', d.last_name) AS driver_name
                FROM bookings b LEFT JOIN customer_profiles c ON b.customer_id = c.user_id LEFT JOIN driver_profiles d ON b.driver_id = d.user_id
            """
            my_cursor.execute(query)
            rows = my_cursor.fetchall()
            return rows
        except MyConn.Error as e:
            messagebox.showerror("Database Error", f"Error connecting to database: {str(e)}")
            return []
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
            return []
        finally:
            if 'connection' in locals() and connection.is_connected():
                my_cursor.close()
                connection.close()


        

    ################################################# admin_logout #################################################
    def admin_logout(self):
        # this is to Confirm logout
        response = messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?")
        if response: 
            self.clearScreen()
            from adminLogin import adminWIn 
            adminWIn(self.root) 

    def clearScreen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def change_password_admin(self):
        # this is to open new window 
        self.root2 = Toplevel()
        self.root2.title("Forgot Password")
        self.root2.geometry("340x550+410+70")

        forgot_password = Label(self.root2, text="Forgot Password", font=("Times New Roman", 20, "bold"), fg="black", bg="#f0f0f0")
        forgot_password.place(x=0, y=10, relwidth=1)  

        # Email entry 
        email_label = Label(self.root2, text="Email Address:", font=("Times New Roman", 14,"bold"), fg="black", bg="#f0f0f0")
        email_label.place(x=70, y=55, width=200, height=35)
        self.email = ttk.Entry(self.root2, font=("Times New Roman", 14,))
        self.email.place(x=70, y=100, width=200, height=35)

        # Old password 
        old_password_label = Label(self.root2, text="Old Password:", font=("Times New Roman", 14,"bold"), fg="black", bg="#f0f0f0")
        old_password_label.place(x=70, y=150, width=200, height=35)
        self.old_password_entry = ttk.Entry(self.root2, font=("Times New Roman", 14,), show="*")
        self.old_password_entry.place(x=70, y=200, width=200, height=35)

        # New password 
        new_password_label = Label(self.root2, text="New Password:", font=("Times New Roman", 14,"bold"), fg="black", bg="#f0f0f0")
        new_password_label.place(x=70, y=250, width=200, height=35)
        self.new_password_entry = ttk.Entry(self.root2, font=("Times New Roman", 14,), show="*")
        self.new_password_entry.place(x=70, y=300, width=200, height=35)

        # Confirm new password 
        new_confirm_password_label = Label(self.root2, text="Confirm New Password:", font=("Times New Roman", 14,"bold"), fg="black", bg="#f0f0f0")
        new_confirm_password_label.place(x=70, y=350, width=200, height=35)
        self.new_confirm_password_entry = ttk.Entry(self.root2, font=("Times New Roman", 14,), show="*")
        self.new_confirm_password_entry.place(x=70, y=400, width=200, height=35)

        # Reset password button
        reset_button = Button(self.root2, text="Reset Password", font=("Times New Roman", 14, "bold"), bg="#4CAF50", fg="white", width=18, height=2, command=self.reset_password)
        reset_button.place(x=70, y=460)

    def reset_password(self):
        # this is to Fetch value
        email = self.email.get()
        old_password = self.old_password_entry.get()
        new_password = self.new_password_entry.get()
        confirm_new_password = self.new_confirm_password_entry.get()

        # this is to Validate input
        if not email or not old_password or not new_password or not confirm_new_password:
            messagebox.showerror("Error", "Please fill in all fields")
            return
        
        if new_password != confirm_new_password:
            messagebox.showerror("Error", "New passwords do not match")
            return

        connection = MyConn.connect(
            host="localhost",
            user="root",
            password="9828807288",
            database="tbs"
        )
        my_cursor = connection.cursor()
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        my_cursor.execute(query, (email, old_password))
        row = my_cursor.fetchone()

        if row is None:
            messagebox.showerror("Error", "Incorrect email or old password")
        else:
            update_query = "UPDATE users SET password = %s WHERE email = %s"
            my_cursor.execute(update_query, (new_password, email))
            connection.commit()
            messagebox.showinfo("Success", "Password has been successfully updated")
            self.root2.destroy()     
    

################################################ Finish ##################################################


if __name__ == "__main__":
    root = Tk()
    app = helloAdmin(root)
    root.mainloop()
