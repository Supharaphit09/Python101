# 'w' สามารถใส่ข้อมูลได้รอบเดียว ถ้าใส่ข้อมูลใหม่จะทำให้ข้อมูลเก่าหาย
# ถ้าใส่ : ปิดท้าย บรรทัดต่อไปต้องเว้น 1 tap

#การwrite แบบ CSV ข้อดี มี , คั่น เข้าใจข้อมูลได้ง่าย
import csv
def readdata():
    with open('add-data.txt',encoding='utf-8') as file:
        data = file.readlines()   #read ไม่เว้นบรรทัด  readlines จะเว้นบรรทัด
        print(data)

#การwrite file 
def writedata():
    with open('data.txt','w',encoding='utf-8') as file:
        file.write('hello world')

def adddata(text):
    with open('add-data.txt','a',encoding='utf-8') as file:
        file.write(text + '\n')

def readdata():
    with open('add-data.txt',encoding='utf-8') as file:
        #data = file.readlines()   #read ไม่มี[ ] เป็นเหมือนปกติ  readlines/expoet to list ข้อมูลม[ ]
        data = file.read()
        print(data)

readdata()

#adddata('อายส์ชอบเต้น')                            