from tkinter import*
from tkinter import ttk #นำเข้าเพื่อทำให้ปุ่มไม่นู่น
from tkinter import messagebox #ตกแต่งหน้าจอแสดงผล

####################CSV####################
import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)
        
def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file)
        data = list(fr)
    return data
###########################################

GUI = Tk()
GUI.title('NOTE BY ME')
GUI.geometry('500x1100') 

L1 = Label(GUI,text='TO DO LIST',font=('Arial Black',30),fg='Black',bg='#F7F6CF',width=10,height=1)
L1.place(x=120,y=80)

GUI.configure(bg='#4F80C0')

##########
def button2():
        text='เรียนเทปแคลคูลัส'
        messagebox.showinfo('To Do',text)

FB1=Frame(GUI)
FB1=LabelFrame(GUI,text='Fighting!',font=('Arial Black',10),fg='White',bg='#FBCCD0')
FB1.place(x=200,y=200)
B2 = ttk.Button(FB1,text='To Do List',command=button2)
B2.pack(ipadx=5,ipady=5,padx=10,pady=10)

##########
def button3():
        text='การบ้าน Python Ep.2'
        messagebox.showinfo('You can do it',text)

FB2=Frame(GUI)
FB2=LabelFrame(GUI,text='Dont give up!',font=('Arial Black',10),fg='White',bg='#FBCCD0')
FB2.place(x=200,y=350)
B3 = ttk.Button(FB2,text='Finish',command=button3)
B3.pack(ipadx=5,ipady=5,padx=10,pady=10)

##########
def button4():
        text='เรียนรู้การเขียน tkinter'
        messagebox.showinfo('Good job',text)

FB3=Frame(GUI)
FB3=LabelFrame(GUI,text='Good job!',font=('Arial Black',10),fg='White',bg='#FBCCD0')
FB3.place(x=200,y=500)
B4 = ttk.Button(FB3,text='Feedback',command=button4)
B4.pack(ipadx=5,ipady=5,padx=10,pady=10)

##########
def button5():
        text='จดทั้งหมดลง GoodNotes'
        messagebox.showinfo('Keep Fighting',text)

FB4=Frame(GUI)
FB4=LabelFrame(GUI,text='Relax!',font=('Arial Black',10),fg='White',bg='#FBCCD0')
FB4.place(x=200,y=650)
B5 = ttk.Button(FB4,text='Note',command=button5)
B5.pack(ipadx=5,ipady=5,padx=10,pady=10)

###########
LF1 = ttk.LabelFrame(GUI,text='Everyting that she like')
LF1.place(x=155,y=800)

v_data = StringVar()
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Arial Black',10))
E1.pack(pady=5,padx=5)

from datetime import datetime

def SaveData():
        t = datetime.now().strftime('%Y%m%d %H%M%S')
        data = v_data.get()
        text = [t,data]
        writecsv(text)
        v_data.set('')
        
B4 = ttk.Button(LF1,text='Save',command=SaveData)
B4.pack(ipadx=10,ipady=10)

GUI.mainloop()