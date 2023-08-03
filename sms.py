from tkinter import *
import time
import ttkthemes
from tkinter import ttk

# alt + left mouse click = multiple cursor
# Function Part
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
    datetimeLabel.config(text=f'   Date: {date}\nTime: {current_time}')
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
sliderLabel = Label(root, text=s, font=('arial', 26, 'italic bold'), width=30)
sliderLabel.place(x=220, y=0)
slider()

# Style for the button, make it bolded.
style = ttk.Style()
style.configure("Bold.TButton", font=('arial', 9, 'bold'))

# ttk. to apply theme on the button
connectButton = ttk.Button(root, text='Connect database', style="Bold.TButton")
connectButton.place(x=990, y=0)

leftFrame = Frame(root)
leftFrame.place(x=50, y=80, width=300, height=600)

logo_image = PhotoImage(file='students.png')
logo_Label = Label(leftFrame, image=logo_image)
logo_Label.grid(row=0, column=0)


addstudentButton = ttk.Button(leftFrame, text='Add Student', width=20, state=DISABLED, style="Bold.TButton")
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