import tkinter as tk
from tkinter import messagebox

def add_task():
    text1 = entry.get()
    if text1:
        list_box.insert(tk.END, text1)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning!", "Write a task to be added")

def del_task():
    try:
        index = list_box.curselection()[0]
        list_box.delete(index)
    except:
        messagebox.showwarning("Warning!", "Select a task to delete")

def edit_task():
    try:
        index = list_box.curselection()[0]
    
        selected_text = list_box.get(index)
        entry.delete(0, tk.END)
        entry.insert(tk.END, selected_text)
        list_box.delete(index)
    except:
        messagebox.showwarning("Warning!", "Select a task to be edited")

def complete_task():
    try:
        index = list_box.curselection()[0]
        list_box.selection_set(index)
        list_box.itemconfig(index,{'bg': 'green', 'fg': 'white'})
    except:
        messagebox.showwarning("Warning!", "Select a task to complete")

def clear_task():
    list_box.delete(0, tk.END)

root = tk.Tk()
root.title("To Do List")
root.geometry("1200x530")

#Frame 1 start consists of a label, Text entry field, and a add task button
frame = tk.Frame(root)
label = tk.Label(frame, text = "Enter your task", font=("Arial", 20))
label.pack(padx = 10,side = "left")
entry = tk.Entry(frame, width=50,  font=("Arial", 20))
entry.pack(padx = 10,side = "left")
add_task_button = tk.Button(frame, text = "Add Task", width = 20, height = 2, font=("Arial", 9), command = add_task)
add_task_button.pack(padx = 10, side = "left")
frame.pack(pady = 30)

#textarea where the added task will be visible
list_box = tk.Listbox(root, height=10, width=75, font=("Arial", 20))
list_box.pack()

#frame 2 consists of remove button and complete task button
frame2 = tk.Frame(root)
remove_task_button = tk.Button(frame2, text = "Delete Task", width = 20, height = 2, font=("Arial", 9), command = del_task)
remove_task_button.pack(side = "left", padx = 20)
edit_task_button = tk.Button(frame2, text = "Edit Task", width = 20, height = 2, font=("Arial", 9), command = edit_task)
edit_task_button.pack(side = "left", padx = 20)
complete_task_button = tk.Button(frame2, text = "Complete Task", width = 20, height = 2, font=("Arial", 9), command = complete_task)
complete_task_button.pack(side = "left", padx = 20)
clearall_task_button = tk.Button(frame2, text = "Clear All", width = 20, height = 2, font=("Arial", 9), command = clear_task)
clearall_task_button.pack(side = "left", padx = 20)
frame2.pack(pady = 20)

root.mainloop()