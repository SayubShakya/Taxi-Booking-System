from tkinter import * #this is importing all tkinter (*) =aLL
from tkinter import messagebox  #this is importing show pop-up messages
from tkinter import ttk  #this is importing widgets_like_combobox
from PIL import Image, ImageTk  #this is importing images
import mysql.connector as MyConn #this is importing MySQL_connector_to_interact_with_database
import Global  #this is to import globle varible for id
from db import Db as Database #this is importing Database from db

class driverDashboard:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg="#808080")

        # this is for background image setup
        self.background_image = Image.open("Images/driverDashboard.jpg")
        self.background_image = self.background_image.resize((1560, 800))
        self.bg = ImageTk.PhotoImage(self.background_image)

        # Create Label for background image
        bg_label = Label(self.root, image=self.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # this is for gray_background
        top_frame = Frame(self.root, height=100, bg="#808080")
        top_frame.place(x=0, y=0, width=1560, height=100)

        # Title Label
        title_Label = Label(top_frame, text="TAXI BOOKING SYSTEM", font=("Times New Roman", 30, "bold"), bg="#808080")
        title_Label.place(x=20, y=20)

        # log_name_label = Label(top_frame, text="Welcome: [User Name]", font=("Times New Roman", 20), bg="#808080")
        # log_name_label.place(x=900, y=30)

        # Left Frame with gray background
        left_frame = Frame(self.root, width=300, bg="#808080")
        left_frame.place(x=0, y=100, width=350, height=700)

        # Dashboard_label
        Dashboard = Label(left_frame, text="Driver Dashboard", font=("Times New Roman", 25, "bold"), width=20, bg="#808080", cursor="hand2")
        Dashboard.place(x=-23, y=50)

        # Buttons
        complete_trip = Button(left_frame, text="View Trip", font=("Times New Roman", 16), width=20, bg="#cccccc", cursor="hand2", command= self.completeTrip)
        complete_trip.place(x=50, y=130)

        trip_history = Button(left_frame, text="View Trip History", font=("Times New Roman", 16), width=20, bg="#cccccc", cursor="hand2", command=self.tripHistory)
        trip_history.place(x=50, y=240)

        Vehicle_info = Button(root, text="Vehicle", font=("Times New Roman", 16), width=20, bg="#cccccc", cursor="hand2", command=self.vehicle)
        Vehicle_info.place(x=50, y=285)

        my_profile_button = Button(left_frame, text="My Profile", font=("Times New Roman", 16), width=20, bg="#cccccc", cursor="hand2", command=self.viewProfile)
        my_profile_button.place(x=50, y=300)

        change_password_button = Button(left_frame, text="Change Password", font=("Times New Roman", 16), width=20, bg="#cccccc", cursor="hand2", command=self.change_password_driver)
        change_password_button.place(x=50, y=360)

        # this is for Status_radio_buttons
        self.my_status = StringVar()
        status_button = ["ACTIVE", "INACTIVE"]

        for i, radio_status in enumerate(status_button):
            Radiobutton(left_frame, variable=self.my_status, text=radio_status, value=radio_status, bg="#808080").place(x=130, y=450 + (i * 30))

        self.my_label = Label(left_frame, bg="#808080", text="You selected: ACTIVE")
        self.my_label.place(x=130, y=520)

        Button(left_frame, text="Update Status", command=self.update_status, bg="#cccccc").place(x=130, y=560)

        # Logout_button
        logout_button = Button(left_frame, text="Logout", font=("Times New Roman", 16), width=20, bg="#cccccc", cursor="hand2", command=self.driver_logout)
        logout_button.place(x=50, y=620)



    ################################################ update_status ##################################################
    def update_status(self):
        selected_status = self.my_status.get()
        self.my_label.config(text=f"You selected: {selected_status}")
        
        driver_id = Global.id
        
        try:
            mydb = MyConn.connect(
                host="localhost", 
                user="root", 
                password="9828807288",
                database="tbs")
            
            cursor = mydb.cursor()
            query = "UPDATE driver_profiles SET status = %s WHERE user_id = %s"
            cursor.execute(query, (selected_status, driver_id))
            mydb.commit()
            messagebox.showinfo("Success", "Status updated successfully!")

        except MyConn.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

        finally:

            if mydb.is_connected():
                mydb.close()


    ################################################## completeTrip #################################################
    def completeTrip(self):
        my_frame = Frame(self.root, bg="#a6a6a6")
        my_frame.place(x=350, y=100, width=1300, height=700)

        # this is to Load and display background image
        self.booking_bg_image = Image.open("Images/dashboardBg.jpg")
        self.booking_bg_image = self.booking_bg_image.resize((1300, 700))
        self.booking_bg_image = ImageTk.PhotoImage(self.booking_bg_image)

        bg_label = Label(my_frame, image=self.booking_bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title label
        label_register = Label(my_frame,text="Assign Booking",font=("Times New Roman", 24, "bold"),fg="black",bg="#a6a6a6")
        label_register.place(x=350, y=50, width=300, height=40)

        # this is to Create the treeview for the table
        columns = ("Booking ID", "Pickup Location", "Drop Off Location", "Pickup Date", "Pickup Time")
        self.treeview = ttk.Treeview(my_frame, columns=columns, show="headings")

        #this is to Define the headings
        for col in columns:
            self.treeview.heading(col, text=col)

        #this is to Define the column widths
        self.treeview.column("Booking ID", width=100)
        self.treeview.column("Pickup Location", width=200)
        self.treeview.column("Drop Off Location", width=200)
        self.treeview.column("Pickup Date", width=150)
        self.treeview.column("Pickup Time", width=150)

        # this is to Place the treeview
        self.treeview.place(x=10, y=150, width=1200, height=300)
        data = self.fetch_AssignTrip_info()  # Ensure this function returns a list of tuples
        for row in data:
            self.treeview.insert("", "end", values=row)

        # this is to Bind a selection event
        self.treeview.bind("<ButtonRelease-1>", self.on_select_completeTrip)

    def on_select_completeTrip(self, event):
        # this is to Get selected item
        selected_item = self.treeview.selection()

        if selected_item:
            selected_values = self.treeview.item(selected_item[0], "values")
            self.booking_id = selected_values[0]

            # this is to Fetch driver details using booking_id
            customer_info = self.fetch_Customer_info(self.booking_id)

            # this is to Create a new window to display driver details
            new_window = Toplevel(self.root)
            new_window.title("Assign Trip")
            new_window.geometry("500x500")

            label_register = Label(new_window,text="Assign Trip Details",font=("Times New Roman", 24, "bold"),fg="black")
            label_register.place(x=120, y=50, width=300, height=40)

            # this is for UI elements for driver details
            labels = ["CustomerID", "CustomerName", "Phone"]
            entries = {}
            y_positions = [150, 200, 250]

            for i, label_text in enumerate(labels):
                label = Label(new_window,text=f"{label_text}:",font=("Times New Roman", 14, "bold"),fg="black",bg=new_window.cget("bg"))
                label.place(x=10, y=y_positions[i], width=200, height=35)

                entry = ttk.Entry(new_window, font=("Times New Roman", 14))
                entry.place(x=220, y=y_positions[i], width=270, height=35)
                entries[label_text] = entry

            completeBtn = Button(new_window, text="Complete", command=self.complete, font=("Times New Roman", 12, "bold"), fg="black", bg="green", bd=0, relief="flat", height=2, width=12)
            completeBtn.place(x=200,y=350)

            if customer_info:
                entries["CustomerID"].insert(0, customer_info[0])
                entries["CustomerName"].insert(0, customer_info[1])
                entries["Phone"].insert(0, customer_info[2])

            # this is to Set all fields to readonly
            for entry in entries.values():
                entry.config(state="readonly")
    
    def complete(self):
        bid = self.booking_id
        print(bid)

        try:
            # this is to connection to the database
            connection = MyConn.connect(
                host="localhost", 
                user="root", 
                password="9828807288", 
                database="tbs"
            )
            my_cursor = connection.cursor()

            # this is to query
            query = "UPDATE bookings SET status = %s WHERE id = %s"
            values = ('COMPLETED', bid)
            my_cursor.execute(query, values)

            # this is to Commit the transaction
            connection.commit()

            messagebox.showinfo("Success", "Update successfully!")
            self.completeTrip()

        except MyConn.Error as e:
            # this is to Handle MySQL specific errors
            messagebox.showerror("Database Error", f"Error connecting to database: {str(e)}")
        except Exception as e:
            # this is to Handle other types of errors
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
        finally:
            # this is to Ensure cursor and connection are closed
            if connection.is_connected():
                my_cursor.close()
                connection.close()

    def fetch_AssignTrip_info(self):
        try:
            connection = MyConn.connect(
                host="localhost",
                user="root",
                password="9828807288",
                database="tbs"
            )
            my_cursor = connection.cursor()
            query = "SELECT id, pick_up_address, drop_off_address, pick_up_date, pick_up_time FROM bookings WHERE driver_id = %s and status='Assign'"
            my_cursor.execute(query, (Global.id,))
            rows = my_cursor.fetchall()
            return rows if rows else []  # this is to Return an empty list if no rows found
        except MyConn.Error as e:
            messagebox.showerror("Database Error", f"Error connecting to database: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                my_cursor.close()
                connection.close()

    def fetch_Customer_info(self, booking_id):
        try:
            connection = MyConn.connect(
                host="localhost",
                user="root",
                password="9828807288",
                database="tbs"
            )
            my_cursor = connection.cursor()

            # this is to Fetch driver_id using booking_id
            query = "SELECT customer_id FROM bookings WHERE id = %s"
            my_cursor.execute(query, (booking_id,))
            booking_row = my_cursor.fetchone()

            if booking_row and booking_row[0]:  # If driver_id exists
                customer_id = booking_row[0]

                # this is to Fetch driver details using driver_id
                query = "SELECT user_id, first_name, phone_number FROM customer_profiles WHERE user_id = %s"
                my_cursor.execute(query, (customer_id,))
                cus_row = my_cursor.fetchone()

                if cus_row:
                    return cus_row
            return None
        except MyConn.Error as e:
            messagebox.showerror("Database Error", f"Error fetching driver details: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                my_cursor.close()
                connection.close()



    ################################################## tripHistory #################################################
    def tripHistory(self):
        my_frame = Frame(self.root, bg="#a6a6a6")
        my_frame.place(x=350, y=100, width=1300, height=700)

        # this is to Load and display background image
        self.booking_bg_image = Image.open("Images/dashboardBg.jpg")
        self.booking_bg_image = self.booking_bg_image.resize((1300, 700))
        self.booking_bg_image = ImageTk.PhotoImage(self.booking_bg_image)

        bg_label = Label(my_frame, image=self.booking_bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title label
        label_register = Label(my_frame,text="Trip History",font=("Times New Roman", 24, "bold"),fg="black",bg="#a6a6a6")
        label_register.place(x=350, y=50, width=300, height=40)

        # this is to Create the treeview for the table
        columns = ("Booking ID", "Pickup Location", "Drop Off Location", "Pickup Date", "Pickup Time", "Status")
        self.treeview = ttk.Treeview(my_frame, columns=columns, show="headings")

        # this is to Define the headings
        for col in columns:
            self.treeview.heading(col, text=col)

        # this is to Define the column widths
        self.treeview.column("Booking ID", width=100)
        self.treeview.column("Pickup Location", width=200)
        self.treeview.column("Drop Off Location", width=200)
        self.treeview.column("Pickup Date", width=150)
        self.treeview.column("Pickup Time", width=150)
        self.treeview.column("Status", width=150)

        # this is to Place the treeview
        self.treeview.place(x=10, y=150, width=1200, height=300)
        data = self.fetch_TripHistory_info()  # Ensure this function returns a list of tuples
        for row in data:
            self.treeview.insert("", "end", values=row)

        # this is to Bind a selection event
        self.treeview.bind("<ButtonRelease-1>", self.on_select_TripHistory)
    
    def fetch_TripHistory_info(self):
        try:
            connection = MyConn.connect(
                host="localhost",
                user="root",
                password="9828807288",
                database="tbs"
            )
            my_cursor = connection.cursor()
            query = "SELECT id, pick_up_address, drop_off_address, pick_up_date, pick_up_time, status FROM bookings WHERE driver_id = %s and status='COMPLETED'"
            my_cursor.execute(query, (Global.id,))
            rows = my_cursor.fetchall()
            return rows if rows else []  # this is to Return an empty list if no rows found
        except MyConn.Error as e:
            messagebox.showerror("Database Error", f"Error connecting to database: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                my_cursor.close()
                connection.close()

    def on_select_TripHistory(self, event):
        # this is to Get selected item
        selected_item = self.treeview.selection()

        if selected_item:
            selected_values = self.treeview.item(selected_item[0], "values")
            self.booking_id = selected_values[0]

            # this is to Fetch driver details using booking_id
            customer_info = self.fetch_Customer_info(self.booking_id)

            # this is to Create a new window to display driver details
            new_window = Toplevel(self.root)
            new_window.title("Customer Information")
            new_window.geometry("500x500")

            label_register = Label(new_window,text="Customer Trip Details",font=("Times New Roman", 24, "bold"),fg="black")
            label_register.place(x=120, y=50, width=300, height=40)

            # this is for UI elements for driver details
            labels = ["CustomerID", "CustomerName", "Phone"]
            entries = {}
            y_positions = [150, 200, 250]

            for i, label_text in enumerate(labels):
                label = Label(new_window,text=f"{label_text}:",font=("Times New Roman", 14, "bold"),fg="black",bg=new_window.cget("bg"))
                label.place(x=10, y=y_positions[i], width=200, height=35)

                entry = ttk.Entry(new_window, font=("Times New Roman", 14))
                entry.place(x=220, y=y_positions[i], width=270, height=35)
                entries[label_text] = entry

            if customer_info:
                entries["CustomerID"].insert(0, customer_info[0])
                entries["CustomerName"].insert(0, customer_info[1])
                entries["Phone"].insert(0, customer_info[2])

            # this is to Set all fields to readonly
            for entry in entries.values():
                entry.config(state="readonly")


    def fetch_vehicle_info(self):
        # this is to Connect to the database and fetch vehicle data for the logged-in driver
        try:
            connection = MyConn.connect(
                host="localhost",
                user="root",
                password="9828807288",
                database="tbs"
            )
            cursor = connection.cursor()

            # this is to Use the logged-in user's ID (Global.id)
            user_id = Global.id  

            # this is to Query
            query = """SELECT v.id, v.name, v.number, v.color FROM vehicles vJOIN driver_profiles dp ON v.driver_profile_id = dp.id WHERE dp.user_id = %s
            """
            cursor.execute(query, (user_id,))
            result = cursor.fetchall()

            return result  # this is to Return the fetched data

        except MyConn.Error as e:
            messagebox.showerror("Database Error", f"Error: {str(e)}")
            return []  #this is to Return an empty list in case of an error
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


    ################################################## vehicle #################################################
    def vehicle(self):
        # Create a frame for the vehicle view
        my_frame = Frame(self.root, bg="#a6a6a6")
        my_frame.place(x=350, y=100, width=1300, height=700)

        # Load and display background image
        self.booking_bg_image = Image.open("Images/dashboardBg.jpg")
        self.booking_bg_image = self.booking_bg_image.resize((1300, 700))
        self.booking_bg_image = ImageTk.PhotoImage(self.booking_bg_image)
        bg_label = Label(my_frame, image=self.booking_bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title label
        label_register = Label(my_frame, text="Vehicle Information", font=("Times New Roman", 24, "bold"), fg="black", bg="#a6a6a6")
        label_register.place(x=350, y=50, width=300, height=40)

        # Create the treeview for the table
        columns = ("Vehicle ID", "Name", "Number", "Color")
        self.treeview = ttk.Treeview(my_frame, columns=columns, show="headings")

        # Define the headings
        for col in columns:
            self.treeview.heading(col, text=col)

        # Define the column widths
        self.treeview.column("Vehicle ID", width=100)
        self.treeview.column("Name", width=200)
        self.treeview.column("Number", width=200)
        self.treeview.column("Color", width=150)

        # Place the treeview
        self.treeview.place(x=10, y=150, width=1200, height=300)

        # Fetch data specific to the logged-in driver and populate the table
        data = self.fetch_vehicle_info()
        for row in data:
            self.treeview.insert("", "end", values=row)

        # Add Vehicle Button
        add_button = Button(my_frame, text="Add Vehicle", font=("Times New Roman", 12, "bold"), command=self.add_vehicle_window, fg="black", bg="green", relief="flat", height=2, width=15)
        add_button.place(x=450, y=500)

        # Bind a selection event
        self.treeview.bind("<ButtonRelease-1>", lambda event: self.add_vehicle_window())

    def add_vehicle_window(self):
        # Open a new window for adding a vehicle
        new_window = Toplevel(self.root)
        new_window.title("Add Vehicle")
        new_window.geometry("500x500")

        label_register = Label(new_window, text="Add Vehicle", font=("Times New Roman", 24, "bold"), fg="black")
        label_register.place(x=100, y=25, width=300, height=40)

        # Name
        name_label = Label(new_window, text="Name:", font=("Times New Roman", 14, "bold"), fg="black", bg=new_window.cget("bg"))
        name_label.place(x=10, y=100, width=200, height=35)
        self.name_entry = ttk.Entry(new_window, font=("Times New Roman", 14))
        self.name_entry.place(x=220, y=100, width=270, height=35)

        # Number
        number_label = Label(new_window, text="Number:", font=("Times New Roman", 14, "bold"), fg="black", bg=new_window.cget("bg"))
        number_label.place(x=10, y=150, width=200, height=35)
        self.number_entry = ttk.Entry(new_window, font=("Times New Roman", 14))
        self.number_entry.place(x=220, y=150, width=270, height=35)

        # Color
        color_label = Label(new_window, text="Color:", font=("Times New Roman", 14, "bold"), fg="black", bg=new_window.cget("bg"))
        color_label.place(x=10, y=200, width=200, height=35)
        self.color_entry = ttk.Entry(new_window, font=("Times New Roman", 14))
        self.color_entry.place(x=220, y=200, width=270, height=35)

        # Submit Button
        submit_button = Button(new_window, text="Add Vehicle", font=("Times New Roman", 12, "bold"), command=self.insert_vehicle_data, fg="black", bg="green", relief="flat", height=2, width=12)
        submit_button.place(x=150, y=300, width=200)

    def insert_vehicle_data(self):
        name = self.name_entry.get()
        number = self.number_entry.get()
        color = self.color_entry.get()
        database = Database()  # Object of the Database class
        try:
            # Fetch driver profile from the database
            driver_profile = database.queryOne(f"SELECT id FROM driver_profiles WHERE user_id = {Global.id}")
         
            if driver_profile:
                driver_profile_id = driver_profile[0]
                # Insert the new vehicle into the database
                database.queryUpdate(f"INSERT INTO vehicles (name, number, color, driver_profile_id) VALUES ('{name}', '{number}', '{color}', {driver_profile_id})")
                messagebox.showinfo("Success", "Vehicle added successfully!")
                self.vehicle()  # Refresh the vehicle list
            else:
                messagebox.showerror("Error", "Driver profile not found!")

        except MyConn.Error as e:
            messagebox.showerror("Database Error", f"Error: {str(e)}")
        finally:
            database.disconnect()

    def fetch_vehicle_info(self):
        database = Database()  # Object of the Database class
        try:
            query = f"""
            SELECT v.id, v.name, v.number, v.color FROM vehicles v JOIN driver_profiles dp ON v.driver_profile_id = dp.id WHERE dp.user_id = {Global.id};
            """
            return database.queryAll(query)  # Execute and return data
        except MyConn.Error as e:
            messagebox.showerror("Database Error", f"Error: {str(e)}")
            return []


            

################################################ viewProfile ##################################################


    def viewProfile(self):
        my_frame = Frame(self.root, bg="#a6a6a6")
        my_frame.place(x=350, y=100, width=1300, height=700)

        self.booking_bg_image = Image.open("Images/dashboardBg.jpg")
        self.booking_bg_image = self.booking_bg_image.resize((1300, 700))
        self.booking_bg_image = ImageTk.PhotoImage(self.booking_bg_image)

        bg_label = Label(my_frame, image=self.booking_bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        bg_label = Label(my_frame, image=self.booking_bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        #labels
        profile = Label(my_frame,text="View Profile: ",font=("Times New Roman",14,"bold" ),fg="black",bg="#a6a6a6")
        profile.place(x=350, y=50, width=300, height=40)


        first_name = Label(my_frame,text="First Name:",font=("Times New Roman", 14,"bold"),fg="black",bg="#a6a6a6")
        first_name.place(x=10, y=200, width=300, height=40)
        self.firstEntry = Entry(my_frame, width=20)
        self.firstEntry.place(x=300, y=200, width=300, height=40)


        last_name = Label(my_frame,text="Last Name:",font=("Times New Roman", 14,"bold"),fg="black",bg="#a6a6a6")
        last_name.place(x=10, y=250, width=300, height=40)
        self.lastEntry = Entry(my_frame, width=20)
        self.lastEntry.place(x=300, y=250, width=300, height=40)


        address = Label(my_frame,text="Address",font=("Times New Roman", 14,"bold"),fg="black",bg="#a6a6a6")
        address.place(x=10, y=300, width=300, height=40)
        self.addressEntry = Entry(my_frame, width=20)
        self.addressEntry.place(x=300, y=300, width=300, height=40)

        gender = Label(my_frame,text="Gender:",font=("Times New Roman", 14,"bold"),fg="black",bg="#a6a6a6")
        gender.place(x=10, y=350, width=300, height=40)
        self.genderEntry = Entry(my_frame, width=20)
        self.genderEntry.place(x=300, y=350, width=300, height=40)

        phoneno = Label(my_frame,text="Phone:",font=("Times New Roman", 14,"bold"),fg="black",bg="#a6a6a6")
        phoneno.place(x=10, y=400, width=300, height=40)
        self.phoneEntry = Entry(my_frame, width=20)
        self.phoneEntry.place(x=300, y=400, width=300, height=40)

        license_no = Label(my_frame,text="License Number:",font=("Times New Roman", 14,"bold"),fg="black",bg="#a6a6a6")
        license_no.place(x=8, y=450, width=300, height=40)
        self.license_noEntry = Entry(my_frame, width=20)
        self.license_noEntry.place(x=300, y=450, width=300, height=40)

        update_Button = Button(my_frame, text="Update", borderwidth=0, cursor="hand2", font=("Times New Roman", 12, "bold"), command=self.updateData, fg="black", bg="green", bd=0, relief="flat", height=2, width=12)
        update_Button.place(x=80, y=550, width=200)


                # Back Button
        back_Button = Button(my_frame, text="Back", borderwidth=0, cursor="hand2", font=("Times New Roman", 12, "bold"), command=self.backButton, fg="black", bg="red", bd=0, relief="flat", height=2, width=12)
        back_Button.place(x=350, y=550, width=200, height=50)

        self.fetchProfile()
    
    def fetchProfile(self):
        try:
                connection = MyConn.connect(
                    host="localhost",
                    user="root",
                    password="9828807288",
                    database="tbs"
                )
                my_cursor = connection.cursor()
                my_cursor.execute(f"SELECT * FROM driver_profiles WHERE user_id={Global.id}")
                row = my_cursor.fetchall()
                for data in row:
                    self.firstEntry.insert(0, data[1])
                    self.lastEntry.insert(0, data[2])
                    self.addressEntry.insert(0, data[3])
                    self.phoneEntry.insert(0, data[4])
                    self.genderEntry.insert(0, data[5])
                    self.license_noEntry.insert(0, data[8])
                connection.close()
        except Exception as e:
                messagebox.showerror("Error", f"Database Error: {e}")
            
    def updateData(self):
        firstname=self.firstEntry.get()
        lastname=self.lastEntry.get()
        address=self.addressEntry.get()
        phone=self.phoneEntry.get()
        gender=self.genderEntry.get()
        license=self.license_noEntry.get()
        try:
            connection = MyConn.connect(
                host="localhost", 
                user="root", 
                password="9828807288", 
                database="tbs"
            )
            my_cursor = connection.cursor()

            # Insert user
            my_cursor.execute(
                "Update driver_profiles set first_name=%s,last_name=%s,address=%s, phone_number=%s, gender=%s, license_no=%s where user_id=%s",
                (firstname,lastname,address,phone,gender,license, Global.id)  
            )
            connection.commit()

            messagebox.showinfo("Success", "Update successfully!")
            
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

    def backButton(self):
            self.clearScreen()
            from driverDash import driverDashboard 
            driverDashboard(self.root) 

    def clearScreen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


     ################################################## driver_logout #################################################
    def driver_logout(self):
        # Confirm logout
        response = messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?")
        if response: 
            self.clearScreen()
            from driverLogin import driver 
            driver(self.root) 

    def clearScreen(self):
        for widget in self.root.winfo_children():
            widget.destroy()



     ################################################## change_password_driver #################################################
    def change_password_driver(self):
        # new window 
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
    app = driverDashboard(root)
    root.mainloop()
