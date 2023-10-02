from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox, filedialog
import pymysql
import pandas

# alt + left mouse click = multiple cursor
# shift + tab = decrease indentation

# Function Part
def iexit():
    result=messagebox.askyesno('Confirm', 'Do you want to exit?')
    if result:  # If you want to exit then destroy main window.
        root.destroy()
    else:
        pass
def export_data():
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    indexing = studentTable.get_children()  # Returns the index of all the rows that we store in variable indexing
    newlist=[]
    # Iterate through the tuple and get the content
    for index in indexing:
        content=studentTable.item(index)
        dataList=content['values']
        newlist.append(dataList)  # New list has all the rows of datalist in a single list
    table = pandas.DataFrame(newlist, columns=['Student ID', 'Name', 'Phone', 'Email', 'Address', 'Gender', 'D.O.B', 'Added Date', 'Added Time'])
    table.to_csv(url, index=False)
    messagebox.showinfo('Success', 'Data is saved successfully.')

def toplevel_field_data(title, button_text, command):
    global idEntry, nameEntry, phoneEntry, emailEntry, addressEntry, genderEntry, dobEntry, alter_window
    alter_window = Toplevel()  # It creates a new top-level window.
    alter_window.title(title)  # Instead of passing title directly, pass title variable
    alter_window.resizable(False, False)
    alter_window.grab_set()  # Close the window you are working with first, doesn't let you click anywhere else
    idLabel = Label(alter_window, text='Student ID', font=('times new roman', 20, 'bold'), fg='midnight blue')
    idLabel.grid(row=0, column=0, padx=20, pady=15, sticky=W)  # sticky=W moves text to left side
    idEntry = Entry(alter_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, padx=15, pady=10)

    nameLabel = Label(alter_window, text='Name', font=('times new roman', 20, 'bold'), fg='midnight blue')
    nameLabel.grid(row=1, column=0, padx=20, pady=15, sticky=W)
    nameEntry = Entry(alter_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, padx=10, pady=15)

    phoneLabel = Label(alter_window, text='Phone', font=('times new roman', 20, 'bold'), fg='midnight blue')
    phoneLabel.grid(row=2, column=0, padx=20, pady=15, sticky=W)
    phoneEntry = Entry(alter_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, padx=15, pady=10)

    emailLabel = Label(alter_window, text='Email', font=('times new roman', 20, 'bold'), fg='midnight blue')
    emailLabel.grid(row=3, column=0, padx=20, pady=15, sticky=W)
    emailEntry = Entry(alter_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, padx=15, pady=10)

    addressLabel = Label(alter_window, text='Address', font=('times new roman', 20, 'bold'), fg='midnight blue')
    addressLabel.grid(row=4, column=0, padx=20, pady=15, sticky=W)
    addressEntry = Entry(alter_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, padx=15, pady=10)

    genderLabel = Label(alter_window, text='Gender', font=('times new roman', 20, 'bold'), fg='midnight blue')
    genderLabel.grid(row=5, column=0, padx=20, pady=15, sticky=W)
    genderEntry = Entry(alter_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, padx=15, pady=10)

    dobLabel = Label(alter_window, text='D.O.B', font=('times new roman', 20, 'bold'), fg='midnight blue')
    dobLabel.grid(row=6, column=0, padx=20, pady=15, sticky=W)
    dobEntry = Entry(alter_window, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, padx=15, pady=10)

    student_Button = ttk.Button(alter_window, text=button_text, command=command)  # Pass variable button_text, command
    student_Button.grid(row=7, columnspan=2, pady=10)

    # Condition for Update Form: if condition is True, then all the selected info will be entered in the entry fields
    if title=='Update Student':
        indexing = studentTable.focus()  # focus() method retrieves the currently selected item (row)
        content = studentTable.item(indexing)  # item(indexing) retrieves the details of that selected item
        listofData = content['values']
        idEntry.insert(0, listofData[0])
        nameEntry.insert(0, listofData[1])
        phoneEntry.insert(0, listofData[2])
        emailEntry.insert(0, listofData[3])
        addressEntry.insert(0, listofData[4])
        genderEntry.insert(0, listofData[5])
        dobEntry.insert(0, listofData[6])

def update_data():
    query = 'update student set name=%s, mobile=%s, email=%s, address=%s, gender=%s, dob=%s, date=%s, time=%s'
    mycursor.execute(query, (nameEntry.get(), phoneEntry.get(), emailEntry.get(), addressEntry.get(),
                             genderEntry.get(), dobEntry.get(), date, current_time, idEntry.get()))
    con.commit()
    messagebox.showinfo('Success', f'ID {idEntry.get()} is modified successfully.', parent=alter_window)
    alter_window.destroy()
    show_student()


def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())  # Delete existing data before new content
    for data in fetched_data:
        studentTable.insert('', END, values=data)

def delete_student():
    indexing = studentTable.focus()  # Get the index of the focused item (row)
    print(indexing)  # Print the index
    if not indexing:  # Check if any row is selected
        messagebox.showwarning('No Selection', 'Please select a student to delete.')
        return
    content = studentTable.item(indexing)
    contentID = content['values'][0]  # Extract the ID - first value from the content

    # Define the SQL query to delete a student based on their ID
    query = 'delete from student where id=%s'
    mycursor.execute(query, contentID)
    # If deleting or adding some data - commit changes
    con.commit()
    messagebox.showinfo('Student Deleted', f'ID {contentID} is deleted successfully.')
    # To see updated rows in the treeview after deletion
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())  # Delete existing data before new content
    for data in fetched_data:
        studentTable.insert('', END, values=data)


def search_data():
    # Select all columns from the student table where the specified column match the search criteria
    query = 'select * from student where id=%s or name=%s or email=%s or phone=%s or address=%s or gender=%s or dob=%s'

    mycursor.execute(query, (idEntry.get(), nameEntry.get(), emailEntry.get(), phoneEntry.get(), 
                             addressEntry.get(), genderEntry.get(), dobEntry.get()))
    # Clear the existing contents of the studentTable widget to prepare for new data
    studentTable.delete(*studentTable.get_children())

    # Store the particular row inside this fetched data
    fetched_data = mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('', END, values=data)


def add_data():
    if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='' or 
    addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
        messagebox.showerror('Error', 'All fields are required.', parent=alter_window)
    else:
        try:
            query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query, (idEntry.get(), nameEntry.get(), phoneEntry.get(), emailEntry.get(),
                                     addressEntry.get(), genderEntry.get(), dobEntry.get(), date,
                                     current_time))
            con.commit()  # Changes committed,
            result = messagebox.askyesno('Confirm', 'Data Added Successfully. Do you want to clean the form?',
                                         parent=alter_window)
            if result:  # Clean form once filled out
                idEntry.delete(0, END)
                nameEntry.delete(0, END)
                phoneEntry.delete(0, END)
                emailEntry.delete(0, END)
                addressEntry.delete(0, END)
                genderEntry.delete(0, END)
                dobEntry.delete(0, END)
            else:
                pass
        except:
            messagebox.showerror('Error', 'ID cannot be repeated.', parent=alter_window)
            return

        query = 'select *from student'  # Student is the table name
        mycursor.execute(query)
        # Fetch all the data returned by the query and store it in 'fetched_data'
        fetched_data = mycursor.fetchall()
        # Clear the existing data in the Treeview widget before populating with new data
        studentTable.delete(studentTable.get.children())
        for data in fetched_data:

            # Treeview object var = studentTable
            studentTable.insert('', END, values=data)


def connect_database():
    def connect():
        global mycursor, con # Can be used in other functions
        try:
            # Connect with mySQL database
            con = pymysql.connect(host=hostEntry.get(), user=usernameEntry.get(), password=passwordEntry.get())
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Invalid Details.', parent=connectWindow)
            return

        # CREATE database
        try:
            query = 'create database studentmanagementsystem'
            # In order to execute queries we will use mycursor
            mycursor.execute(query)
            query = 'use studentmanagementsystem'
            mycursor.execute(query)
            query = 'create table student(id int not null primary key, name varchar(30) not null, phone varchar(10), ' \
                    'email varchar(50) not null, address varchar(100) not null, gender varchar(30) not null, ' \
                    'dob varchar(10), date varchar(60) not null, time varchar(60) not null)'
            mycursor.execute(query)
        except:
            query = 'use studentmanagementsystem'
            mycursor.execute(query)

        messagebox.showinfo('Success', 'Database Connection is successful.', parent=connectWindow)

        # Automatically close the Success window
        connectWindow.destroy()

        # Update the state of the buttons from being disabled to normal when connected to db
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)

    # Use toplevel to create GUI window on top of the main window
    connectWindow = Toplevel()
    connectWindow.grab_set()  # Close one window at a time
    connectWindow.geometry('470x250+730+230')  # Create Window size + Location
    connectWindow.title('Database Connection')  # Create Title
    connectWindow.resizable(False, False)  # Fixed window size

    hostnameLabel = Label(connectWindow, text='Host Name', font=('arial', 20, 'bold'),
                          fg='DeepSkyBlue4')  #fg = font color
    hostnameLabel.grid(row=0, column=0, padx=20)

    hostEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)  #bd = border
    hostEntry.grid(row=0, column=1, padx=30, pady=20)

    usernameLabel = Label(connectWindow, text='Username', font=('arial', 20, 'bold'),
                          fg='DeepSkyBlue3')  #fg = font color
    usernameLabel.grid(row=1, column=0, padx=20)

    usernameEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)  #bd = border
    usernameEntry.grid(row=1, column=1, padx=30, pady=20)

    passwordLabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'),
                          fg='DeepSkyBlue2')  # fg = font color
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)  # bd = border
    passwordEntry.grid(row=2, column=1, padx=30, pady=20)

    connectButton = ttk.Button(connectWindow, text='CONNECT', command=connect)
    connectButton.grid(row=3, columnspan=2)

count = 0
text = ''
def slider():
    global text, count  # In order to modify value inside a function
    if count==len(s): # Restart Header title once it reached the end
        count = 0
        text = ''
    text = text + s[count]
    sliderLabel.config(text=text)
    count+=1 # Go to next char
    sliderLabel.after(400, slider)

def clock():
    global date, current_time
    date = time.strftime('%m/%d/%Y')
    current_time = time.strftime('%H:%M:%S')
    # config method used to update something on this label
    datetimeLabel.config(text=f'   Date: {date}\nTime: {current_time}', fg='DodgerBlue4')
    # Update the seconds after some time, clock function gets called every 1 sec
    datetimeLabel.after(1000, clock)

# GUI PART
root = ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('blue')

root.geometry('1174x680+0+0')
root.title('Student Management System')
root.resizable(0, 0)

datetimeLabel = Label(root, font=('times new roman', 16, 'bold'))
datetimeLabel.place(x=5, y=5)
clock()

s = 'Student Management System'  # s[count] = S when count is 0, its t when count is 1.
sliderLabel = Label(root, text=s, font=('arial', 26, 'italic bold'), width=30, fg='DodgerBlue4')
sliderLabel.place(x=220, y=0)
slider()

# Style for the button, make it bolded.
style = ttk.Style()
style.configure("Bold.TButton", font=('arial', 9, 'bold'))

# ttk. to apply theme on the button
connectButton = ttk.Button(root, text='Connect database', style="Bold.TButton", command=connect_database)
connectButton.place(x=990, y=0)

leftFrame = Frame(root)
leftFrame.place(x=50, y=80, width=300, height=600)

logo_image = PhotoImage(file='students.png')
logo_Label = Label(leftFrame, image=logo_image)
logo_Label.grid(row=0, column=0)

# THE BUTTON TABS
# command used to call function
# lambda function is defining the action to be taken when the button is clicked
addstudentButton = ttk.Button(leftFrame, text='Add Student', width=20, state=DISABLED, style="Bold.TButton", command=lambda :toplevel_field_data('Add Student', 'ADD', add_data))
addstudentButton.grid(row=1, column=0, pady=20)

searchstudentButton = ttk.Button(leftFrame, text='Search Student', width=20, state=DISABLED, style="Bold.TButton", command=lambda :toplevel_field_data('Search Student', 'SEARCH', search_data))
searchstudentButton.grid(row=2, column=0, pady=20)

deletestudentButton = ttk.Button(leftFrame, text='Delete Student', width=20, state=DISABLED, style="Bold.TButton", command=delete_student)
deletestudentButton.grid(row=3, column=0, pady=20)

updatestudentButton = ttk.Button(leftFrame, text='Update Student', width=20, state=DISABLED, style="Bold.TButton", command=lambda :toplevel_field_data('Update Student', 'UPDATE', update_data))
updatestudentButton.grid(row=4, column=0, pady=20)

showstudentButton = ttk.Button(leftFrame, text='Show Student', width=20, state=DISABLED, style="Bold.TButton", command=show_student)
showstudentButton.grid(row=5, column=0, pady=20)

exportstudentButton = ttk.Button(leftFrame, text='Export Data', width=20, state=DISABLED, style="Bold.TButton", command=export_data)
exportstudentButton.grid(row=6, column=0, pady=20)

exitButton = ttk.Button(leftFrame, text='Exit', width=20, style="Bold.TButton", command=iexit)
exitButton.grid(row=7, column=0, pady=20)

rightFrame = Frame(root)
rightFrame.place(x=350, y=80, width=820, height=595)

# H/V scroll bar
scrollBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame, orient=VERTICAL)

studentTable = ttk.Treeview(rightFrame, columns=('Student ID', 'Name', 'Phone', 'Email', 'Address'
                                  , 'Gender', 'D.O.B', 'Added Date', 'Added Time'),
                            xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)
# Define a style for the column headers
style = ttk.Style()
style.configure("Treeview.Heading", borderwidth=1, relief="solid", font=('arial', 13, 'bold'))

# Apply the style to each column header
for column in studentTable['columns']:
    studentTable.heading(column, text=column, anchor=CENTER)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)

# Fill both x and y of this view; Widgets are packed in the order they are created
studentTable.pack(fill=BOTH, expand=1)

studentTable.heading('Student ID', text='Student ID')
studentTable.heading('Name', text='Name')
studentTable.heading('Phone', text='Phone')
studentTable.heading('Email', text='Email')
studentTable.heading('Address', text='Address')
studentTable.heading('Gender', text='Gender')
studentTable.heading('D.O.B', text='D.O.B')
studentTable.heading('Added Date', text='Added Date')
studentTable.heading('Added Time', text='Added Time')

studentTable.column('Student ID', width=130, anchor=CENTER)
studentTable.column('Name', width=150, anchor=CENTER)
studentTable.column('Phone', width=200, anchor=CENTER)
studentTable.column('Email', width=210, anchor=CENTER)
studentTable.column('Address', width=200, anchor=CENTER)
studentTable.column('Gender', width=110, anchor=CENTER)
studentTable.column('D.O.B', width=110, anchor=CENTER)
studentTable.column('Added Date', width=140, anchor=CENTER)
studentTable.column('Added Time', width=140, anchor=CENTER)

style = ttk.Style()
style.configure('Treeview', rowheight=35, font=('arial', 12, 'bold'), foreground='DodgerBlue4', background='alice blue',
                fieldbackground='alice blue')

# headings of the table columns will be visible
studentTable.config(show='headings')

root.mainloop()
