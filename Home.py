import tkinter as tk
from tkinter import *
import re


window = tk.Tk()
window.title('Calculator')
frame = LabelFrame(window)
frame.pack(padx=1, pady=1)
output = Label(frame, text="0", background="light grey")
output.config(height=4,width=32)
output.grid(row=0,column=0,columnspan=4, sticky="NSEW")

dec_used = False
minus_used = False

def check_out_empty():
    if output.cget("text") == "0":
        empty_out = True
    else:
        empty_out = False
    return empty_out
def check_out_neg_empty():
    if output.cget("text") == "-0":
        empty_neg_out = True
    else:
        empty_neg_out = False
    return empty_neg_out
def prev_operator():
    if output.cget("text")[-1] in ["/", "*", "+", "-"]:
        return True
    else:
        return False
def operator_zero():
    if len(output.cget("text"))>=2:
        if output.cget("text")[-2] in ["/", "*", "+", "-"] and output.cget("text")[-1] == "0":
            return True
        else:
            return False
    else:
        return False

def clear_button():
    output.config(text="0")
    clear.config(text="AC")
    global dec_used
    dec_used = False
def seven_button():
    if check_out_empty():
        output.config(text="7")
    elif check_out_neg_empty():
        output.config(text="-7")
    elif operator_zero():
        output.config(text=output.cget("text")[:-1]+"7")
    else:
        output.config(text=output.cget("text")+"7")
    clear.config(text="C")
def four_button():
    if check_out_empty():
        output.config(text="4")
    elif check_out_neg_empty():
        output.config(text="-4")
    elif operator_zero():
        output.config(text=output.cget("text")[:-1]+"4")
    else:
        output.config(text=output.cget("text")+"4")
    clear.config(text="C")
def one_button():
    if check_out_empty():
        output.config(text="1")
    elif check_out_neg_empty():
        output.config(text="-1")
    elif operator_zero():
        output.config(text=output.cget("text")[:-1]+"1")
    else:
        output.config(text=output.cget("text")+"1")
    clear.config(text="C")
def eight_button():
    if check_out_empty():
        output.config(text="8")
    elif check_out_neg_empty():
        output.config(text="-8")
    elif operator_zero():
        output.config(text=output.cget("text")[:-1]+"8")
    else:
        output.config(text=output.cget("text")+"8")
    clear.config(text="C")
def five_button():
    if check_out_empty():
        output.config(text="5")
    elif check_out_neg_empty():
        output.config(text="-5")
    elif operator_zero():
        output.config(text=output.cget("text")[:-1]+"5")
    else:
        output.config(text=output.cget("text")+"5")
    clear.config(text="C")
def two_button():
    if check_out_empty():
        output.config(text="2")
    elif check_out_neg_empty():
        output.config(text="-2")
    elif operator_zero():
        output.config(text=output.cget("text")[:-1]+"2")
    else:
        output.config(text=output.cget("text")+"2")
    clear.config(text="C")
def zero_button():
    if check_out_empty():
        output.config(text="0")
    elif not output.cget("text")[-1] == "0" or dec_used:
        output.config(text=output.cget("text")+"0")
def nine_button():
    if check_out_empty():
        output.config(text="9")
    elif check_out_neg_empty():
        output.config(text="-9")
    elif operator_zero():
        output.config(text=output.cget("text")[:-1]+"9")
    else:
        output.config(text=output.cget("text")+"9")
    clear.config(text="C")
def six_button():
    if check_out_empty():
        output.config(text="6")
    elif check_out_neg_empty():
        output.config(text="-6")
    elif operator_zero():
        output.config(text=output.cget("text")[:-1]+"6")
    else:
        output.config(text=output.cget("text")+"6")
    clear.config(text="C")
def three_button():
    if check_out_empty():
        output.config(text="3")
    elif check_out_neg_empty():
        output.config(text="-3")
    elif operator_zero():
        output.config(text=output.cget("text")[:-1]+"3")
    else:
        output.config(text=output.cget("text")+"3")
    clear.config(text="C")
def decimal_button():
    global dec_used
    if check_out_empty():
        output.config(text="0.")
    elif not dec_used and not prev_operator():
        output.config(text=output.cget("text")+".")
    dec_used = True

def posneg_button():
    if check_out_empty():
        output.config(text="-0")
    operators = ["/", "*", "+", "-"]
    oper_in = False
    i= len(output.cget("text"))-1
    while output.cget("text")[i] not in operators:
        #print(i)
        if i-1 != -1:
            i -= 1
        if i == 0:
            oper_in = False
            break
        else:
            oper_in = True
    if oper_in:
        if output.cget("text")[i] == "-":
            if not minus_used:
                output.config(text=output.cget("text")[:i] + output.cget("text")[i+1:])
            else:
                if output.cget("text")[i] == "-" and output.cget("text")[i-1] == "-":
                    output.config(text=output.cget("text")[:i] + output.cget("text")[i + 1:])
                else:
                    output.config(text=output.cget("text")[:i + 1] + "-" + output.cget("text")[i + 1:])
        else:
            output.config(text=output.cget("text")[:i+1] + "-" + output.cget("text")[i+1:])


    else:
        if output.cget("text")[0] == "-":
            output.config(text=output.cget("text")[1:])
        else:
            output.config(text="-"+output.cget("text"))

def divide_button():
    global dec_used, minus_used
    if check_out_empty():
        output.config(text="0/")
    elif check_out_neg_empty():
        output.config(text="-0/")
    elif not output.cget("text")[-1] == "/" and not prev_operator():
        output.config(text=(output.cget("text")+"/"))
        dec_used = False
        minus_used = False
def multiply_button():
    global dec_used, minus_used
    if check_out_empty():
        output.config(text="0*")
    elif check_out_neg_empty():
        output.config(text="-0*")
    elif not output.cget("text")[-1] == "*" and not prev_operator():
        output.config(text=(output.cget("text")+"*"))
        dec_used = False
        minus_used = False
def minus_button():
    global dec_used
    global minus_used
    if check_out_empty():
        output.config(text="0-")
        minus_used = True
    elif check_out_neg_empty():
        output.config(text="-0-")
        minus_used = True
    elif not output.cget("text")[-1] == "-" and not prev_operator():
        output.config(text=(output.cget("text")+"-"))
        dec_used = False
        minus_used = True

def plus_button():
    global dec_used, minus_used
    if check_out_empty():
        output.config(text="0+")
    elif check_out_neg_empty():
        output.config(text="-0+")
    elif not output.cget("text")[-1] == "+" and not prev_operator():
        output.config(text=(output.cget("text")+"+"))
        dec_used = False
        minus_used = False

def equals_button():
    out_list = re.split(r'([^.0-9])', str(output.cget("text")))
    out_list = list(filter(None, out_list))
    print(out_list)
    neg_first = False
    if out_list[0] == "-":
        neg_first = True
    if not neg_first:
        running_sum = float(out_list[0])
    else:
        running_sum = -float(out_list[1])

    for item in out_list[1:]:
        if item == "/":
            # print(running_sum)
            if out_list[out_list.index(item)+1] == "-":
                running_sum = float(running_sum)/-float(out_list[out_list.index(item)+2])
            else:
                running_sum = float(running_sum)/float(out_list[out_list.index(item)+1])
            # print(float(out_list[out_list.index(item)+1]))
            # print(running_sum)
        elif item == "*":
            if out_list[out_list.index(item)+1] == "-":
                running_sum = float(running_sum)*-float(out_list[out_list.index(item)+2])
            else:
                running_sum = float(running_sum)*float(out_list[out_list.index(item)+1])

        elif item == "+":
            if out_list[out_list.index(item)+1] == "-":
                running_sum = float(running_sum)+-float(out_list[out_list.index(item)+2])
            else:
                running_sum = float(running_sum)+float(out_list[out_list.index(item)+1])
        elif item == "-" and ((out_list[out_list.index(item)-1]) not in ["/", "*", "+"]):
            running_sum = float(running_sum)-float(out_list[out_list.index(item)+1])

    output.config(text=str(running_sum))
    #operators = ["/", "*", "+", "-"]
    # i = 0
    # running_sum = float(0)
    # while output.cget("text")[i] is not None:
    #     if output.cget("text")[i] in operators:
    #         running_sum = float(output.cget("text")[:i])
    #     i += 1
    # m = 0
    # while output.cget("text")[m] is not None:
    #     if output.cget("text")[m] in operators:
    #         if output.cget("text")[m] == "/":
    #             running_sum = running_sum/output.cget("text")[m+1]
    #         elif output.cget("text")[m] == "*":
    #             running_sum = running_sum*output.cget("text")[m+1]
    #         elif output.cget("text")[m] == "+":
    #             running_sum = running_sum+output.cget("text")[m+1]
    #         elif output.cget("text")[m] == "-":
    #             running_sum = running_sum-output.cget("text")[m+1]
    #     m += 1
    # output.config(text=running_sum)







clear = Button(frame, text="AC", command=clear_button)
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
posneg = Button(frame, text="+/-", command=posneg_button)
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
divide = Button(frame, text="÷", command=divide_button)
divide.config(height=4, width=8)
divide.grid(row=1, column=3, sticky="NSEW")
multiply = Button(frame, text="×", command=multiply_button)
multiply.config(height=4, width=8)
multiply.grid(row=2, column=3, sticky="NSEW")
minus = Button(frame, text="-", command=minus_button)
minus.config(height=4, width=8)
minus.grid(row=3, column=3, sticky="NSEW")
plus = Button(frame, text="+", command=plus_button)
plus.config(height=4, width=8)
plus.grid(row=4, column=3, sticky="NSEW")
equals = Button(frame, text="=", command=equals_button)
equals.config(height=4, width=8)
equals.grid(row=5, column=3, sticky="NSEW")




tk.mainloop()
