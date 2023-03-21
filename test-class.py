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

class Shop(Cat):
    def __init__(self, name, color, age, disease, species, cost):
        super().__init__(name, color, age)
        self.disease = disease
        self.species = species
        self.cost = cost
        
    def start(self):
        print("...Welcome...")
        
    def stop(self):
        print("...Thank you...")
        
    def info(self):
        print(f"Information about your cat {self.name} ({self.color}, {self.age}):")
        print(f"  - Disease: {self.disease}")
        print(f"  - Species: {self.species}")
        print(f"  - Cost: {self.cost} baht")


my_shop = Shop("Singto", "White", 5, "flu", "Persian", 5000)

my_shop.start()
my_shop.info()
print('Update about your cat')
my_shop.meow()
my_shop.eat("fish")
my_shop.sleep()
my_shop.stop()