from tkinter import *
from PIL import Image, ImageTk
import csv

GUI = Tk()
GUI.title("Tax.calculate")
GUI.geometry("485x1000")

bg_image = Image.open("pic/1.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(GUI, image=bg_photo)
bg_label.place(x=0, y=-50)

GUI.configure(bg='#F7F6CF')

L1 = Label(GUI,text='WELCOME',font=('Arial Black',30),fg='Black',bg='#F5F7CF',width=10,height=1)
L1.place(x=120,y=80)

# Button
name_label = Label(GUI, text="NAME:",font=('Arial Black',8),fg='Black',bg='#F5F7CF')
name_label.place(x=150, y=300)

name_entry = Entry(GUI)
name_entry.place(x=200, y=300)

id_label = Label(GUI, text="ID:",font=('Arial Black',8),fg='Black',bg='#F5F7CF')
id_label.place(x=150, y=450)

id_entry = Entry(GUI)
id_entry.place(x=180, y=450)

income_label = Label(GUI, text="INCOME:",font=('Arial Black',8),fg='Black',bg='#F5F7CF')
income_label.place(x=150, y=600)

income_entry = Entry(GUI)
income_entry.place(x=220, y=600)

class TaxCalculator:
    def __init__(self, income):
        self.income = income

    def calculate_tax(self):
        tax = 0
        income = self.income

        if income <= 150000:
            tax = 0
        elif income <= 300000:
            tax = (income - 150000) * 0.05
        elif income <= 500000:
            tax = (income - 300000) * 0.1 + 7500
        elif income <= 750000:
            tax = (income - 500000) * 0.15 + 27500
        elif income <= 1000000:
            tax = (income - 750000) * 0.2 + 65000
        elif income <= 2000000:
            tax = (income - 1000000) * 0.25 + 115000
        elif income <= 5000000:
            tax = (income - 2000000) * 0.3 + 365000
        else:
            tax = (income - 5000000) * 0.35 + 1265000

        return tax

income_entry = Entry(GUI)
income_entry.place(x=220, y=600)

# Submit
def submit():
    name = name_entry.get()
    id = id_entry.get()
    income = float(income_entry.get())
    tax_calculator = TaxCalculator(income)
    tax = tax_calculator.calculate_tax()
    with open("tax.csv", "a", newline="") as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(["Name", "ID", "Income", "Tax"])
        writer.writerow([name, id, income, tax])
    name_entry.delete(0, END)
    id_entry.delete(0, END)
    income_entry.delete(0, END)


submit_button = Button(GUI, text="Submit", command=submit, bg='#cfd0f7')
submit_button.place(x=150, y=700)

GUI.mainloop()