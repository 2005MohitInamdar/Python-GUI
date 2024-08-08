import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Expense Tracker")
root.configure(bg="black")
root.geometry("780x400")
#logic to save a file

def show_info():
    try:
        with open("Expense Tracker.txt", "r") as f:
            contents = f.read()
            messagebox.showinfo("File Contents", contents)
    except FileNotFoundError:
        messagebox.showerror("Error", "File 'Expense Tracker.txt' not found")
    except Exception as e:
        messagebox.showerror("Error", str(e))
def save_info():
    try:
        with open("Expense Tracker.txt", "a") as f:
            f.write(f"{entry.get()} : spent on {entry_info.get()}\n")
            entry.delete(0, tk.END)
            entry_info.delete(0, tk.END)
    except:
        messagebox.showwarning("ERROR!", "Message was not added")
#end of logic

#first frame consists of an entry field and a button

frame = tk.Frame(root, bg = "black")

label = tk.Label(frame, text = "Expense Tracker", font = "Arial 30", bg = "black", fg = "white")
label.grid(row = 0, column = 0, pady = 20, columnspan=2)

label_entry = tk.Label(frame, text = "Enter amount", font = "Arial 20", bg = "black", fg = "white")
label_entry.grid(row = 1, column = 0, pady = 20, padx=10)

entry = tk.Entry(frame, width = 30, font = "Arial 20", relief="ridge")
entry.grid(row = 1, column = 1,  pady = 10)

label_info = tk.Label(frame, text = "Where did you spent?", font = "Arial 20", bg = "black", fg = "white")
label_info.grid(row = 2, column = 0, pady = 20, padx=10)

entry_info = tk.Entry(frame, width = 30, font = "Arial 20", relief="ridge")
entry_info.grid(row = 2, column = 1,  pady = 10)

button = tk.Button(frame, text = "Show Info", font = "Arial 20", bg = "black", fg = "white", command = show_info)
button.grid(row = 3, column = 0, pady = 20)

button = tk.Button(frame, text = "Save Info", font = "Arial 20", bg = "black", fg = "white", command = save_info)
button.grid(row = 3, column = 1, pady = 20)

frame.grid()
#end of first frame



root.mainloop()