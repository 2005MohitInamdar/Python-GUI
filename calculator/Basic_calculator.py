import tkinter as tk


class GUI:

    def append_button_text(self, value):
        current_text=self.textarea.get("1.0", "end-1c")

        if value =="=":
            try:
                if "+" in current_text:
                    numbers =current_text.split("+")
                    result= float(numbers[0]) +  float(numbers[1])
                    self.textarea.delete("1.0",tk.END)
                    self.textarea.insert(tk.END,str(result))
                elif "-" in current_text:
                    numbers = current_text.split("-")
                    result = float(numbers[0]) - float(numbers[1])
                    self.textarea.delete("1.0", tk.END)
                    self.textarea.insert(tk.END, str(result))
                elif "*" in current_text:
                    numbers = current_text.split("*")
                    result = float(numbers[0]) *float(numbers[1])
                    self.textarea.delete("1.0", tk.END)
                    self.textarea.insert(tk.END, str(result))
                elif "%" in current_text:
                    numbers = current_text.split("%")
                    result = float(numbers[0])% float(numbers[1])
                    self.textarea.delete("1.0", tk.END)
                    self.textarea.insert(tk.END, str(result))
                elif "/" in current_text:
                    numbers = current_text.split("/")
                    result =float(numbers[0]) / float(numbers[1])
                    self.textarea.delete("1.0", tk.END)
                    self.textarea.insert(tk.END, str(result))

            except ValueError:
                self.textarea.delete("1.0", tk.END)
                self.textarea.insert(tk.END, "Error")
        elif value =="C":
            self.textarea.delete("1.0", tk.END)

        elif value == "D":
            modified_text = current_text[:-1]  # Remove the last character
            self.textarea.delete("1.0", "end-1c")  # Clear the current text in the textarea
            self.textarea.insert("1.0", modified_text)

        else:
            self.textarea.delete("1.0", tk.END)
            self.textarea.insert(tk.END, current_text + value)

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("400x600")

        self.textarea = tk.Text(self.root, height=2, width=50, font=("Arial", 20))

        self.frame = tk.Frame(self.root)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)

        self.button_add = tk.Button(self.frame, text="+", font=("Arial", "18"), height=2,
                                    command=lambda: self.append_button_text(self.button_add["text"]))
        self.button_add.grid(row=0, column=1, sticky=tk.W + tk.E)

        self.button_mod = tk.Button(self.frame, text="%", font=("Arial", "18"), height=2,
                                    command=lambda: self.append_button_text(self.button_mod["text"]))
        self.button_mod.grid(row=0, column=2, sticky=tk.W + tk.E)

        self.button_div = tk.Button(self.frame, text="/", font=("Arial", "18"), height=2,
                                    command=lambda: self.append_button_text(self.button_div["text"]))
        self.button_div.grid(row=0, column=3, sticky=tk.W + tk.E)

        self.button7 = tk.Button(self.frame, text="7", font=("Arial", "18"), height=2,
                                 command=lambda: self.append_button_text(self.button7["text"]))
        self.button7.grid(row=1, column=0, sticky=tk.W + tk.E)

        self.button8 = tk.Button(self.frame, text="8", font=("Arial", "18"), height=2,
                                 command=lambda: self.append_button_text(self.button8["text"]))
        self.button8.grid(row=1, column=1, sticky=tk.W + tk.E)

        self.button9 = tk.Button(self.frame, text="9", font=("Arial", "18"), height=2,
                                 command=lambda: self.append_button_text(self.button9["text"]))
        self.button9.grid(row=1, column=2, sticky=tk.W + tk.E)

        self.button_mul = tk.Button(self.frame, text="*", font=("Arial", "18"), height=2,
                                    command=lambda: self.append_button_text(self.button_mul["text"]))
        self.button_mul.grid(row=1, column=3, sticky=tk.W + tk.E)

        self.button4 = tk.Button(self.frame, text="4", font=("Arial", "18"), height=2,
                                 command=lambda: self.append_button_text(self.button4["text"]))
        self.button4.grid(row=2, column=0, sticky=tk.W + tk.E)

        self.button5 = tk.Button(self.frame, text="5", font=("Arial", "18"), height=2,
                                 command=lambda: self.append_button_text(self.button5["text"]))
        self.button5.grid(row=2, column=1, sticky=tk.W + tk.E)

        self.button6 = tk.Button(self.frame, text="6", font=("Arial", "18"), height=2,
                                 command=lambda: self.append_button_text(self.button6["text"]))
        self.button6.grid(row=2, column=2, sticky=tk.W + tk.E)

        self.button_sub = tk.Button(self.frame, text="-", font=("Arial", "18"), height=2,
                                    command=lambda: self.append_button_text(self.button_sub["text"]))
        self.button_sub.grid(row=2, column=3, sticky=tk.W + tk.E)

        self.button1 = tk.Button(self.frame, text="1", font=("Arial", "18"), height=2,
                                 command=lambda: self.append_button_text(self.button1["text"]))
        self.button1.grid(row=3, column=0, sticky=tk.W + tk.E)

        self.button2 = tk.Button(self.frame, text="2", font=("Arial", "18"), height=2,
                                 command=lambda: self.append_button_text(self.button2["text"]))
        self.button2.grid(row=3, column=1, sticky=tk.W + tk.E)

        self.button3 = tk.Button(self.frame, text="3", font=("Arial", "18"), height=2,
                                 command=lambda: self.append_button_text(self.button3["text"]))
        self.button3.grid(row=3, column=2, sticky=tk.W + tk.E)

        self.button_delete_1 = tk.Button(self.frame, text="D", font=("Arial", "18"), height=2,
                                         command=lambda: self.append_button_text(self.button_delete_1["text"]))
        self.button_delete_1.grid(row=3, column=3, sticky=tk.W + tk.E)

        self.button_dot = tk.Button(self.frame, text=".", font=("Arial", "18"), height=2,
                                    command=lambda: self.append_button_text(self.button_dot["text"]))
        self.button_dot.grid(row=4, column=0, sticky=tk.W + tk.E)

        self.button0 = tk.Button(self.frame, text="0", font=("Arial", "18"), height=2,
                                 command=lambda: self.append_button_text(self.button0["text"]))
        self.button0.grid(row=4, column=1, sticky=tk.W + tk.E)

        self.button_clear = tk.Button(self.frame, text="C", font=("Arial", "18"), height=2,
                                      command=lambda: self.append_button_text(self.button_clear["text"]))
        self.button_clear.grid(row=4, column=2, sticky=tk.W + tk.E)

        self.button_equals = tk.Button(self.frame, text="=", font=("Arial", "18"), height=2,
                                       command=lambda: self.append_button_text(self.button_equals["text"]))
        self.button_equals.grid(row=4, column=3, sticky=tk.W + tk.E)

        self.textarea.pack(fill=tk.X, padx=30, pady=50)
        self.frame.pack(fill=tk.X, padx=30)
        self.root.mainloop()


GUI()
