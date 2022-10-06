from cgitb import text
import tkinter
from pytube import YouTube

import tkinter as tk
from tkinter import *
import os
import re

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Youtube Caption Downloader")
        self.geometry('500x200')
        self.resizable(False, False)
        self.LocalCode = None
        self.my_menu = Menu(self)
        self.config(menu=self.my_menu)
        self.menubar()
        self.WidgetSetup()
    def WidgetSetup(self):
        self.URL = Entry(self, width=25,font=("Helvetica", 20))
        self.URL.place(x=65, y=50)
        self.Local = Entry(self, width=5,font=("Helvetica", 15))
        # self.Local.place(x=120, y=100)
        # self.Local['state'] = 'disabled'
        self.TextTopView = Label(self,text="ใส่ลิงก์ Youtube ลงไป",font=("Helvetica", 20)).place(x=250, y=25, anchor="center")
        self.Button = Button(self, text="ค้นหาซับ", width=8, font=("Helvetica", 15),command=self.finding,bg='#24d6d1',fg='white')
        self.Button.place(x=250, y=100)
        self.Button1 = Button(self, text="โหลดซับ", width=8, font=("Helvetica", 15),command=self.download,bg='#3eb83e',fg='white')
        self.Button1.place(x=350, y=100)
        self.Button1['state'] = 'disabled'
        self.Button2 = Button(self, text="เปิดโฟลเดอร์", width=15, font=("Helvetica", 10),command=lambda: os.startfile('Subtitle'))
        self.Button2.place(x=250, y=142)
        if os.path.isdir("Subtitle") != True:
            self.Button2['state'] = 'disabled'
        else:
            self.Button2['state'] = 'normal'
        # lambda: os.startfile('File_srt')
    def finding(self):
        Label(self,text=f'                            ').place(x=65,y=150)
        self.Mylabeldata = None
        if self.URL.get() == '':
              Label(self,text=f'ใส่ลิงก์ก่อน').place(x=65,y=150)
        else:
            Label(self,text=f'ภาษาในซับแล้วรหัส                          ').place(x=65,y=150)
            try:
                self.yt = YouTube(f'{self.URL.get()}')
                self.TextTopView = Label(self,text="                                                    ",font=("Helvetica", 20)).place(x=250, y=25, anchor="center")
                Label(self,text=f'{self.yt.title[0:30]} {self.yt.title[-5:-1]}').place(x=250, y=25, anchor="center")
                self.OPTION = []
                self.option_local = StringVar(self)
                
                for i in range(1,self.yt.captions.__len__()+1):
                    print(i)
                    self.OPTION.append(self.yt.captions.all()[i].code)
                    self.Mylabeldata = Label(self,text=f'ภาษา {self.yt.captions.all()[i].name} รหัส {self.yt.captions.all()[i].code}').place(x=65,y=150+(30*i))
                    self.geometry(f'500x{i*30+200}')
                    self.Local['state'] = 'normal'
                    self.URL['state'] = 'disabled'
                    self.Button['state'] = 'disabled'
                    self.Button1['state'] = 'normal'
                    self.DropDown()

            except:
                pass
    def split_text(self,text):
        import re
        string_to_split = text
        res = re.split(
            '[^a-zA-Zก-ฮ0-9.ะาิืี๊่้ึ ุูแโเะั ำไใฤฤาฦฦา่้๊๋ๆ-]', string_to_split)
        res = ''.join(res)
        res = re.split('\s+', res)
        res = ''.join(res)
        res = re.split('.mp4', res)
        res = ''.join(res)
        return res
    def download(self):
        self.LocalDropDown = Label(self,text="                                ",width=12,font=("Helvetica", 25))
        self.LocalDropDown.place(x=20, y=100)
        if self.LocalCode == None:
            self.LocalCode = self.OPTION[0]
        self.localtext = self.yt.captions.get(f'{self.LocalCode}')
        self.filename = self.split_text(self.yt.title)
        if os.path.isdir("Subtitle"):
            with open(f"Subtitle/{self.filename}.srt",'w',encoding="utf-8") as f:
                f.write(self.localtext.generate_srt_captions())
        else:
            os.mkdir("Subtitle")
            with open(f"Subtitle/{self.filename}.srt",'w',encoding="utf-8") as f:
                f.write(self.localtext.generate_srt_captions())
        self.URL['state'] = 'normal'
        self.Button['state'] = 'normal'
        self.Button1['state'] = 'normal'
        self.Button2['state'] = 'normal'
        Label(self,text=f'ดาวน์โหลดซับทำเสร็จแล้วไฟล่อยู่ที่').place(x=65,y=150)
        self.geometry('500x200')
    def DropDown(self):
        self.option_local.set(self.OPTION[0])
        Label(self,text="เลือกภาษา",font=("Helvetica", 15)).place(x=80, y=120, anchor="center")
        self.LocalDropDown = OptionMenu(self,self.option_local,*self.OPTION,command=self.callbackSelectLocal)
        self.LocalDropDown.config(width=5,font=("Helvetica", 17))
        self.LocalDropDown.place(x=140, y=100)
    def callbackSelectLocal(self,event):
        self.LocalCode = event

    def menubar(self):
        self.filemenu = Menu(self.my_menu, tearoff=0)
        self.filemenu.add_command(label="ออก", command=self.quit)
        self.my_menu.add_cascade(label="ไฟล์", menu=self.filemenu)
        self.langmenu = Menu(self.my_menu, tearoff=0)
        self.TextTh = self.langmenu.add_command(label="ไทย",command=self.changeTH)
        self.TextEng = self.langmenu.add_command(label="English",command=self.changeENG)
        self.my_menu.add_cascade(label="ภาษา", menu=self.langmenu)
    def changeTH(self):
        print('TH')
    def changeENG(self):
        print('English')
        # self.TextTh['label'] = 'ไทย'
        # self.TextEng['label'] = 'English'
        # self.Button['text'] = 'Find Subtitle'
if __name__ == "__main__":
    app = App()
    app.mainloop()