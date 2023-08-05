from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox
from datetime import datetime
import pymysql

# alt + left mouse click = multiple cursor

# Function Part
def add_student():
    def add_data():
        if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
            messagebox.showerror('Error', 'All fields are required.', parent=add_window)
        else:
            currentdate = time.strftime('%m/%d/%Y')
            currenttime = time.strftime('%H:%M:%S')
            query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(idEntry.get(), nameEntry.get(), phoneEntry.get(), emailEntry.get(),
                                    addressEntry.get(), genderEntry.get(), dobEntry.get(), currentdate, currenttime))
            con.commit()  # Changes committed,
            result = messagebox.askyesno('Success', 'Data Added Successfully. Do you want to clean the form?', parent=add_window)
            if result:  # Clean form
                idEntry.delete(0, END)
                nameEntry.delete(0, END)
                phoneEntry.delete(0, END)
                emailEntry.delete(0, END)
                addressEntry.delete(0, END)
                genderEntry.delete(0, END)
                dobEntry.delete(0, END)
            else:
                pass


    add_window = Toplevel()  # It creates a new top-level window.
    add_window.resizable(0, 0)
    add_window.grab_set()  # Close the window you are working with first, doesn't let you click anywhere else
    idLabel = Label(add_window, text='Student ID', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=20, pady=15, sticky=W)  # sticky W moves text to left side
    idEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, padx=15, pady=10)

    nameLabel = Label(add_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=20, pady=15, sticky=W)
    nameEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, padx=10, pady=15)

    phoneLabel = Label(add_window, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=20, pady=15, sticky=W)
    phoneEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, padx=15, pady=10)

    emailLabel = Label(add_window, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=20, pady=15, sticky=W)
    emailEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, padx=15, pady=10)

    addressLabel = Label(add_window, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=20, pady=15, sticky=W)
    addressEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, padx=15, pady=10)

    genderLabel = Label(add_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=20, pady=15, sticky=W)
    genderEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, padx=15, pady=10)

    dobLabel = Label(add_window, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=20, pady=15, sticky=W)
    dobEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, padx=15, pady=10)

    add_student_Button = ttk.Button(add_window, text='ADD STUDENT', command=add_data)
    add_student_Button.grid(row=7, columnspan=2, pady=10)

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
                    'dob DATE not null, date varchar(60) not null, time varchar(60) not null)'
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
    connectWindow.resizable(0, 0)  # Fixed window size

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
addstudentButton = ttk.Button(leftFrame, text='Add Student', width=20, state=DISABLED, style="Bold.TButton", command=add_student)
addstudentButton.grid(row=1, column=0, pady=20)

searchstudentButton = ttk.Button(leftFrame, text='Search Student', width=20, state=DISABLED, style="Bold.TButton")
searchstudentButton.grid(row=2, column=0, pady=20)

deletestudentButton = ttk.Button(leftFrame, text='Delete Student', width=20, state=DISABLED, style="Bold.TButton")
deletestudentButton.grid(row=3, column=0, pady=20)

updatestudentButton = ttk.Button(leftFrame, text='Update Student', width=20, state=DISABLED, style="Bold.TButton")
updatestudentButton.grid(row=4, column=0, pady=20)

showstudentButton = ttk.Button(leftFrame, text='Show Student', width=20, state=DISABLED, style="Bold.TButton")
showstudentButton.grid(row=5, column=0, pady=20)

exportstudentButton = ttk.Button(leftFrame, text='Export Data', width=20, state=DISABLED, style="Bold.TButton")
exportstudentButton.grid(row=6, column=0, pady=20)

exitButton = ttk.Button(leftFrame, text='Exit', width=20, style="Bold.TButton")
exitButton.grid(row=7, column=0, pady=20)

rightFrame = Frame(root)
rightFrame.place(x=350, y=80, width=820, height=595)

# H/V scroll bar
scrollBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame, orient=VERTICAL)

studentTable = ttk.Treeview(rightFrame, columns=('Student ID', 'Name', 'Phone', 'Email', 'Address'
                                  , 'Gender', 'D.O.B', 'Added Date', 'Added Time'),
                            xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

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

# headings of the table columns will be visible
studentTable.config(show='headings')

root.mainloop()