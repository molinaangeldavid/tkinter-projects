import os
from tkinter import *
from tkinter import messagebox
from generate_password import Generatepass

BLUE = '#35589A'
HEADER = 'WEBSITE | USERNAME | PASSWORD\n'
FILE_EXISTS = os.path.isfile('passwords.txt')
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
password_account = Generatepass()


def put_password():
    my_pass = password_account.generate_pass()
    if len(input_password.get()) > 0:
        input_password.delete(0,END)
        input_password.insert(0,my_pass)
    else:    
        input_password.insert(0,my_pass)
    


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    
    my_website = input_website.get()
    my_username = input_username.get()
    my_password = input_password.get()
    
    if len(my_website) == 0 or len(my_username) == 0 or len(my_password) == 0:
        messagebox.showerror(title='Error!',message='Don\'t left it empty boxes')
    else:    
        is_ok = messagebox.askokcancel(title='Validate inputs',message=f'This are your inputs:\nWebsite: {my_website}\nUsername: {my_username}\nPassword: {my_password}')

        if is_ok == True:
            with open('passwords.txt','a')as password:
                password.write(f'Website: {my_website} | Username: {my_username} | Password: {my_password}\n')
                input_website.delete(0,END)
                input_username.delete(0,END)
                input_password.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title('Password Manage')
screen.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
image_password = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=image_password)
canvas.grid(row=0,column=1)

website = Label(text='Website:')
website.grid(row=1,column=0,pady=5)

input_website = Entry(highlightthickness=2,highlightcolor=BLUE,width=52)
input_website.grid(row=1,column=1,columnspan=2)
input_website.insert(0,'twitter')

email_username = Label(text='Username / Email:')
email_username.grid(row=2,column=0,pady=5)

input_username = Entry(highlightthickness=2,highlightcolor=BLUE,width=52)
input_username.grid(row=2,column=1,columnspan=2)
input_username.insert(0,'email@gmail.com')

password = Label(text='Password:')
password.grid(row=3,column=0,pady=5)

input_password = Entry(highlightthickness=2,highlightcolor=BLUE,width=33)
input_password.grid(row=3,column=1)

generate_password = Button(text='Generate Password',command=put_password)
generate_password.grid(row=3,column=2)

add_account = Button(text='Add',width=45,command=save_password)
add_account.grid(row=4,column=1,columnspan=2,pady=10)


screen.mainloop()
