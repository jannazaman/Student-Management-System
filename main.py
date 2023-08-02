from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Both username and password are required fields.')
    elif usernameEntry.get() == 'Janna' and passwordEntry.get() == '12345':
        messagebox.showinfo('Login Successful', 'Welcome!')
    else:
        messagebox.showerror('Invalid Credentials', 'Please enter correct username and password.')

window = Tk()

# Width & Height of window (+0+0 is dist from x & y-axis)
window.geometry('1280x700+0+0')
# Disable maximize feature
window.resizable(False, False)

backgroundImage = ImageTk.PhotoImage(file='bg.png')
bgLabel = Label(window, image=backgroundImage)
bgLabel.place(x=0, y=0)

loginFrame = Frame(window, bg='azure3')
loginFrame.place(x=400, y=150)

logoImage = PhotoImage(file='logo.png')
logoLabel = Label(loginFrame, image=logoImage)
logoLabel.grid(row=0, column=0, columnspan=2)

usernameImage = PhotoImage(file='user.png')
usernameLabel = Label(loginFrame, image=usernameImage, text='Username', compound=LEFT
                      , font=('times new roman', 20, 'bold'), bg='azure3')
usernameLabel.grid(row=1, column=0, pady=10, padx=10)

usernameEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5, fg='medium aquamarine')
usernameEntry.grid(row=1, column=1, pady=10, padx=10)


passwordImage = PhotoImage(file='password.png')
passwordLabel = Label(loginFrame, image=passwordImage, text='Password', compound=LEFT
                      , font=('times new roman', 20, 'bold'), bg='azure3')
passwordLabel.grid(row=2, column=0, pady=10, padx=10)

passwordEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5, fg='medium aquamarine')
passwordEntry.grid(row=2, column=1, pady=10, padx=10)

loginButton = Button(loginFrame, text='Login', font=('times new roman', 15, 'bold'), width=12
                     , fg='white', bg='cadet blue', activebackground='cadet blue'
                     , activeforeground='white', cursor='hand2', command=login)
loginButton.grid(row=3, column=1, pady=10)

# .mainloop will keep window on loop, so we can see it continuously
window.mainloop()