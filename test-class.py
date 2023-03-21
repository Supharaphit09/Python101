'''
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
'''

#Test 2
class chanel:
    chanelName = 'POPS Anime Thailand'
    
    def __init__(self, name,episod):
        self.name = name
        self.episod = episod
    
    def watch(self):
        print('ดูจบแล้ว' + '/n')
    
    def want(self):
        print('ตอนที่อยากดู' + '/n')
    
    def like(self):
        print('ตอนที่ชอบ' + '/n')

class anime(chanel):
    def __init__(self, name , episod , another , love):
        super().__init__(name , episod)
        self.another = another   # ตอนที่อยากดู
        self.love = love    # ตัวละครที่ชอบ
        
    def emo(self):
        print('very enjoy!')
        
    def emi(self):
        print("Don't forget to wear glasses!" + '\n')
        
#Instance
one = anime('Shin-chan' , '66-A', '66-B', 'Shin-chan')

one.emi()
print(f'Name : {one.name}')
print(f'Episode : {one.episod}')
print(f'Want to watch : {one.another}')
print(f'My fav character : {one.love}' + '\n')
one.emo()

print('===========================================')
two = anime('Shugo Chara!' , '2', "Don't have", "Don't have")

two.emi()
print(f'Name : {two.name}')
print(f'Episode : {two.episod}')
print(f'Want to watch : {two.another}')
print(f'My fav character : {two.love}' + '\n')
two.emo()