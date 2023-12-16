import mysql.connector as sqltor

# Establishing a connection to the MySQL database
mycon = sqltor.connect(host="localhost", user="root", passwd="krish8125", database="school")

# Checking if the connection is successful
if mycon.is_connected():
    print('Welcome to School Portal')
    # Creating a cursor to execute SQL queries
    cursor = mycon.cursor()

    # SQL statement to create the 'student' table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS student (
        SchNo INT,
        FirstName VARCHAR(255),
        LastName VARCHAR(255),
        Class INT,
        Section CHAR(1),
        House VARCHAR(255),
        Age INT,
        English INT,
        Computer INT,
        Physics INT,
        Chemistry INT,
        Maths INT,
        TotalMarks INT,
        Percentage INT,
        Grade CHAR(1)
    )
    """

    # Executing the create table query
    cursor.execute(create_table_query)

    # Committing the changes to the database
    mycon.commit()

    # Closing the cursor
    cursor.close()

# Admin Portal function
def admin():
    print(" Welcome to School Admin Portal")
    print("""
          1 for Adding Student Record
          2 for Deleting Student Record
          3 for Search for a Student Record
          4 for Display records of all Students
          5 for Exit""")
    task = input("What task do you like to perform? : ")
    if task == '1':
        add()
    elif task == '2':
        delete()
    elif task == '3':
        search()
    elif task == '4':
        display()
    elif task == '5':
        print("Bye bye!")
    else:
        print("Select the task correctly........")
        admin()

# Teacher Portal function
def teacher():
    print(" Welcome to School Teacher Portal")
    print("""
          1 for Adding Student Marks
          2 for Search for a Student Record
          3 for Display records of all Students
          4 for Exit""")
    task = input("What task do you like to perform? : ")
    if task == '1':
        edit()
    elif task == '2':
        search()
    elif task == '3':
        display()
    elif task == '4':
        print("Bye bye!")
    else:
        print("Select the task correctly........")
        teacher()

# Student Portal function
def student():
    print(" Welcome to School Student Portal")
    print("""
          1 for Checking your Report Card
          2 for exit""")
    task = input("What task do you like to perform? : ")
    if task == '1':
        search()
    elif task == '2':
        print("Bye bye!")
    else:
        print("Select the task correctly........")
        student()

# Function to add student data
def add():
    n = int(input("How many students do you want to add data for: "))
    for i in range(n):
        print("Add data of Student", i + 1)
        schno = int(input("Enter the Scholar No.: "))
        FName = input("Enter First Name: ")
        LName = input("Enter Last Name: ")
        Class = int(input("Enter Class: "))
        Section = input("Enter Section: ").capitalize()
        House = input("Enter House: ").capitalize()
        Age = int(input("Enter Age: "))

        # SQL statement to insert data into the 'student' table
        insert_data_query = """
        INSERT INTO student (SchNo, FirstName, LastName, Class, Section, House, Age)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        # Data to be inserted
        data = (schno, FName, LName, Class, Section, House, Age)

        try:
            # Creating a cursor to execute SQL queries
            cursor = mycon.cursor()

            # Executing the insert data query
            cursor.execute(insert_data_query, data)

            # Committing the changes to the database
            mycon.commit()

            print("Data inserted successfully!")

        except sqltor.Error as e:
            print(f"Error: {e}")
            mycon.rollback()

        finally:
            # Closing the cursor
            cursor.close()

# Function to edit student marks
def edit():
    print("Enter Marks of Student")
    schno = int(input("Enter the Scholar No.: "))
    Eng = int(input("Enter English Marks: "))
    Comp = int(input("Enter Computer Marks: "))
    Phy = int(input("Enter Physics Marks: "))
    Chem = int(input("Enter Chemistry Marks: "))
    Maths = int(input("Enter Maths Marks: "))

    # SQL statement to update student marks in the 'student' table
    update_marks_query = """
    UPDATE student
    SET English = %s, Computer = %s, Physics = %s, Chemistry = %s, Maths = %s
    WHERE SchNo = %s
    """

    # Data to be updated
    data = (Eng, Comp, Phy, Chem, Maths, schno)

    try:
        # Creating a cursor to execute SQL queries
        cursor = mycon.cursor()

        # Executing the update marks query
        cursor.execute(update_marks_query, data)

        # Committing the changes to the database
        mycon.commit()

        print("Marks updated successfully!")

    except sqltor.Error as e:
        print(f"Error: {e}")
        mycon.rollback()

    finally:
        # Closing the cursor
        cursor.close()

# Function to delete a student record
def delete():
    schno = int(input("Enter the Scholar No.: "))

    # SQL statement to delete a student record from the 'student' table
    delete_record_query = """
    DELETE FROM student
    WHERE SchNo = %s
    """

    # Data for deletion
    data = (schno,)

    try:
        # Creating a cursor to execute SQL queries
        cursor = mycon.cursor()

        # Executing the delete record query
        cursor.execute(delete_record_query, data)

        # Committing the changes to the database
        mycon.commit()

        print(f"Record of Student with {schno} Deleted!!")

    except sqltor.Error as e:
        print(f"Error: {e}")
        mycon.rollback()

    finally:
        # Closing the cursor
        cursor.close()

# Function to search for a student record
def search():
    schno = int(input("Enter the Scholar No.: "))

    # SQL statement to search for a student record in the 'student' table
    search_record_query = """
    SELECT * FROM student
    WHERE SchNo = %s
    """

    # Data for search
    data = (schno,)

    try:
        # Creating a cursor to execute SQL queries
        cursor = mycon.cursor()

        # Executing the search record query
        cursor.execute(search_record_query, data)

        # Fetching and printing the search result
        result = cursor.fetchone()
        if result:
            print("Record of Student with", schno)
            print("SchNo:", result[0])
            print("FirstName:", result[1])
            print("LastName:", result[2])
            print("Class:", result[3])
            print("Section:", result[4])
            print("House:", result[5])
            print("Age:", result[6])
            print("English:", result[7])
            print("Computer:", result[8])
            print("Physics:", result[9])
            print("Chemistry:", result[10])
            print("Maths:", result[11])
            print("TotalMarks:", result[12])
            print("Percentage:", result[13])
            print("Grade:", result[14])
        else:
            print(f"No record found for Scholar No. {schno}")

    except sqltor.Error as e:
        print(f"Error: {e}")

    finally:
        # Closing the cursor
        cursor.close()

# Function to display student records
def display():
    print('''
          1 for Display all records
          2 for Display records with filters''')
    n = input("Enter your choice: ")

    if n == '1':
        # SQL statement to display all records from the 'student' table
        display_all_query = """
        SELECT * FROM student
        """

        try:
            # Creating a cursor to execute SQL queries
            cursor = mycon.cursor()

            # Executing the display all query
            cursor.execute(display_all_query)

            # Fetching and printing all records
            results = cursor.fetchall()
            if results:
                for result in results:
                    print("SchNo:", result[0])
                    print("FirstName:", result[1])
                    print("LastName:", result[2])
                    print("Class:", result[3])
                    print("Section:", result[4])
                    print("House:", result[5])
                    print("Age:", result[6])
                    print("English:", result[7])
                    print("Computer:", result[8])
                    print("Physics:", result[9])
                    print("Chemistry:", result[10])
                    print("Maths:", result[11])
                    print("TotalMarks:", result[12])
                    print("Percentage:", result[13])
                    print("Grade:", result[14])
                    print("-------------------------------")
            else:
                print("No records found.")

        except sqltor.Error as e:
            print(f"Error: {e}")

        finally:
            # Closing the cursor
            cursor.close()

    elif n == '2':
        # You can implement filters based on your requirements
        print("RECORDS WITH FILTERS - Not implemented in this example.")

    else:
        print("Select the task correctly........")

# Main loop for user interaction
while True:
    print('''
          1 for Admin
          2 for Teacher
          3 for Student''')
    user_type = input("Please select your user type: ")
    if user_type == '1':
        admin()
        break
    elif user_type == '2':
        teacher()
        break
    elif user_type == '3':
        student()
        break
    else:
        print("Select the user type correctly........")
        print("........Restarting........")

# Closing the database connection after the main loop
mycon.close()