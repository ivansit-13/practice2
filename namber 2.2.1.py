class Student:

    def __init__(self, surname = "Нет Фамилии", data = "нет даты рождения", numberG = "нет номера группы",listg = "Нет листа оценок"):
        self.surname = surname
        self.data = data
        self.numberG = numberG
        self.listg = listg

    def changes_surname(self, surname):
        self.surname = surname

    def changes_data(self, data):
        self.data = data

    def changes_numberG(self, numberG):
       self.numberG = numberG

    def changes_listg(self,listg):
        self.listg = listg

    def info(self):
        print(f"Фамилия: {self.surname}")
        print(f"Дата рождения: {self.data}")
        print(f"Номер группы: {self.numberG}")
        print(f"Успеваемость: {self.listg}")

print("Если хотите выйти введите 0, иначе, любой символ")
a = input("Вы вводите: ")
while a != "0":
    print("Вы хотите редактировать пользователя? 0 - нет, 1 - да")
    a = input("Вы вводите: ")
    Student1 = Student()
    if a == "1":
        surname = input("Введите Фамилию ")
        Student1.changes_surname(surname)
        data = input("Введите дату раждения ")
        Student1.changes_data(data)
        numberG = int(input("Введите номер группы "))
        Student1.changes_numberG(numberG)
        listg = []
        for i in range(5):
            grade = int(input(f"Введите оценку {i + 1}: "))
            listg.append(grade)
        Student1.changes_listg(listg)
        Student1.info()
    else:
        Student1.info()
    print("Если хотите выйти введите 0, иначе, любой символ")
    a = input("Вы вводите: ")