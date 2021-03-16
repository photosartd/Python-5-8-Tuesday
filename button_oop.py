class Button:
    #Должен быть метод init
    def __init__(self):
        self.count = 0
    def click(self):
        self.count += 1
    def click_count(self):
        return self.count
    def reset(self):
        self.count = 0

button1 = Button()
print("В самом начале:")
print(button1.click_count())
print("Кликнем 1000 раза: ")
for i in range(1000):
    button1.click()
print(button1.click_count())
print("Обнулим количество кликов")
button1.reset()
print(button1.click_count())
