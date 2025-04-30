# Задание 1. Реализуйте класс Worker, который будет иметь следующие свойства: name,
# surname, rate (ставка за день работы), days (количество отработанных дней). Также класс
# должен иметь метод GetSalary(), который будет выводить зарплату работника. Зарплата -
# это произведение ставки rate на количество отработанных дней days;

class Worker:
    def __init__(self,name = "name",surname = "surname",rate = 0,days = 0):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days

    def defGetSalary(self):
        return print("Зарплата сие человека = ",self.rate * self.days)

    def info(self):
        print("____________Информация о персонале_____________")
        print(f"Имя - {self.name}")
        print(f"Фамилия - {self.surname}")
        print(f"Ставка - {self.rate}")
        print(f"Количество отработаных дней - {self.days}")
        print("_______________________________________________")

men = Worker("Иван","Петрович",250,5)
men.info()
men.defGetSalary()