#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import math
import tkinter.messagebox


root = Tk()
root.title("Calulatrice pseudo scientifique de titi")
root.configure(background="blue")
root.resizable(width=False, height=False)
root.geometry("872x518+600+300")

calc = Frame(root)
calc.grid()


class Calc():
    def __init__(self):
        self.total =0
        self.current =""
        self.input_value= True
        self.check_sum = False
        self.operator = ""
        self.result = False

    def numberEntered(self, num):
        self.result = False
        firstnumber = txtDisplay.get()
        secondnumber = str(num)
        if self.input_value:
            self.current = secondnumber
            self.input_value = False
        else:
            if secondnumber == "":
                if secondnumber in firstnumber:
                    return
            self.current = firstnumber + secondnumber
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.operator == "add":
            self.total += self.current
        if self.operator == "sub":
            self.total -= self.current
        if self.operator == "multiple":
            self.total *= self.current
        if self.operator == "divide":
            self.total /= self.current
        if self.operator == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, operator):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.operator = operator
        self.result = False

    def clear(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def clearAll(self):
        self.clear()
        self.total = 0

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(float(txtDisplay.get()))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(float(txtDisplay.get()))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(float(txtDisplay.get()))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(float(txtDisplay.get()))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(float(txtDisplay.get()))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(float(txtDisplay.get()))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def square(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def modulo(self):
        self.result = False
        self.current = math.modf(float(txtDisplay.get()))
        self.display(self.current)

    def Pm(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(txtDisplay.get()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current)


added_value = Calc()

txtDisplay = Entry(calc, font=('arial',20,'bold'), bg='blue', bd=30, width=29, justify=RIGHT)
txtDisplay.grid(row=0 ,column=0 ,columnspan=4 ,pady=1)
txtDisplay.insert(0, "0")

numbers = "789456123"
i =0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('arial',20,'bold'), bd = 4, text = numbers[i]))
        btn[i].grid(row= j, column= k, pady= 1)
        btn[i]["command"] = lambda x= numbers[i]: added_value.numberEntered(x)
        i = i+ 1


btnClear = Button(calc, text=chr(67), width= 6, height=2, font=('arial',20,'bold'), bd = 4, bg= 'blue',
                  command = added_value.clear).grid(row=1 ,column=0, pady= 1)
btnClearAll = Button(calc, text=chr(67)+ chr(69), width= 6, height=2, font=('arial',20,'bold'), bd = 4, bg= 'blue',
                     command = added_value.clearAll).grid(row=1 ,column=1, pady= 1)

btnSquare = Button(calc, text="√" , width= 6, height=2, font=('arial',20,'bold'), bd = 4, bg= 'blue',
                   command = added_value.square).grid(row=1 ,column=2, pady= 1)


btnAdd = Button(calc, text="+", width= 6, height=2, font=('arial',20,'bold'), bd = 4, bg= 'blue',
                command=lambda: added_value.operation("add")).grid(row=1 ,column=3, pady= 1)

btnSub = Button(calc, text="-" , width= 6, height=2, font=('arial',20,'bold'), bd = 4, bg= 'blue',
                command=lambda: added_value.operation("sub")).grid(row=2 ,column=3, pady= 1)

btnMultiple = Button(calc, text="*", width= 6, height=2, font=('arial',20,'bold'), bd = 4, bg= 'blue',
                     command=lambda: added_value.operation("multiple")).grid(row=3 ,column=3, pady= 1)

btnDiv = Button(calc, text=chr(247), width= 6, height=2, font=('arial',20,'bold'), bd = 4, bg= 'blue',
                command=lambda: added_value.operation("divide")).grid(row=4 ,column=3, pady= 1)



btnZero = Button(calc, text="0", width= 6, height=2, font=('arial',20,'bold'), bd = 4, bg= 'blue',
                 command =lambda: added_value.numberEntered(0)).grid(row=5 ,column=0, pady= 1)

btnDot = Button(calc, text="." , width= 6, height=2, font=('arial',20,'bold'), bd = 4, bg= 'blue',
                command =lambda: added_value.numberEntered(".")).grid(row= 5 ,column= 1, pady= 1)

btnPM = Button(calc, text= chr(177), width= 6, height=2, font=('arial',20,'bold'), bd = 4, bg= 'blue',
               command = added_value.Pm).grid(row= 5 ,column= 2, pady= 1)

btnEquals = Button(calc, text= "=", width= 6, height=2, font=('arial',20,'bold'), bd = 4, bg= 'blue',
                   command = added_value.sum_of_total).grid(row=5 ,column=3, pady= 1)



btnPi = Button(calc, text="π" , width= 6, height=2, font=('arial',20,'bold'), bd=4, bg= 'blue',
               command = added_value.pi).grid(row=4 ,column=5, pady= 1)
btnCos = Button(calc, text="cos", width= 6, height=2, font=('arial',20,'bold'), bd=4, bg= 'blue',
                command =added_value.cos).grid(row=1 ,column=5, pady= 1)
btnTan = Button(calc, text="tan" , width= 6, height=2, font=('arial',20,'bold'), bd=4, bg= 'blue',
                command =added_value.tan).grid(row=1 ,column=6, pady= 1)
btnSin = Button(calc, text="sin", width= 6, height=2, font=('arial',20,'bold'), bd=4, bg= 'blue',
                command = added_value.sin).grid(row=1 ,column=4, pady= 1)


btnCosh = Button(calc, text="cosH", width= 6, height=2, font=('arial',20,'bold'), bd=4,
                 command = added_value.cosh).grid(row=2 ,column=4, pady= 1)
btnTanh = Button(calc, text="tanH", width= 6, height=2, font=('arial',20,'bold'), bd=4,
                 command = added_value.tanh).grid(row=2 ,column=5, pady= 1)
btnSinH = Button(calc, text="sinH" , width= 6, height=2, font=('arial',20,'bold'), bd=4,
                 command = added_value.sinh).grid(row= 2 ,column= 6, pady= 1)


btnLog = Button(calc, text= "log", width= 6, height=2, font=('arial',20,'bold'), bd = 4,
                command = added_value.log).grid(row= 3 ,column= 4, pady= 1)
btnExp = Button(calc, text= "Exp", width= 6, height=2, font=('arial',20,'bold'), bd = 4,
                command = added_value.exp).grid(row= 3 ,column= 5, pady= 1)
btnMod = Button(calc, text= "Mod", width= 6, height=2, font=('arial',20,'bold',), bd = 4,
                command = added_value.modulo).grid(row= 3 ,column= 6, pady= 1)
btnE = Button(calc, text= "e", width= 6, height=2, font=('arial',20,'bold'), bd = 4, command = added_value.e ).grid(row= 4 ,column= 4, pady= 1)


btnLog2 = Button(calc, text= "log2", width= 6, height=2, font=('arial',20,'bold'), bd = 4, bg='blue',
                 command = added_value.log2).grid(row= 5 ,column= 4, pady= 1)
btnacosh = Button(calc, text= "acosH", width= 6, height=2, font=('arial',20,'bold'), bd = 4, bg='blue',
                  command = added_value.acosh).grid(row= 4 ,column= 6, pady= 1)
btnAsinh = Button(calc, text= "asinH", width= 6, height=2, font=('arial',20,'bold'), bd = 4, bg='blue',
                  command = added_value.asinh).grid(row= 5 ,column= 5, pady= 1)


labeldisplay = Label(calc, text="Hello", font=('arial', 30, 'bold'), justify=CENTER)
labeldisplay.grid(row = 0, column = 4, columnspan=4)


#===================MENU===================

def Exit():
    Exit= tkinter.messagebox.askyesno("Hey", "Voulez-vous vraiment quitter ?")
    if Exit > 0:
        root.destroy()
        return


def Calculate():
    root.resizable(width=False, height=False)
    root.geometry("944x568+600+300")

menubar = Menu(calc)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "options", menu=filemenu)
filemenu.add_command(label="exit", command=Exit)

root.config(menu=menubar)
root.mainloop()