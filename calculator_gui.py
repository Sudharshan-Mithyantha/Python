from tkinter import *
from tkinter import messagebox
import math

root = Tk()
root.title("Simple Calculator")

frame = LabelFrame(root, padx=5, pady=5)

disp = Entry(root, width = 30, borderwidth = 5, font=("Times New Roman",16))
disp.grid(row=0, column=0, ipady = 10, columnspan=5)

def screen(number):
    current = disp.get()
    disp.delete(0, END)
    disp.insert(0, str(current) + str(number))

def click_plus(operator):
    global op
    op = operator
    global f_num
    f_num = int(disp.get())
    disp.delete(0, END)

def Add():
    s_num = int(disp.get())
    disp.delete(0, END)
    if op == "+":
        disp.insert(0, f_num+s_num)
    elif op == "-":
        disp.insert(0, f_num-s_num)
    elif op == "*":
        disp.insert(0, f_num*s_num)
    elif op == "/":
        disp.insert(0, f_num/s_num)
    elif op == "%":
        disp.insert(0, f_num%s_num)
    elif op == "power":
        disp.insert(0, int(math.pow(f_num, s_num)))

    else:
        disp.insert(0, "invalid")

def square_root():
    num = int(disp.get())
    disp.delete(0, END)
    disp.insert(0, float(math.sqrt(num)))

def square():
    num = int(disp.get())
    disp.delete(0, END)
    disp.insert(0, num*num)

def clr_scr():
    disp.delete(0, END)

def quit_pgm():
    response = messagebox.askyesno("Message","Do you really want to exit program?")
    if response == 1:
        root.quit()

button_0 = Button(frame, text="0", padx=40, pady=20, command = lambda: screen(0))
button_1 = Button(frame, text="1", padx=40, pady=20, command = lambda: screen(1))
button_2 = Button(frame, text="2", padx=40, pady=20, command = lambda: screen(2))
button_3 = Button(frame, text="3", padx=40, pady=20, command = lambda: screen(3))
button_4 = Button(frame, text="4", padx=40, pady=20, command = lambda: screen(4))
button_5 = Button(frame, text="5", padx=40, pady=20, command = lambda: screen(5))
button_6 = Button(frame, text="6", padx=40, pady=20, command = lambda: screen(6))
button_7 = Button(frame, text="7", padx=40, pady=20, command = lambda: screen(7))
button_8 = Button(frame, text="8", padx=40, pady=20, command = lambda: screen(8))
button_9 = Button(frame, text="9", padx=40, pady=20, command = lambda: screen(9))
button_plus = Button(frame, text = "+", padx=38, pady=20, command = lambda:click_plus("+"))
button_minus = Button(frame, text = "-", padx=41, pady=20, command = lambda:click_plus("-"))
button_mul = Button(frame, text = "*", padx=40, pady=20, command = lambda:click_plus("*"))
button_div = Button(frame, text = "/", padx=42, pady=20, command = lambda:click_plus("/"))
button_mod = Button(frame, text = "mod", padx = 30, pady=20, command = lambda:click_plus("%"))
button_sqrt = Button(frame, text = "sqrt", padx = 31, pady = 20, command = square_root)
button_sqr = Button(frame, text = "x^2", padx = 30, pady = 20, command = square)
button_pow = Button(frame, text = "x^n", padx = 31, pady = 20, command = lambda:click_plus("power"))
button_equal = Button(frame, text = "=", padx=39, pady=20, command = Add)
button_clr = Button(frame, text = "Clear", padx=74, pady=20, command = clr_scr)
button_quit = Button(frame, text = "Quit program", padx=50, pady=20, command = quit_pgm)

frame.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
button_0.grid(row=5,column=0)
button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_plus.grid(row=2,column=3)
button_minus.grid(row=3,column=3)
button_mul.grid(row=4,column=3)
button_div.grid(row=5,column=3)
button_pow.grid(row=1, column=0)
button_mod.grid(row=1,column=1)
button_sqr.grid(row=1,column=2)
button_sqrt.grid(row=1,column=3)
button_equal.grid(row=6,column=3)
button_clr.grid(row=5, column=1, columnspan=2)
button_quit.grid(row=6, column=0, columnspan=2)

root.mainloop()
