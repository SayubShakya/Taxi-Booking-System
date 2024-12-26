from tkinter import * #this is importing all tkinter (*) =aLL
from tkinter import messagebox  #this is importing show pop-up messages
from tkinter import ttk  #this is importing widgets_like_combobox
from PIL import Image, ImageTk  #this is importing images
from tkcalendar import DateEntry #this is importing tkcalendar dateEntry
import tkintermapview  #this is importing ttkintermapview
import mysql.connector as MyConn #this is importing MySQL_connector_to_interact_with_database
import Global  #this is to import globle varible for id
from datetime import datetime #this is importing datetime
from db import Db as Database #this is importing Database from db

class cusDashboard:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg="#808080")

        self.background_image = Image.open("Images/customerDashboard.jpg")
        self.background_image = self.background_image.resize((1560, 800))
        self.bg = ImageTk.PhotoImage(self.background_image)

        # Create Label for background image
        bg_label = Label(self.root, image=self.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # this is to gray_background
        top_frame = Frame(self.root, height=100, bg="#808080")
        top_frame.place(x=0, y=0, width=1560, height=100)

        # Title Label
        title_Label = Label(top_frame, text="TAXI BOOKING SYSTEM", font=("Times New Roman", 30, "bold"), bg="#808080")
        title_Label.place(x=20, y=20)

        #this is to Left Frame with gray background
        left_frame = Frame(self.root, width=300, bg="#808080")
        left_frame.place(x=0, y=100, width=350, height=700)

        # Dashboard_label
        Dashboard = Label(left_frame, text="Customer Dashboard", font=("Times New Roman", 20, "bold"), width=20, bg="#808080", cursor="hand2")
        Dashboard.place(x=20, y=50)

        # this is to Buttons
        booking_button = Button(left_frame, text="Booking", font=("Times New Roman", 16), width=20, bg="#cccccc", cursor="hand2", command= self.customerbooking)
        booking_button.place(x=50, y=130)

        profile_button = Button(left_frame, text="My Profile", font=("Times New Roman", 16), width=20, bg="#cccccc", cursor="hand2", command=self.viewProfile)
        profile_button.place(x=50, y=200)

        view_booking_button = Button(left_frame, text="View Booking", font=("Times New Roman", 16), width=20, bg="#cccccc", cursor="hand2", command = self.viewBooking)
        view_booking_button.place(x=50, y=270)

        booking_history_button = Button(left_frame, text="Booking History", font=("Times New Roman", 16), width=20, bg="#cccccc", cursor="hand2", command = self.viewHistory)
        booking_history_button.place(x=50, y=340)

        change_password_button = Button(left_frame, text="Change Password", font=("Times New Roman", 16), width=20, bg="#cccccc", cursor="hand2", command=self.change_password_customer)
        change_password_button.place(x=50, y=410)

        logout_button = Button(left_frame, text="Logout", font=("Times New Roman", 16), width=20, bg="#cccccc", cursor="hand2", command=self.customer_logout)
        logout_button.place(x=50, y=480)




    ################################################# customerbooking #################################################
    def customerbooking(self):
        my_frame = Frame(self.root, bg="#a6a6a6")
        my_frame.place(x=350, y=100, width=1300, height=700)

        self.booking_bg_image = Image.open("Images/dashboardBg.jpg")
        self.booking_bg_image = self.booking_bg_image.resize((1300, 700))
        self.booking_bg_image = ImageTk.PhotoImage(self.booking_bg_image)

        bg_label = Label(my_frame, image=self.booking_bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        label_register = Label(my_frame, text="Customer Booking", font=("Times New Roman", 24, "bold"), fg="black", bg="#a6a6a6")
        label_register.place(x=350, y=50, width=300, height=40)

        # Pickup Address
        pick_up_address = Label(my_frame, text="Pickup Address:", font=("Times New Roman", 14, "bold"), fg="black", bg=my_frame.cget("bg"), bd=0, relief="flat")
        pick_up_address.place(x=10, y=150, width=200, height=35)
        self.pick_up_address_entry = ttk.Entry(my_frame, font=("Times New Roman", 14,))
        self.pick_up_address_entry.place(x=220, y=150, width=270, height=35)

        # Dropoff Address
        drop_up_address = Label(my_frame, text="Dropoff Address:", font=("Times New Roman", 14, "bold"), fg="black", bg=my_frame.cget("bg"), bd=0, relief="flat")
        drop_up_address.place(x=10, y=200, width=200, height=35)
        self.drop_up_address_entry = ttk.Entry(my_frame, font=("Times New Roman", 14,))
        self.drop_up_address_entry.place(x=220, y=200, width=270, height=35)

        # Pickup Date
        pick_up_date = Label(my_frame, text="Pickup Date:", font=("Times New Roman", 14, "bold"), fg="black", bg=my_frame.cget("bg"), bd=0, relief="flat")
        pick_up_date.place(x=10, y=250, width=200, height=35)

        # DateEntry
        self.pick_up_date_entry = DateEntry(my_frame, font=("Times New Roman", 14,), width=12)  
        self.pick_up_date_entry.place(x=220, y=250, width=270, height=35)

        # Pickup Time dropdown
        pick_up_time_label = Label(my_frame, text="Pickup Time:", font=("Times New Roman", 14, "bold"), fg="black", bg=my_frame.cget("bg"), bd=0, relief="flat")
        pick_up_time_label.place(x=10, y=300, width=200, height=35)

        # Time picker dropdown
        self.pick_up_hour = ttk.Combobox(my_frame, font=("Times New Roman", 14,), values=[f"{i:02d}" for i in range(1, 13)], width=5) 
        self.pick_up_hour.place(x=220, y=300, width=80, height=35)
        self.pick_up_hour.set("12")  

        self.pick_up_minute = ttk.Combobox(my_frame, font=("Times New Roman", 14,), values=[f"{i:02d}" for i in range(0, 60, 5)], width=5)  
        self.pick_up_minute.place(x=310, y=300, width=80, height=35)
        self.pick_up_minute.set("00")  

        # Register Button
        register_Button = Button(my_frame, text="Register Booking", borderwidth=0, cursor="hand2", font=("Times New Roman", 12, "bold"), fg="black", bg="green", bd=0, relief="flat", height=2, width=12, command = self.registerBooking)
        register_Button.place(x=10, y=400, width=200, height=50)


        # Back Button
        back_Button = Button(my_frame, text="Back", borderwidth=0, cursor="hand2", font=("Times New Roman", 12, "bold"), command=self.backButton, fg="black", bg="red", bd=0, relief="flat", height=2, width=12)
        back_Button.place(x=240, y=400, width=200, height=50)

        # this is to set Map 
        mero_map = Frame(my_frame, bg="white", width=550, height=400)
        mero_map.place(x=550, y=150)

        map_widget = tkintermapview.TkinterMapView(mero_map, width=550, height=400, corner_radius=0)
        map_widget.set_address("Kathmandu, Nepal")  
        map_widget.set_zoom(10)
        map_widget.pack()

        mero_frame= LabelFrame(my_frame, bg="lightblue", bd=0)
        mero_frame.place(x=550, y=505, width=550, height=50)  

        my_entry = Entry(mero_frame, font=("Helvetica", 18))
        my_entry.place(x=10, y=10, width=420, height=30)

        my_button = Button(mero_frame, text="Lookup", font=("Helvetica", 14), bg="blue", fg="white", height=1, width=10)
        my_button.place(x=440, y=10)




    ################################################# registerBooking #################################################
    def registerBooking(self):
        pick_up_address = self.pick_up_address_entry.get()
        drop_off_address = self.drop_up_address_entry.get()
        pick_up_date = self.pick_up_date_entry.get()
        pickup_time = f"{self.pick_up_hour.get()}:{self.pick_up_minute.get()}"

        try:
            # this is to convert the pick_up_date to a datetime object to compare with the current date
            pick_up_date_obj = datetime.strptime(pick_up_date, "%m/%d/%y")
            current_date = datetime.now()

            # this is to check if the selected date is in the past
            if pick_up_date_obj < current_date:
                messagebox.showerror("Error", "You cannot book a ride for past date!")
                return

            # If the date is valid, convert it to the required format
            pick_up_date = pick_up_date_obj.strftime("%Y-%m-%d")

        except ValueError as e:
            messagebox.showerror("Error", f"Invalid date format: {e}")
            return 

        user_id = Global.id
        print("Global ID:", user_id)

        try:
            
            connection = MyConn.connect(
                host="localhost",
                user="root",
                password="9828807288",
                database="tbs"
            )
            my_cursor = connection.cursor()
            my_cursor.execute(
                """INSERT INTO bookings (customer_id, pick_up_address, drop_off_address, pick_up_date, pick_up_time, status) VALUES (%s, %s, %s, %s, %s, %s)""",
                (user_id, pick_up_address, drop_off_address, pick_up_date, pickup_time, 'Pending')
            )
            connection.commit()  
            messagebox.showinfo("Success", "Booking registered successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Database Error: {e}")
        finally:
            if connection.is_connected():
                my_cursor.close()
                connection.close()




    ################################################# viewProfile #################################################
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
        profile = Label(my_frame,text="View Profile: ",font=("Times New Roman", 24, "bold"),fg="black",bg="#a6a6a6")
        profile.place(x=350, y=50, width=300, height=40)


        first_name = Label(my_frame,text="First Name:",font=("Times New Roman", 14, "bold"),fg="black",bg="#a6a6a6")
        first_name.place(x=10, y=200, width=300, height=40)
        self.firstEntry = Entry(my_frame, width=20)
        self.firstEntry.place(x=250, y=200, width=300, height=40)


        last_name = Label(my_frame,text="Last Name:",font=("Times New Roman",  14, "bold"),fg="black",bg="#a6a6a6")
        last_name.place(x=10, y=250, width=300, height=40)
        self.lastEntry = Entry(my_frame, width=20)
        self.lastEntry.place(x=250, y=250, width=300, height=40)


        address = Label(my_frame,text="Address",font=("Times New Roman",  14, "bold"),fg="black",bg="#a6a6a6")
        address.place(x=10, y=300, width=300, height=40)
        self.addressEntry = Entry(my_frame, width=20)
        self.addressEntry.place(x=250, y=300, width=300, height=40)

        gender = Label(my_frame,text="Gender:",font=("Times New Roman",  14, "bold"),fg="black",bg="#a6a6a6")
        gender.place(x=10, y=350, width=300, height=40)
        self.genderEntry = Entry(my_frame, width=20)
        self.genderEntry.place(x=250, y=350, width=300, height=40)

        phoneno = Label(my_frame,text="Phone:",font=("Times New Roman",  14, "bold"),fg="black",bg="#a6a6a6")
        phoneno.place(x=10, y=400, width=300, height=40)
        self.phoneEntry = Entry(my_frame, width=20)
        self.phoneEntry.place(x=250, y=400, width=300, height=40)

        update_Button = Button(my_frame, text="Update", borderwidth=0, cursor="hand2", font=("Times New Roman", 12, "bold"), command=self.updateData1, fg="black", bg="green", bd=0, relief="flat", height=2, width=12)
        update_Button.place(x=80, y=500, width=200)

        # Back Button
        back_Button = Button(my_frame, text="Back", borderwidth=0, cursor="hand2", font=("Times New Roman", 12, "bold"), command=self.backButton, fg="black", bg="red", bd=0, relief="flat", height=2, width=12)
        back_Button.place(x=350, y=500, width=200, height=50)

        self.fetchProfile()
    
    def fetchProfile(self):
        try:
            db = Database()
            row = db.queryAll(f"SELECT * FROM customer_profiles WHERE user_id={Global.id}")
            
            for data in row:
                    self.firstEntry.insert(0, data[1])
                    self.lastEntry.insert(0, data[2])
                    self.addressEntry.insert(0, data[3])
                    self.phoneEntry.insert(0, data[4])
                    self.genderEntry.insert(0, data[5])
            db.disconnect()
        except Exception as e:
                messagebox.showerror("Error", f"Database Error: {e}")
            
    def updateData1(self):
        firstname=self.firstEntry.get()
        lastname=self.lastEntry.get()
        address=self.addressEntry.get()
        phone=self.phoneEntry.get()
        gender=self.genderEntry.get()
        try:
            connection = MyConn.connect(
                host="localhost", 
                user="root", 
                password="9828807288", 
                database="tbs"
            )
            my_cursor = connection.cursor()

            #this is to Insert user
            my_cursor.execute(
                "Update customer_profiles set first_name=%s,last_name=%s,address=%s, phone_number=%s, gender=%s where user_id=%s",
                (firstname,lastname,address,phone,gender,Global.id)  
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

    ################################################ viewBooking #################################################
    def fetch_booking_info(self):
        try:
                connection = MyConn.connect(
                    host="localhost",
                    user="root",
                    password="9828807288",
                    database="tbs"
                )
                my_cursor = connection.cursor()
                print(Global.id)
                my_cursor.execute(f"SELECT * FROM bookings WHERE customer_id={Global.id} and status='Pending'")
                row = my_cursor.fetchall()
                return row

        except MyConn.Error as e:
            messagebox.showerror("Database Error", f"Error connecting to database: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
        finally:
            if connection.is_connected():
                my_cursor.close()
                connection.close()

    def viewBooking(self):
        # this is for frame 
        my_frame = Frame(self.root, bg="#a6a6a6")
        my_frame.place(x=350, y=100, width=1300, height=700)

        # background image
        self.booking_bg_image = Image.open("Images/dashboardBg.jpg")
        self.booking_bg_image = self.booking_bg_image.resize((1300, 700))
        self.booking_bg_image = ImageTk.PhotoImage(self.booking_bg_image)

        bg_label = Label(my_frame, image=self.booking_bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # label
        label_register = Label(my_frame,text="View Booking",font=("Times New Roman", 24, "bold"),fg="black",bg="#a6a6a6")
        label_register.place(x=350, y=50, width=300, height=40)

        # this is to treeview table
        columns = ("Booking ID", "Pickup Location", "Drop Off Location", "Pickup Date", "Pickup Time")
        self.treeview = ttk.Treeview(my_frame, columns=columns, show="headings")
        for col in columns:
            self.treeview.heading(col, text=col)

        self.treeview.column("Booking ID", width=100)
        self.treeview.column("Pickup Location", width=200)
        self.treeview.column("Drop Off Location", width=200)
        self.treeview.column("Pickup Date", width=150)
        self.treeview.column("Pickup Time", width=150)
        self.treeview.place(x=10, y=150, width=1200, height=300)

        # this is to fetch data
        data = self.fetch_booking_info() 
        for row in data:
            self.treeview.insert("", "end", values=row)

        # this is to bind 
        self.treeview.bind("<ButtonRelease-1>", self.on_select_booking)

    def on_select_booking(self, event):

        selected_item = self.treeview.selection()
        new_window = Tk()
        new_window.title("Update Books")
        new_window.geometry("500x500")

        label_register = Label(new_window, text="Update Booking", font=("Times New Roman", 24, "bold"), fg="black")
        label_register.place(x=120, y=50, width=300, height=40)

        # Pickup Address
        pick_up_address = Label(new_window, text="Pickup Address:", font=("Times New Roman", 14, "bold"), fg="black", bg=new_window.cget("bg"))
        pick_up_address.place(x=10, y=150, width=200, height=35)
        self.pick_up_address_entry = ttk.Entry(new_window, font=("Times New Roman", 14))
        self.pick_up_address_entry.place(x=220, y=150, width=270, height=35)

        # Dropoff Address
        drop_up_address = Label(new_window, text="Dropoff Address:", font=("Times New Roman", 14, "bold"), fg="black", bg=new_window.cget("bg"))
        drop_up_address.place(x=10, y=200, width=200, height=35)
        self.drop_up_address_entry = ttk.Entry(new_window, font=("Times New Roman", 14))
        self.drop_up_address_entry.place(x=220, y=200, width=270, height=35)

        # Pickup Date
        pick_up_date = Label(new_window, text="Pickup Date:", font=("Times New Roman", 14, "bold"), fg="black", bg=new_window.cget("bg"))
        pick_up_date.place(x=10, y=250, width=200, height=35)
        self.pick_up_date_entry = DateEntry(new_window, font=("Times New Roman", 14))
        self.pick_up_date_entry.place(x=220, y=250, width=270, height=35)

        # Pickup Time
        pick_up_time = Label(new_window, text="Pickup Time:", font=("Times New Roman", 14, "bold"), fg="black", bg=new_window.cget("bg"))
        pick_up_time.place(x=10, y=300, width=200, height=35)
        self.pick_up_time_entry = ttk.Entry(new_window, font=("Times New Roman", 14))
        self.pick_up_time_entry.place(x=220, y=300, width=270, height=35)

        self.bid = None
        print(self.bid)

        if selected_item:
            # this is to values of selected row
            selected_values = self.treeview.item(selected_item[0], "values")
            print("Selected Row Values:", selected_values)

            self.bid=selected_values[0]

            self.pick_up_address_entry.delete(0, END)
            self.pick_up_address_entry.insert(0, selected_values[1])

            self.drop_up_address_entry.delete(0, END)
            self.drop_up_address_entry.insert(0, selected_values[2])

            self.pick_up_date_entry.delete(0, END)
            self.pick_up_date_entry.insert(0, selected_values[3])

            self.pick_up_time_entry.delete(0, END)
            self.pick_up_time_entry.insert(0, selected_values[4])
        
        # this is to Submit Button
        update_Button = Button(new_window, text="Submit", borderwidth=0, cursor="hand2", font=("Times New Roman", 12, "bold"), command=self.updateData, fg="black", bg="green", bd=0, relief="flat", height=2, width=12)
        update_Button.place(x=150, y=350, width=200)

        # this is to cancel Button
        cancel_Button = Button(new_window, text="Cancel Booking", borderwidth=0, cursor="hand2", font=("Times New Roman", 12, "bold"), command=self.cancelbookingData, fg="black", bg="Red", bd=0, relief="flat", height=2, width=12)
        cancel_Button.place(x=150, y=420, width=200)

    def updateData(self):
        bid1=self.bid
        pick_up=self.pick_up_address_entry.get()
        drop_up=self.drop_up_address_entry.get()
        pick_up_date=self.pick_up_date_entry.get()
        pick_up_time=self.pick_up_time_entry.get()

        try:
            connection = MyConn.connect(
                host="localhost", 
                user="root", 
                password="9828807288", 
                database="tbs"
            )
            my_cursor = connection.cursor()

            my_cursor.execute(
                "Update bookings set pick_up_address=%s,drop_off_address=%s,pick_up_date=%s, pick_up_time=%s where id=%s",
                (pick_up,drop_up,pick_up_date,pick_up_time,bid1)  
            )
            connection.commit()

            messagebox.showinfo("Success", "Update successfully!")
            
        except MyConn.Error as e:
            messagebox.showerror("Database Error", f"Error connecting to database: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
        finally:
            self.viewBooking()
            if connection.is_connected():
                my_cursor.close()
                connection.close()



    def cancelbookingData(self):
        bid1 = self.bid 
        try:
            #this is for database
            connection = MyConn.connect(
                host="localhost", 
                user="root", 
                password="9828807288", 
                database="tbs"
            )
            my_cursor = connection.cursor()

            #this is to delete booking from database
            my_cursor.execute("DELETE FROM bookings WHERE id=%s", (bid1,))
            connection.commit()

            # this is to show success message
            messagebox.showinfo("Success", "Booking cancelled successfully!")
            
        except MyConn.Error as e:
            messagebox.showerror("Database Error", f"Error connecting to database: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
        finally:
            self.viewBooking()
            if connection.is_connected():
                my_cursor.close()
                connection.close()



    ################################################# viewHistory #################################################
    def viewHistory(self):
        #  this is to frame 
        my_frame = Frame(self.root, bg="#a6a6a6")
        my_frame.place(x=350, y=100, width=1300, height=700)

        #  this is to background image
        self.booking_bg_image = Image.open("Images/dashboardBg.jpg")
        self.booking_bg_image = self.booking_bg_image.resize((1300, 700))
        self.booking_bg_image = ImageTk.PhotoImage(self.booking_bg_image)

        bg_label = Label(my_frame, image=self.booking_bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # label
        label_register = Label(my_frame,text="Booking History",font=("Times New Roman", 24, "bold"),fg="black", bg="#a6a6a6")
        label_register.place(x=350, y=50, width=300, height=40)

        # this is to treeview for the table
        columns = ("Booking ID", "Pickup Location", "Drop Off Location", "Pickup Date", "Pickup Time", "Status")
        self.treeview = ttk.Treeview(my_frame, columns=columns, show="headings")

        for col in columns:
            self.treeview.heading(col, text=col)


        self.treeview.column("Booking ID", width=100)
        self.treeview.column("Pickup Location", width=200)
        self.treeview.column("Drop Off Location", width=200)
        self.treeview.column("Pickup Date", width=150)
        self.treeview.column("Pickup Time", width=150)
        self.treeview.column("Status", width=150)

        # this is to treeview
        self.treeview.place(x=10, y=150, width=1200, height=300)
        data = self.fetch_bookingHistory_info()  # this is to Ensure this function returns a list of tuples
        for row in data:
            self.treeview.insert("", "end", values=row)
        
        # this is to Bind 
        self.treeview.bind("<ButtonRelease-1>", self.on_select_bookingHistory)

    def on_select_bookingHistory(self, event):

        selected_item = self.treeview.selection()

        if selected_item:
            selected_values = self.treeview.item(selected_item[0], "values")
            booking_id = selected_values[0]

            driver_info = None
            # this is to Fetch driver 
            driver_info = self.fetch_driver_info(booking_id)

            new_window = Toplevel(self.root)
            new_window.title("Driver Information")
            new_window.geometry("500x500")

            label_register = Label(new_window, text="Driver Information", font=("Times New Roman", 24, "bold"), fg="black")
            label_register.place(x=120, y=50, width=300, height=40)

            labels = ["Driver Name", "Phone Number", "License Number"]
            entries = {}
            y_positions = [150, 200, 250]

            for i, label_text in enumerate(labels):
                label = Label(new_window, text=f"{label_text}:", font=("Times New Roman", 14, "bold"), fg="black", bg=new_window.cget("bg"))
                label.place(x=10, y=y_positions[i], width=200, height=35)

                entry = ttk.Entry(new_window, font=("Times New Roman", 14))
                entry.place(x=220, y=y_positions[i], width=270, height=35)
                entries[label_text] = entry

            if driver_info:
                print(driver_info[1])
                print(driver_info[4])
                print(driver_info[8])
                entries["Driver Name"].insert(0, driver_info[1])
                entries["Phone Number"].insert(0, driver_info[4])
                entries["License Number"].insert(0, driver_info[8])

            for entry in entries.values():
                entry.config(state="readonly")


    def fetch_bookingHistory_info(self):
        try:
            connection = MyConn.connect(
                host="localhost",
                user="root",
                password="9828807288",
                database="tbs"
            )
            my_cursor = connection.cursor()
            query = "SELECT id, pick_up_address, drop_off_address, pick_up_date, pick_up_time, status FROM bookings WHERE customer_id = %s"
            my_cursor.execute(query, (Global.id,))
            rows = my_cursor.fetchall()
            return rows
        except MyConn.Error as e:
            messagebox.showerror("Database Error", f"Error connecting to database: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                my_cursor.close()
                connection.close()

    def fetch_driver_info(self, booking_id):
        try:
            connection = MyConn.connect(
                host="localhost",
                user="root",
                password="9828807288",
                database="tbs"
            )
            my_cursor = connection.cursor()
            
            query = "SELECT * FROM bookings WHERE id = %s"
            my_cursor.execute(query, (booking_id,))
            row = my_cursor.fetchone()
            
            driver_id = None
            if row:
                driver_id = row[7]  
            print("DID->",driver_id)
            
            if driver_id:
                query = f"SELECT * FROM driver_profiles WHERE user_id ={driver_id}"
                my_cursor.execute(query)
                drow = my_cursor.fetchone()
                
                if drow:
                    print("Data->",drow)
                    return drow
            
            return None
        except MyConn.Error as e:
            messagebox.showerror("Database Error", f"Error fetching driver details: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                my_cursor.close()
                connection.close()

    def backButton(self):
            self.clearScreen()
            from customerDash import cusDashboard 
            cusDashboard(self.root) 

    def clearScreen(self):
        for widget in self.root.winfo_children():
            widget.destroy()



    ################################################# customer_logout #################################################
    def customer_logout(self):
        # this is to Confirm logout
        response = messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?")
        if response: 
            self.clearScreen()
            from customerLogin import Login_Window
            Login_Window(self.root)  

    def clearScreen(self):
        for widget in self.root.winfo_children():
            widget.destroy()



    ################################################# change_password_customer #################################################
    def change_password_customer(self):
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

        #this is to  Validate input
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
    app = cusDashboard(root)
    root.mainloop()
