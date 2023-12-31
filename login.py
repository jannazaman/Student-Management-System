from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    # Check if username or password is empty
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Both username and password are required fields.')
    # Check if the entered username and password are correct
    elif usernameEntry.get() == 'Janna' and passwordEntry.get() == '12345':
        # Show a successful login message
        messagebox.showinfo('Approved', 'Welcome! Login Successful.')
        # Close the login window when successful and open another window (sms.py)
        window.destroy()
        import sms
    else:
        # Show an error message for invalid credentials
        messagebox.showerror('Invalid Credentials', 'Please enter correct username and password.')

window = Tk()
# Width & Height of window (+0+0 is dist from x & y-axis)
window.geometry('1280x700+0+0')
window.title('Login System')
# Disable maximize feature
window.resizable(False, False)

backgroundImage = ImageTk.PhotoImage(file='bg.png')
bgLabel = Label(window, image=backgroundImage)
bgLabel.place(x=0, y=0)

loginFrame = Frame(window, bg='azure3')
loginFrame.place(x=400, y=150)

logoImage = PhotoImage(file='logo.png')
logoLabel = Label(loginFrame, image=logoImage, bg='azure3')
logoLabel.grid(row=0, column=0, columnspan=2, pady=5)

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
