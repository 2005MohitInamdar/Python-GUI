import tkinter as tk
import random
import string

def gen_password():

    len=int(entry.get())


    char=string.ascii_letters

    if digi.get():
        char+=string.digits
    if specialchars.get():
        char+=string.punctuation
    if alpha.get():
        char += string.ascii_letters
    passwd=''.join(random.choice(char) for x in range(len))

    pass_displ.config(text="The Generated Password is: "+passwd)


root=tk.Tk()
root.title("Password Generator")
root.geometry("600x250")

frame1=tk.Frame(root)


label=tk.Label(frame1, text="Enter the length of the Password to be generated:")
label.grid(row=0 , column=1 , padx=5 , pady=5)

entry=tk.Entry(frame1)
entry.grid(row=0 , column=2 , padx=5 , pady=5)



digi=tk.BooleanVar()


specialchars=tk.BooleanVar()

alpha = tk.BooleanVar()

digi_box=tk.Checkbutton(frame1 , text="Digits",font=("Arial", 14), variable=digi)
digi_box.grid(row=1 , column=0 , padx=3 , pady=3)

speci_chars_box=tk.Checkbutton(frame1 , text="Special Characters" ,font=("Arial", 14), variable= specialchars)
speci_chars_box.grid(row=1, column=1, padx=3, pady=3)

alpha_box=tk.Checkbutton(frame1 , text="Alphabets" ,font=("Arial", 14), variable= alpha)
alpha_box.grid(row=1, column=2, padx=3, pady=3)
frame1.pack(pady=10)

gen_btnpass=tk.Button(root, text="Generate Password" ,font=("Arial", 14), command=gen_password)
gen_btnpass.pack(pady=10)


frame=tk.Frame(root)

pass_displ=tk.Label(frame, text="", font=("Arial", 18))

frame.pack()
pass_displ.pack(pady=10)

root.mainloop()
