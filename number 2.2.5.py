# Задание 5. Создать класс с двумя свойствами. Добавить конструктор с входными
# параметрами. Добавить конструктор, инициализирующий свойства по умолчанию.
# Добавить деструктор, выводящий на экран сообщение об удалении объекта. Написать
# программу, демонстрирующую все возможности класса;

class MyClass:
    def __init__(self, meaning1="Поумолчанию_1", meaning2="Поумолчанию_2"):
        self.meaning1 = meaning1
        self.meaning2 = meaning2

    def info(self):
      print(f"Значение 1: {self.meaning1}")
      print(f"Значение 2: {self.meaning2}")

    def __del__(self):
        print("Ну мы всё Удалили, отдыхай")

myclass = MyClass("Привет!", "МИР!")
myclass.info()

myclass_default = MyClass()
myclass_default.info()

myclass.meaning1 = "МИР!"
myclass.meaning2 = "ПРИВЕТ!"
myclass.info()

myclass.__del__()