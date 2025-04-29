# Задание 2. Создайте класс с именем Train, содержащий свойства: название пункта
# назначения, номер поезда, время отправления. Добавить возможность вывода
# информации о поезде, номер которого введен пользователем. Написать программу,
# демонстрирующую все возможности класса;

class Train:
    def __init__(self,name = "Нет названия пункта назначения",number = "Нет номера поезда",time = "Нет времени отправления"):
        self.name = name
        self.number = number
        self.time = time
    def info_number(self):
        return self.number
    def changes_name(self, name):
        self.name = name
    def changes_time(self, time):
        self.time = time

    def info(self):
        print(f"Названия пункта назначения: {self.name}")
        print(f"Номера поезда: {self.number}")
        print(f"Времени отправления: {self.time}")

Train1 = Train("Томск-Белый_Яр",643,"17:45")
Train2 = Train("Томск-Красноярск",6233,"21:45")
Train3 = Train("Томск-Новокузнецк",1423,"1:00")
mas = [Train1,Train2,Train3]
print("\n","______________","\n")
Train1.info()
print("\n","______________","\n")
Train2.info()
print("\n","______________","\n")
Train3.info()
print("\n","______________","\n")
exit_program = int(input("Если 1 - то вы хотите редактировать, иначе 0 - "))
while exit_program != 0:
    a = int(input("Введите номер поезда "))
    for i in range(len(mas)):
        if mas[i].info_number() == a:
            print("Замена данных","\n")
            newname = input("Названия пункта назначения: ")
            mas[i].changes_name(newname)
            newtime = input("Введите новое время поезда: ")
            mas[i].changes_time(newtime)
            print("\n", "______Новая_информация________", "\n")
            mas[i].info()
            print("\n", "______________________________", "\n")

    exit_program = int(input("Если 1 - то вы хотите продолжить редактировать, иначе 0 - "))