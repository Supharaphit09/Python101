# สร้าง Class สำหรับแมว (Cat)
class Cat:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
        
    def meow(self):
        print("Meow!")
        
    def sleep(self):
        print(f"{self.name} is sleeping.")
        
    def eat(self, food):
        print(f"{self.name} is eating {food}. Yum yum!")
        
# สร้าง Class สำหรับรถยนต์ (Car)
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def start_engine(self):
        print("Starting the engine...")
        
    def stop_engine(self):
        print("Stopping the engine...")
        
    def drive(self):
        print(f"Driving the {self.brand} {self.model} ({self.year})")
        
# สร้าง Object จาก Class Cat
my_cat = Cat("Whiskers", "white", 3)

# เรียกใช้ Method ของ Object Cat
my_cat.meow()  # output: "Meow!"
my_cat.sleep()  # output: "Whiskers is sleeping."
my_cat.eat("fish")  # output: "Whiskers is eating fish. Yum yum!"

# สร้าง Object จาก Class Car
my_car = Car("Toyota", "Camry", 2020)

# เรียกใช้ Method ของ Object Car
my_car.start_engine()  # output: "Starting the engine..."
my_car.drive()  # output: "Driving the Toyota Camry (2020)"
my_car.stop_engine()  # output: "Stopping the engine..."