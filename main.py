import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)
root.geometry("300x300+50+50")

# Create a function for each button
def zero():
    entry.insert(tk.END, "0")

def one():
    entry.insert(tk.END, "1")

def two():
    entry.insert(tk.END, "2")

def three():
    entry.insert(tk.END, "3")

def four():
    entry.insert(tk.END, "4")

def five():
    entry.insert(tk.END, "5")

def six():
    entry.insert(tk.END, "6")

def seven():
    entry.insert(tk.END, "7")

def eight():
    entry.insert(tk.END, "8")

def nine():
    entry.insert(tk.END, "9")

def left_bracket():
    entry.insert(tk.END, "(")

def right_bracket():
    entry.insert(tk.END, ")")

def clear():
    entry.delete(0, tk.END)

def delete():
    entry.delete(len(entry.get()) - 1)

def divide():
    entry.insert(tk.END, "/")

def multiply():
    entry.insert(tk.END, "x")

def subtract():
    entry.insert(tk.END, "-")

def add():
    entry.insert(tk.END, "+")

def decimal():
    entry.insert(tk.END, ".")

def equals():
    thing_to_be_calculated = entry.get()
    new_thing_to_be_calculated = []
    for i in thing_to_be_calculated:
        if i.lower() == "x":
            new_thing_to_be_calculated.append("*")
        elif i.lower() == "^":
            new_thing_to_be_calculated.append("**")
        elif i.lower() == "(":
            new_thing_to_be_calculated.append("*(")
        else:
            new_thing_to_be_calculated.append(i)
    thing_to_be_calculated = "".join(new_thing_to_be_calculated)
    answer = None
    try:
        answer = eval(thing_to_be_calculated)
    except ZeroDivisionError:
        answer = "e: 0/0 not possible"
    except ArithmeticError:
        answer = "Error"
    except SyntaxError:
        answer = "Error"
    except NameError:
        answer = "Error"
    entry.delete(0, tk.END)
    entry.insert(0, answer)
    last_done_label.config(text="Last Done: " + thing_to_be_calculated + " = " + str(answer))

# Button Frame
button_frame = ttk.Label(root, padding=10)
button_frame.grid()



# Creating button instances
entry = tk.Entry(button_frame, width=50)

button_left_bracket = tk.Button(button_frame, text="(", command=left_bracket, width=9, height=2, bg="gray80")
button_right_bracket = tk.Button(button_frame, text=")", command=right_bracket, width=9, height=2, bg="gray80")
button_delete = tk.Button(button_frame, text="DEL", command=delete, width=9, height=2, bg="lightgrey")
button_clear = tk.Button(button_frame, text="C", command=clear, width=9, height=2, bg="darkred", fg="white")
button_one = tk.Button(button_frame, text="1", command=one, width=9, height=2)
button_two = tk.Button(button_frame, text="2", command=two, width=9, height=2)
button_three = tk.Button(button_frame, text="3", command=three, width=9, height=2)
button_divide = tk.Button(button_frame, text="/", command=divide, width=9, height=2, bg="gray80")
button_four = tk.Button(button_frame, text="4", command=four, width=9, height=2)
button_five = tk.Button(button_frame, text="5", command=five, width=9, height=2)
button_six = tk.Button(button_frame, text="6", command=six, width=9, height=2)
button_multiply = tk.Button(button_frame, text="*", command=multiply, width=9, height=2, bg="gray80")
button_seven = tk.Button(button_frame, text="7", command=seven, width=9, height=2)
button_eight = tk.Button(button_frame, text="8", command=eight, width=9, height=2)
button_nine = tk.Button(button_frame, text="9", command=nine, width=9, height=2)
button_subtract = tk.Button(button_frame, text="-", command=subtract, width=9, height=2, bg="gray80")
button_decimal = tk.Button(button_frame, text=".", command=decimal, width=9, height=2, bg="gray75")
button_zero = tk.Button(button_frame, text="0", command=zero, width=9, height=2)
button_add = tk.Button(button_frame, text="+", command=add, width=9, height=2, bg="gray80")
button_equals = tk.Button(button_frame, text="=", command=equals, width=9, height=2, bg="lightgrey")


# Assigning buttons to a grid
entry.grid(row=0, column=0, columnspan=4, sticky="w")
button_left_bracket.grid(row=1, column=0, pady=2)
button_right_bracket.grid(row=1, column=1, pady=2)
button_delete.grid(row=1, column=2, pady=2)
button_clear.grid(row=1, column=3, pady=2)
button_one.grid(row=2, column=0, pady=2)
button_two.grid(row=2, column=1, pady=2)
button_three.grid(row=2, column=2, pady=2)
button_divide.grid(row=2, column=3, pady=2)
button_four.grid(row=3, column=0, pady=2)
button_five.grid(row=3, column=1, pady=2)
button_six.grid(row=3, column=2, pady=2)
button_multiply.grid(row=3, column=3, pady=2)
button_seven.grid(row=4, column=0, pady=2)
button_eight.grid(row=4, column=1, pady=2)
button_nine.grid(row=4, column=2, pady=2)
button_subtract.grid(row=4, column=3, pady=2)
button_decimal.grid(row=5, column=0, pady=2)
button_zero.grid(row=5, column=1, pady=2)
button_add.grid(row=5, column=2, pady=2)
button_equals.grid(row=5, column=3, pady=2)

# Last Frame
last_frame = ttk.Label(root, padding=10)
last_frame.grid()

last_done_label = tk.Label(last_frame, text="Last Done: ")

last_done_label.grid(row=6, column=0, pady=2)

# Run the application
root.mainloop()