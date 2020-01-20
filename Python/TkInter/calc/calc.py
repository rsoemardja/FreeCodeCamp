from tkinter import * 

root = Tk()
root.title("Simple Calculator")
#riit,geinetrt("400x400")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#e.insert(0, "Enter Your Name: ")

def Button_Clicker(number):
    new_number = e.get() + str(number)
    e.delete(0, END)
    e.insert(0, new_number)

def Button_Clear():
    e.delete(0, END)

def Button_Add():
    global f_num
    global math
    math = "addiction"
    f_num = first_number
    e.delete(0, END)

def Button_Subtract():
    global f_num
    global math
    math = "subtraction"
    f_num = first_number
    e.delete(0, END)

def Button_Multiply():
    global f_num
    global math
    math = "multiplication"
    f_num = first_number
    e.delete(0, END)

def Button_Divide():
    global f_num
    global math
    math = "division"
    f_num = first_number
    e.delete(0, END)

def Button_Equal(second_number):
    num_1 = f_num
    if math == "addition":
        e.delete(0, END)
        e.insert(0, int(num_1) + int(second_number))
	if math == "subtraction":
		e.insert(0, int(num_1) - int(second_number))
        e.delete(0, END)
	if math == "multiplication":
		e.insert(0, int(num_1) * int(second_number))
        e.delete(0, END)
	if math == "division":
		e.insert(0, int(num_1) / int(second_number))


# Define Buttons 

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(1))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(1))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(1))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(1))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(1))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(1))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(1))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(1))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(1))

button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)

button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)

# Put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
#button_subtract.grid(row=5, column=1)
#button_multiply.grid(row=5, column=2)
#button_divide.grid(row=6, column=0)

button_equal.grid(row=5, column=1, columnspan=2)

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

#myButton = Button(root, text="Enter Your Stock Quote", command=myClick)
#myButton.pack()

root.mainloop()