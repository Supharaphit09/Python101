class school:
    # Attribute
    schoolName = 'Acu'
    
    # Constructor ต้องอยู่หลัง Attribute
    def __init__(self, subject = 'Python Programming'):
        print('ให้แสดงข้อความนี้ เมื่อมีการสร้าง Instance')
        self.subject = subject
    
    # Method
    def hello(self):
        print('สวัสดีตอนเช้า ยินดีต้อนรับนักเรียนทุกคน')
        
    def teach(self):
        print(f'โรงเรียนนี้ เปิดสอนวิชา{self.subject}')

# วิธีการสืบทอด class
class student(school):
    def __init__(self, fullname, level, scores, subject):
        super().__init__(subject) #super ใช้สำหรับดึงข้อมูลจาก Attribute และ Method จาก class แม่
        self.fullname = fullname
        self.level = level
        self.scores = scores
    
    def checkGrade(self):
        if self.scores >= 80:
            print(f'วิชา{self.subject}ได้เกรด A')
        elif self.scores >= 70:
            print(f'วิชา{self.subject}ได้เกรด B')
        elif self.scores >= 60:
            print(f'วิชา{self.subject}ได้เกรด C')
        elif self.scores >= 50:
            print(f'วิชา{self.subject}ได้เกรด D')
        else:
            print(f'วิชา{self.subject}ได้เกรด F')
            
# Instance
#school1 = school() #School1 ชื่อ Instance #ถ้าใส่ text ไว้ใน () จะรันเป็น text เพราะมี Constructor 2 ตัว จึงเอาตัวที่อยู่หลังสุด
#print(f'ชื่อโรงเรียน : {school1.schoolName}')
#school1.hello()
#school1.teach()

print('================================')
student01 = student('สมชาย สายลม', 1 , 75, 'Math')
student01.hello
print(f'ชื่อโรงเรียน{student01.schoolName}')
print(f'ชื่อนักเรียน{student01.fullname}')
print(f'ระดับชั้น{student01.level}')
print(f'คะแนนสอบ{student01.scores}')
student01.checkGrade

print('================================')
student02 = student('สมศักดิ์', 1 , 5, 'Math')
student02.hello
print(f'ชื่อโรงเรียน{student02.schoolName}')
print(f'ชื่อนักเรียน{student02.fullname}')
print(f'ระดับชั้น{student02.level}')
print(f'คะแนนสอบ{student02.scores}')
student02.checkGrade

print('================================')
student03 = student('สมหญิง ปิ้ว', 2 , 99, 'Math')
student03.hello
print(f'ชื่อโรงเรียน{student03.schoolName}')
print(f'ชื่อนักเรียน{student03.fullname}')
print(f'ระดับชั้น{student03.level}')
print(f'คะแนนสอบ{student03.scores}')
student03.checkGrade
