from tkinter import*
from tkinter import ttk #นำเข้าเพื่อทำให้ปุ่มไม่นู่น
from tkinter import messagebox #ตกแต่งหน้าจอแสดงผล

GUI = Tk()
GUI.title('บันทึกสิ่งที่ต้องทำ')
GUI.geometry('500x500') 

L1 = Label(GUI,text='TO DO LIST',font=('Arial Black',30),fg='White',bg='#FFCFCF')
L1.place(x=120,y=50) 

##########
def button2():
        text='เรียนเทปแคลคูลัส'
        messagebox.showinfo('To Do',text)

FB1=Frame(GUI)
FB1=LabelFrame(GUI,text='อย่าขี้เกียจ!')
FB1.place(x=200,y=200)
B2 = ttk.Button(FB1,text='To Do List',command=button2)
B2.pack(ipadx=5,ipady=5,padx=10,pady=10)

##########
def button3():
        text='การบ้าน Python Ep.2'
        messagebox.showinfo('You can do it',text)

FB2=Frame(GUI)
FB2=LabelFrame(GUI,text='พยายามเข้า!')
FB2.place(x=200,y=400)
B3 = ttk.Button(FB2,text='Finish',command=button3)
B3.pack(ipadx=5,ipady=5,padx=10,pady=10)

##########
def button4():
        text='เรียนรู้การเขียน tkinter'
        messagebox.showinfo('Good job',text)

FB3=Frame(GUI)
FB3=LabelFrame(GUI,text='สิ่งที่ได้')
FB3.place(x=200,y=600)
B4 = ttk.Button(FB3,text='Feedback',command=button4)
B4.pack(ipadx=5,ipady=5,padx=10,pady=10)

##########
def button5():
        text='จดทั้งหมดลง GoodNotes'
        messagebox.showinfo('Keep Fighting',text)

FB4=Frame(GUI)
FB4=LabelFrame(GUI,text='จดบันทึก')
FB4.place(x=200,y=800)
B5 = ttk.Button(FB4,text='Note',command=button5)
B5.pack(ipadx=5,ipady=5,padx=10,pady=10)

GUI.mainloop()