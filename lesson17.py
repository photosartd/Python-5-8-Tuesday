class Human:
    #Задаём конструктор класс
    def __init__(self, age, name, height, pol):
        self.age = age
        self.name = name
        self.height = height
        self.pol = pol

    def tell_info(self):
        print("Hi! Im", self.name, ", im", self.age, "years old! Im", self.height, 
        "cm tall and im", self.pol)

    def get_older(self):
        self.age += 1

    def get_older(self, age):
        self.age += age
        
igar = Human(age=42, name="Igar", height=173, pol="Man")
igar.tell_info()
dasha = Human(age=12, name="Dasha", height=154, pol="Female")
dasha.tell_info()
dasha.get_older(100)
dasha.tell_info()
igar.tell_info()