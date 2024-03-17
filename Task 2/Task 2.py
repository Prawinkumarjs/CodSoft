# Task 2 Simple Calculator

from tkinter import *

# for label and height and width of calc

calc = Tk()
calc.title("Calculator")   # title
calc.geometry('335x520')   # dimension like height and width of calculator
calc.config(bg="Black")   # background color

expression = " "         # a variable assign to store the value and display it


def show(key):                               # function used to showcase the expression what we type or touch
    global expression
    expression = expression + str(key)
    text_box.config(text=expression)


def clear():                              # function used for clear the screen
    global expression
    expression = ""
    text_box.config(text=expression)


def evaluate():                          # function used for calculate  a value
    global expression
    result = ""
    if expression != "":
        try:
            result = eval(expression)              # inbuilt function in python for evaluation
            if result == 7:
                print("Thala for a reason")
        except:
            result = "Error"
    text_box.config(text=result)

# button and its  style and function


text_box = Label(calc, text='', width='25', height='2', font=("Arial", 28), bg="white")
text_box.place(x=0, y=0)

# first row

btn_c = Button(calc, command=lambda:clear(), text='C', width=3, height=1, font=("Arial", 30), bg="#FFA500")
btn_c.place(x=0, y=95)
btn_per = Button(calc, command=lambda: show('%'), text='%', width=3, height=1, font=("Arial", 30), bg='#357EC7')
btn_per.place(x=85, y=95)
btn_div = Button(calc, command=lambda: show('/'), text='/', width=3, height=1, font=("Arial", 30), bg='#357EC7')
btn_div.place(x=170, y=95)
btn_mul = Button(calc, command=lambda: show('*'), text='*', width=3, height=1, font=("Arial", 30), bg='#357EC7')
btn_mul.place(x=255, y=95)

# second row

btn_7 = Button(calc, command=lambda: show('7'), text='7', width=3, height=1, font=("Arial", 30), bg='white')
btn_7.place(x=0, y=180)
btn_8 = Button(calc, command=lambda: show('8'), text='8', width=3, height=1, font=("Arial", 30), bg='white')
btn_8.place(x=85, y=180)
btn_9 = Button(calc,command=lambda: show('9'), text='9', width=3, height=1, font=("Arial", 30), bg='white')
btn_9.place(x=170, y=180)
btn_sub = Button(calc,command=lambda: show('-'), text='-', width=3, height=1, font=("Arial", 30), bg='#357EC7')
btn_sub.place(x=255, y=180)

# third row

btn_4 = Button(calc, command=lambda: show('4'), text='4', width=3, height=1, font=("Arial", 30), bg='white')
btn_4.place(x=0, y=265)
btn_5 = Button(calc, command=lambda: show('5'), text='5', width=3, height=1, font=("Arial", 30), bg='white')
btn_5.place(x=85, y=265)
btn_6 = Button(calc, command=lambda: show('6'), text='6', width=3, height=1, font=("Arial", 30), bg='white')
btn_6.place(x=170, y=265)
btn_add = Button(calc, command=lambda: show('+'), text='+', width=3, height=1, font=("Arial", 30), bg='#357EC7')
btn_add.place(x=255, y=265)

# fourth row

btn_1 = Button(calc, command=lambda: show('1'), text='1', width=3, height=1, font=("Arial", 30), bg='white')
btn_1.place(x=0, y=350)
btn_2 = Button(calc, command=lambda: show('2'), text='2', width=3, height=1, font=("Arial", 30), bg='white')
btn_2.place(x=85, y=350)
btn_3 = Button(calc,command=lambda: show('3'), text='3', width=3, height=1, font=("Arial", 30), bg='white')
btn_3.place(x=170, y=350)
btn_eq = Button(calc,command=lambda: evaluate(), text='=', width=3, height=3, font=("Arial", 30), bg='#357EC7')
btn_eq.place(x=255, y=350)

# fifth row

btn_0 = Button(calc, command=lambda: show('0'), text='0', width=3, height=1, font=("Arial", 30), bg='white')
btn_0.place(x=0, y=435)
btn_open = Button(calc, command=lambda: show('('), text='(', width=3, height=1, font=("Arial", 30), bg='white')
btn_open.place(x=85, y=435)
btn_close = Button(calc, command=lambda: show(')'), text=')', width=3, height=1, font=("Arial", 30), bg='white')
btn_close.place(x=170, y=435)


calc.mainloop()
