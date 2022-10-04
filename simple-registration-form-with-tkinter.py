from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
root = Tk()
root.configure(bg='blue')
root.geometry("500x700")#width,height
root.title("Latihan Tkinter")
# root.resizable(width=0,height=0) #Lock ukuran window nya

# PACK
# Label(root,text="Hello Word1", font="Normal 15", background="light blue").pack(side="left")
# Label(root,text="Hello Word", font="Normal 15", background="light blue").pack(side="left") #nambah di sampingnya numpuk
# Label(root,text="Hello Word", font="Normal 15", background="light blue").pack(side="right")
# Label(root,text="Hello Word", font="Normal 15", background="light blue").pack(side="bottom")
# Label(root,text="Hello Word", font="Normal 15", background="light blue").pack(side="top")
# Label(root,text="Hello Word", font="Normal 15", background="light blue").pack(side="top")

# GRID = layouting berbentuk tabel dimulai dari 0 gaes
# Label(root,text="Hello Word1", font="Normal 15", background="light blue").grid(row=0,column=0)
# Label(root,text="Hello Word2", font="Normal 15", background="light blue").grid(row=0,column=1)

# Label(root,text="Hello Word3", font="Normal 15", background="light blue").grid(row=1,column=0)

# PLACE pakai x dan y, x=horizontal, y=vertikal
# Label(root,text="Hello Word1", font="Normal 15", background="light blue").place(x=50,y=50)
# Label(root,text="Hello Word2", font="Normal 15", background="light blue").place(x=50,y=100)

cmb = IntVar()
def cek_data():
    data1 = entry1.get()
    data2 = entry2.get()
    if data1 == "admin" and data2 == "admin":
       messagebox.showinfo("Info", "Data Benar")
       return True
    else:
        messagebox.showinfo("Info", "Data Salah")
        return False
def input_data():
    cek = cek_data()
    if cek == True:
        data_text.delete("1.0",END)
        data1 = entry1.get()
        data2 = entry2.get()
        data3 = cmb.get()
        if data3 == 1:
            data3 = "Pria"
        else:
            data3 = "Wanita"

        data4 = entry3.get()
        data5 = data_combo.get()

        data = "Username : {}\nPassword : {}\nJenis Kelamin : {}\nAlamat : {}\nAgama : {}".format(data1,data2,data3,data4,data5)
        data_text.insert(INSERT,data)
    else:
        data_text.delete("1.0", END)


frame1 = Frame(root,bg="cyan")
Label(frame1,text="Form Registrasi", font="Normal 25", bg="cyan").grid(row=0,column=0,columnspan=3) #kalau di exel columnspan itu merge/menggabungkan cell

Label(frame1,text="Username", font="Normal 15", bg="cyan").grid(row=1,column=0, pady=15)
entry1 = Entry(frame1,font="Normal 15")
entry1.grid(row=1,column=1,padx=15,columnspan=2)

Label(frame1,text="Password", font="Normal 15").grid(row=2,column=0)
entry2 = Entry(frame1,font="Normal 15", show="*")
entry2.grid(row=2,column=1,padx=15,columnspan=2)

Label(frame1,text="Jenis Kelamin", font="Normal 15").grid(row=3,column=0,pady=15)
Radiobutton(frame1,text="Pria",variable=cmb,value=1,font="Normal 15").grid(row=3,column=1)
Radiobutton(frame1,text="Wanita",variable=cmb,value=2,font="Normal 15").grid(row=3,column=2)

Label(frame1,text="Alamat", font="Normal 15").grid(row=4,column=0)
entry3 = Entry(frame1,font="Normal 15")
entry3.grid(row=4,column=1,padx=15,columnspan=2)

data_agama = [
    'Islam',
    'Kristen',
    'Hindu',
    'Budha',
    'Katolik'
]
Label(frame1,text="Agama", font="Normal 15").grid(row=5,column=0,pady=15)
data_combo = ttk.Combobox(frame1,values=data_agama,font="Normal 10",width=29,state="readonly")
data_combo.grid(row=5,column=1,columnspan=2)

Button(frame1,text="Submit",background="light blue", fg="white", font="Normal 15",command=input_data).grid(row=6,column=0,columnspan=3)
Text(frame1,width=35,height=20).grid(row=7,column=0,columnspan=3,pady=15)
data_text = Text(frame1,width=35,height=15)
data_text.grid(row=7,column=0,columnspan=3,pady=10)

frame1.pack()
root.mainloop()
