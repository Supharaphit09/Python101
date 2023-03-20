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

class Shop:
    def __init__(self, name, color, age, disease, species, cost):
        self.cat = Cat(name, color, age)
        self.disease = disease
        self.species = species
        self.cost = cost
        
    def start(self):
        print("...Welcome...")
        
    def stop(self):
        print("...Thank you...")
        
    def info(self):
        print(f"Information about your cat {self.cat.name} ({self.cat.color}, {self.cat.age}):")
        print(f"  - Disease: {self.disease}")
        print(f"  - Species: {self.species}")
        print(f"  - Cost: {self.cost} baht")
        
# Cat
my_cat = Cat("Singto", "white", 3)

my_cat.meow() 
my_cat.sleep()
my_cat.eat("fish")

# Shop
my_shop = Shop("Singto", "white", 3, "Fever", "Persian", 5000)

my_shop.start()
my_shop.info() 
my_shop.stop()