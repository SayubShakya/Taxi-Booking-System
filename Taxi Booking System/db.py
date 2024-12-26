import mysql.connector as Connection #This is to import database connector

class Db:

    def __init__(self):
        self.connection = None  # This is connection object
        self.cursor = None  # This is cursor object
        self.host = "localhost"  # This is database host
        self.user = "root"  # This is database user (root)
        self.password = "9828807288"  # This is database password
        self.database = "tbs"  # This is database name

    def connect(self): # This is to connection to the MySQL database
        self.connection = Connection.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        ) 

    def disconnect(self):  # This is to close the connection and cursor if they are open
        if self.connection.is_connected():
            if self.cursor != None:
                self.cursor.close()  # This is to Close the cursor
            self.connection.close()  # This is to Close the connection

    def queryUpdate(self, query): # This is to Execute an update query (insert, update and delete)
        self.connect()  # this is to Connect to the database
        self.cursor = self.connection.cursor()  # this is to Create a cursor
        self.cursor.execute(query)  # This is to  Execute the query
        self.connection.commit()  # This is to  Commit changes to the database

    def queryAll(self, query): # This is to Execute a query and return all results
        self.connect()  # This is to Connect to the database
        self.cursor = self.connection.cursor()  # This is to Create a cursor
        self.cursor.execute(query)  # This is to Execute the query
        return self.cursor.fetchall()  # This is to Return all the rows as a list of tuples
    
    def queryOne(self, query): # This is to Execute a query and return a single result
        self.connect()  # This is to Connect to the database
        self.cursor = self.connection.cursor()  # This is to Create a cursor
        self.cursor.execute(query)  # This is to Execute the query
        return self.cursor.fetchone()  # This is to Return a single row

################################################ Finish ##################################################