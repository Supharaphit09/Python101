#ไม่มีcsv
from tkinter import *
from PIL import ImageTk, Image

# สร้างหน้าต่าง GUI
root = Tk()
root.title("โปรแกรมบันทึกข้อมูล")
root.geometry("500x500")

# โหลดรูปภาพพื้นหลังด้วย PIL และแปลงเป็น PhotoImage ของ Tkinter
bg_image = Image.open("pic/1.jpg")
bg_image = bg_image.resize((500, 500), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_image)

# สร้าง Label สำหรับรูปภาพพื้นหลังและใช้ place() เพื่อตั้งพื้นที่ของรูปภาพ
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# สร้าง Label และ Entry สำหรับรับข้อมูล
name_label = Label(root, text="ชื่อ:")
name_label.place(x=50, y=50)

name_entry = Entry(root)
name_entry.place(x=100, y=50)

age_label = Label(root, text="อายุ:")
age_label.place(x=50, y=100)

age_entry = Entry(root)
age_entry.place(x=100, y=100)

# สร้างฟังก์ชันเพื่อบันทึกข้อมูลเมื่อกดปุ่ม Submit
def submit():
    name = name_entry.get()
    age = age_entry.get()
    with open("data2.txt", "a") as f:
        f.write(f"{name} {age}\n")
    name_entry.delete(0, END)
    age_entry.delete(0, END)

# สร้างปุ่ม Submit
submit_button = Button(root, text="Submit", command=submit)
submit_button.place(x=50, y=150)

# ใช้ mainloop() เพื่อแสดง GUI
root.mainloop()