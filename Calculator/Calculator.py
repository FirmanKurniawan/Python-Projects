from tkinter import *
from tkinter.messagebox import showinfo


def about():
    showinfo("Made by Mihir")


def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == '^2':
        value1 = int(scvalue.get())
        value = value1 ** 2
        scvalue.set(value)
        screen.update()
    elif text == '=':
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Error"
        scvalue.set(value)
        screen.update()

    elif text == "AC":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("230x320")
root.resizable(0, 0)
root.title("Calculator")
root.wm_iconbitmap("1.ico")
root.configure(background="white")

MenuBar = Menu(root)
HelpMenu = Menu(MenuBar, tearoff=0)
HelpMenu.add_command(label="Help", command=about)
MenuBar.add_cascade(label="Help", menu=HelpMenu)
root.config(menu=MenuBar)

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold", bg="#33cccc")
screen.pack(fill=X, ipadx=8)

f = Frame(root, bg="grey")
b = Button(f, text="AC", width=2, font="lucida 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="^2", width=2, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT)

b = Button(f, text="%", width=2, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT)

b = Button(f, text="/", width=2, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="7", width=2, font="lucida 40 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="8", width=2, font="lucida 40 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT)

b = Button(f, text="9", width=2, font="lucida 40 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT)

b = Button(f, text="*", width=2, font="lucida 40 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="4", width=2, font="lucida 40 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="5", width=2, font="lucida 40 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT)

b = Button(f, text="6", width=2, font="lucida 40 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT)

b = Button(f, text="-", width=2, font="lucida 40 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="1", width=2, font="lucida 40 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="2", width=2, font="lucida 40 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT)

b = Button(f, text="3", width=2, font="lucida 40 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT)

b = Button(f, text="+", width=2, font="lucida 40 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT)
f.pack()

f = Frame(root, bg="grey", relief=SUNKEN)
b = Button(f, text="0", width=2, font="lucida 40 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text=".", width=2, font="lucida 40 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT)

b = Button(f, text="=", width=2, font="lucida 40 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT)
f.pack()
root.mainloop()