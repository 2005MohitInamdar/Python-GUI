import tkinter as tk
from tkinter import messagebox
import subprocess
root = tk.Tk()
root.state('zoomed')
root.title("Contact Book")

def toggle_password_visibility():
    current_show = password_entry.cget("show")
    if current_show == "":
        password_entry.config(show="*")
        btm.config(text="Show Password")
    else:
        password_entry.config(show="")
        btm.config(text="Hide Password")

def open_homepage():
    try:
        subprocess.Popen(['python', 'registeration_page.py'])
        root.destroy()
    except FileNotFoundError:
        print("Error: 'homepage.py' not found")

def open_contactboook():
    try:
        if(ID_entry.get() =="mohit inamdar" and password_entry.get() == "12345"):
            subprocess.Popen(['python', 'contact.py'])
            root.destroy()
        elif(ID_entry.get()!= "mohit inamdar"):
            messagebox.showerror("Error", "Incorrect sign-in ID!")
        elif(password_entry.get()!= "12345"):
            messagebox.showerror("Error", "Incorrect Password!")
        else:
            messagebox.showerror(("Enter ID and Password"))


    except FileNotFoundError:
        print("Error: 'contact.py' not found")

label1 = tk.Label(root, text="Enter your login ID and password", font = ("Arial", 18))
label1.pack(pady=30)

frame = tk.Frame(root)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

ID_label = tk.Label(frame, text="Enter ID",padx=20,pady=10, font=("Arial", 16))  #, show="*"..... 'show' attribute hides the entered characters
ID_label.grid(row=0, column=0)

ID_entry = tk.Entry(frame, font=("Arial", 14))  #, show="*"..... 'show' attribute hides the entered characters
ID_entry.grid(row=0, column=1)

password_label = tk.Label(frame, text="Password",padx=20,pady=10, font=("Arial", 16))  #, show="*"..... 'show' attribute hides the entered characters
password_label.grid(row=1, column=0)

password_entry = tk.Entry(frame, font=("Arial", 14))  #, show="*"..... 'show' attribute hides the entered characters
password_entry.grid(row=1, column=1, pady=20)

btm = tk.Button(frame,text = "Toggle", font=("Arial", 12),  command=toggle_password_visibility)
btm.grid(row=1, column=2)


button_login = tk.Button(text = "Login", font=("Arial", 16), command=open_contactboook)
#button_login.grid(row=2, column=0)




frame.pack()
button_login.pack(pady=15)
root.mainloop()




