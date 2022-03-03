from tkinter import *
root = Tk()
root.title("Simple Calculator")
root.resizable(0, 0)  # this is to prevent from resizing the window


def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def button_clear():
    global expression
    expression = ""
    input_text.set("")


def button_equal():
    global expression
    # 'eval':This function is used to evaluates the string expression directly
    result = str(eval(expression))
    input_text.set(result)
    expression = ""


expression = ""

# 'StringVar()' :It is used to get the instance of input field

input_text = StringVar()

e = Entry(root, font=('bold'), textvariable=input_text,
          width=35, borderwidth=5)
# extend the column to 3 columns
# padx = the horizontal position of this input field, pady = the vertical position of this input field
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# we need to include lambad then only can pass the value through the function
# create number button
Button_1 = Button(root, text="1", padx=40, pady=20, cursor="hand2",
                  command=lambda: button_click(1))
Button_2 = Button(root, text="2", padx=40, pady=20, cursor="hand2",
                  command=lambda: button_click(2))
Button_3 = Button(root, text="3", padx=40, pady=20, cursor="hand2",
                  command=lambda: button_click(3))
Button_4 = Button(root, text="4", padx=40, pady=20, cursor="hand2",
                  command=lambda: button_click(4))
Button_5 = Button(root, text="5", padx=40, pady=20, cursor="hand2",
                  command=lambda: button_click(5))
Button_6 = Button(root, text="6", padx=40, pady=20, cursor="hand2",
                  command=lambda: button_click(6))
Button_7 = Button(root, text="7", padx=40, pady=20, cursor="hand2",
                  command=lambda: button_click(7))
Button_8 = Button(root, text="8", padx=40, pady=20, cursor="hand2",
                  command=lambda: button_click(8))
Button_9 = Button(root, text="9", padx=40, pady=20, cursor="hand2",
                  command=lambda: button_click(9))
Button_0 = Button(root, text="0", padx=40, pady=20, cursor="hand2",
                  command=lambda: button_click(0))
Button_point = Button(root, text=".", padx=42, pady=20, cursor="hand2",
                      command=lambda: button_click('.'))
Button_equal = Button(root, text="=", padx=40, pady=20, cursor="hand2",
                      command=lambda: button_equal())
Button_clear = Button(root, text="Clear", padx=120, cursor="hand2",
                      pady=20, bg="#eee", command=lambda: button_clear())
Button_add = Button(root, text="+", padx=40, pady=20, bg="#eee", cursor="hand2",
                    command=lambda: button_click('+'))
Button_substract = Button(root, text="-", padx=40, pady=20, bg="#eee", cursor="hand2",
                          command=lambda: button_click('-'))
Button_multiply = Button(root, text="x", padx=40, pady=20, bg="#eee", cursor="hand2",
                         command=lambda: button_click('*'))
Button_divide = Button(root, text="/", padx=40, pady=20, bg="#eee", cursor="hand2",
                       command=lambda: button_click('/'))
# put buttons on the screen
Button_1.grid(row=1, column=0)
Button_2.grid(row=1, column=1)
Button_3.grid(row=1, column=2)
Button_add.grid(row=1, column=3)

Button_4.grid(row=2, column=0)
Button_5.grid(row=2, column=1)
Button_6.grid(row=2, column=2)
Button_substract.grid(row=2, column=3)

Button_7.grid(row=3, column=0)
Button_8.grid(row=3, column=1)
Button_9.grid(row=3, column=2)
Button_multiply.grid(row=3, column=3)


Button_0.grid(row=4, column=0)
Button_point.grid(row=4, column=1)
Button_divide.grid(row=4, column=2)
Button_equal.grid(row=4, column=3)

Button_clear.grid(row=5, column=0, columnspan=3)

root.mainloop()