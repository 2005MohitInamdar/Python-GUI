import tkinter as tk
from tkinter import messagebox
import subprocess

def open_homepage():
    try:
        subprocess.Popen(['python', 'homepage.py'])
        root.destroy()
    except FileNotFoundError:
        print("Error: 'homepage.py' not found")

# Create a list to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        contacts.append((name, phone))
        update_contact_list()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Name and Phone fields cannot be empty!")

# Function to update the contact list
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"Name: {contact[0]}, Phone: {contact[1]}")

# Function to edit a contact
def edit_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        name, phone = contacts[selected_index[0]]
        name_entry.delete(0, tk.END)
        name_entry.insert(0, name)
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, phone)
        delete_contact(selected_index[0])

# Function to delete a contact
def delete_contact(index):
    if index:
        contacts.pop(index[0])
        update_contact_list()

# Create the main window
root = tk.Tk()
root.title("Contact Book")
root.state('zoomed')

frame = tk.Frame(root)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
# Create input fields and labels
name_label = tk.Label(frame, text="Name:", font=("Arial", 16))
name_label.grid(row=0, column=0, padx=10, pady=10)


name_entry = tk.Entry(frame, font=("Arial", 14))
name_entry.grid(row=0, column=1, padx=10, pady=10)

phone_label = tk.Label(frame, text="Phone:", font=("Arial", 16))
phone_label.grid(row=1, column=0, padx=10, pady=10)
phone_entry = tk.Entry(frame, font=("Arial", 14))
phone_entry.grid(row=1, column=1, padx=10, pady=10)

# Create buttons
add_button = tk.Button(frame, text="Add Contact", font=("Arial", 12), command=add_contact)
add_button.grid(row=2, column=0, padx=10, pady=35)

edit_button = tk.Button(frame, text="Edit Contact", font=("Arial", 12), command=edit_contact)
edit_button.grid(row=2, column=1, padx=10, pady=35)

delete_button = tk.Button(frame, text="Delete Contact", font=("Arial", 12), command=lambda: delete_contact(contact_listbox.curselection()))
delete_button.grid(row=2, column=2, padx=10, pady=35)

frame.pack(padx=10, pady=10)
# Create a listbox to display contacts
contact_listbox = tk.Listbox(root, height=10, width=50, font=("Arial", 14))
contact_listbox.pack(pady=10)

back_button = tk.Button(root, text="Back", padx=10, font=("Arial", 12), command=open_homepage)
back_button.pack(padx=80, pady=10)
# Update the contact list initially
update_contact_list()

root.mainloop()
