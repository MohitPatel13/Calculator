import tkinter as tk
from tkinter import *


window = tk.Tk()
window.title('Calculator')
frame = LabelFrame(window)
frame.pack(padx=1, pady=1)
output = Label(frame, text="1", background="light grey")
output.config(height=4,width=32)
output.grid(row=0,column=0,columnspan=4, sticky="NSEW")

def check_out_empty():
    if output.cget("text") == "0":
        empty_out = True
    else:
        empty_out = False
    return empty_out


def clear_button():
    output.config(text="0")
def seven_button():
    if check_out_empty():
        output.config(text="7")
    else:
        output.config(text=output.cget("text")+"7")
def four_button():
    if check_out_empty():
        output.config(text="4")
    else:
        output.config(text=output.cget("text")+"4")
def one_button():
    if check_out_empty():
        output.config(text="1")
    else:
        output.config(text=output.cget("text")+"1")
def eight_button():
    if check_out_empty():
        output.config(text="8")
    else:
        output.config(text=output.cget("text")+"8")
def five_button():
    if check_out_empty():
        output.config(text="5")
    else:
        output.config(text=output.cget("text")+"5")
def two_button():
    if check_out_empty():
        output.config(text="2")
    else:
        output.config(text=output.cget("text")+"2")
def zero_button():
    if check_out_empty():
        output.config(text="0")
    else:
        output.config(text=output.cget("text")+"0")
def nine_button():
    if check_out_empty():
        output.config(text="9")
    else:
        output.config(text=output.cget("text")+"9")
def six_button():
    if check_out_empty():
        output.config(text="6")
    else:
        output.config(text=output.cget("text")+"6")
def three_button():
    if check_out_empty():
        output.config(text="3")
    else:
        output.config(text=output.cget("text")+"3")
def decimal_button():
    if check_out_empty():
        output.config(text="0.")
    else:
        output.config(text=output.cget("text")+".")

clear = Button(frame, text="Clear", command=clear_button)
clear.config(height=4, width=8)
clear.grid(row=1, column=0, sticky="NSEW")
seven = Button(frame, text="7")
seven.config(height=4,width=8, command=seven_button)
seven.grid(row=2, column=0, sticky="NSEW")
four = Button(frame, text="4", command=four_button)
four.config(height=4,width=8)
four.grid(row=3, column=0, sticky="NSEW")
one = Button(frame, text="1", command=one_button)
one.config(height=4,width=8)
one.grid(row=4, column=0, sticky="NSEW")
posneg = Button(frame, text="+/-")
posneg.config(height=4, width=8)
posneg.grid(row=1, column=1, columnspan=2, sticky="NSEW")
eight = Button(frame, text="8", command=eight_button)
eight.config(height=4, width=8)
eight.grid(row=2, column=1, sticky="NSEW")
five = Button(frame, text="5", command=five_button)
five.config(height=4, width=8)
five.grid(row=3, column=1, sticky="NSEW")
two = Button(frame, text="2", command=two_button)
two.config(height=4, width=8)
two.grid(row=4, column=1, sticky="NSEW")
zero = Button(frame, text="0", command=zero_button)
zero.config(height=4,width=16)
zero.grid(row=5,column=0,columnspan=2, sticky="NSEW")
nine = Button(frame, text="9", command=nine_button)
nine.config(height=4, width=8)
nine.grid(row=2, column=2, sticky="NSEW")
six = Button(frame, text="6", command=six_button)
six.config(height=4, width=8)
six.grid(row=3, column=2, sticky="NSEW")
three = Button(frame, text="3", command=three_button)
three.config(height=4, width=8)
three.grid(row=4, column=2, sticky="NSEW")
decimal = Button(frame, text=".", command=decimal_button)
decimal.config(height=4,width=8)
decimal.grid(row=5, column=2, sticky="NSEW")
divide = Button(frame, text="÷")
divide.config(height=4, width=8)
divide.grid(row=1, column=3, sticky="NSEW")
multiply = Button(frame, text ="×")
multiply.config(height=4, width=8)
multiply.grid(row=2, column=3, sticky="NSEW")
minus = Button(frame, text ="-")
minus.config(height=4, width=8)
minus.grid(row=3, column=3, sticky="NSEW")
plus = Button(frame, text ="+")
plus.config(height=4, width=8)
plus.grid(row=4, column=3, sticky="NSEW")
equals = Button(frame, text ="=")
equals.config(height=4, width=8)
equals.grid(row=5, column=3, sticky="NSEW")




tk.mainloop()
