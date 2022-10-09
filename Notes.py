# Contributed by Anshu Kumar
import sqlite3 as sql
from tkinter import *
from tkinter import messagebox
try:
       con = sql.connect('pin_your_note.db')
       cur = con.cursor()
       cur.execute('''CREATE TABLE notes_table
                        (date text, notes_title text, notes text)''')
except:
       print("Connected to table of database")
def add_notes():
       today = date_entry.get()
       notes_title = notes_title_entry.get()
       notes = notes_entry.get("1.0", "end-1c")
       if (len(today) <=0) & (len(notes_title)<=0) & (len(notes)<=1):
               messagebox.showerror(message = "ENTER REQUIRED DETAILS" )
       else:
               cur.execute("INSERT INTO notes_table VALUES ('%s','%s','%s')" %(today, notes_title, notes))
               messagebox.showinfo(message="Note added")
               con.commit()
def view_notes():
       date = date_entry.get()
       notes_title = notes_title_entry.get()
       if (len(date) <=0) & (len(notes_title)<=0):
               sql_statement = "SELECT * FROM notes_table"
              
       elif (len(date) <=0) & (len(notes_title)>0):
               sql_statement = "SELECT * FROM notes_table where notes_title ='%s'" %notes_title
     
       elif (len(date) >0) & (len(notes_title)<=0):
               sql_statement = "SELECT * FROM notes_table where date ='%s'"%date
      
       else:
               sql_statement = "SELECT * FROM notes_table where date ='%s' and notes_title ='%s'" %(date, notes_title)
              
       cur.execute(sql_statement)
       row = cur.fetchall()
       if len(row)<=0:
               messagebox.showerror(message="No note found")
       else:
               for i in row:
                       messagebox.showinfo(message="Date: "+i[0]+"\nTitle: "+i[1]+"\nNotes: "+i[2])

def delete_notes():
       date = date_entry.get()
       notes_title = notes_title_entry.get()
       choice = messagebox.askquestion(message="Do you want to delete all notes?")
      
       if choice == 'yes':
               sql_statement = "DELETE FROM notes_table" 
       else:
               if (len(date) <=0) & (len(notes_title)<=0): 
                       messagebox.showerror(message = "ENTER REQUIRED DETAILS" )
                       return
               else:
                      sql_statement = "DELETE FROM notes_table where date ='%s' and notes_title ='%s'" %(date, notes_title)
    
       cur.execute(sql_statement)
       messagebox.showinfo(message="Note(s) Deleted")
       con.commit()
def update_notes():
       today = date_entry.get()
       notes_title = notes_title_entry.get()
       notes = notes_entry.get("1.0", "end-1c")
       if (len(today) <=0) & (len(notes_title)<=0) & (len(notes)<=1):
               messagebox.showerror(message = "ENTER REQUIRED DETAILS" )
       else:
               sql_statement = "UPDATE notes_table SET notes = '%s' where date ='%s' and notes_title ='%s'" %(notes, today, notes_title)
              
       cur.execute(sql_statement)
       messagebox.showinfo(message="Note Updated")
       con.commit()
window = Tk()

window.geometry("500x300")
window.title("Pin Your Note -TechVidvan")
 
title_label = Label(window, text="Pin Your Note -TechVidvan").pack()

date_label = Label(window, text="Date:").place(x=10,y=20)
date_entry = Entry(window,  width=20)
date_entry.place(x=50,y=20)

notes_title_label = Label(window, text="Notes title:").place(x=10,y=50)
notes_title_entry = Entry(window,  width=30)
notes_title_entry.place(x=80,y=50)

notes_label = Label(window, text="Notes:").place(x=10,y=90)
notes_entry = Text(window, width=50,height=5)
notes_entry.place(x=60,y=90)
 
button1 = Button(window,text='Add Notes', bg = 'Turquoise',fg='Red',command=add_notes).place(x=10,y=190)
button2 = Button(window,text='View Notes', bg = 'Turquoise',fg='Red',command=view_notes).place(x=110,y=190)
button3 = Button(window,text='Delete Notes', bg = 'Turquoise',fg='Red',command=delete_notes).place(x=210,y=190)
button4 = Button(window,text='Update Notes', bg = 'Turquoise',fg='Red',command=update_notes).place(x=320,y=190)
 
window.mainloop()
con.close()