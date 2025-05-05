#https://yandex.ru/video/preview/855802827772808546
# Задание 1.
# Разработайте приложение по работе со студентами. Приложение
# должно хранить данные о студентах в базе данных. Сущность
# студента должна описываться в виде класса, у которого будут
# следующие поля:
# 1) Имя
# 2) Фамилия
# 3) Отчество
# 4) Группа
# 5) Оценки(массив из 4 элементов)
# В приложении должен быть следующий функционал:
# 1) Добавление нового студента
# 2) Просмотр всех студентов
# 3) Просмотр одного студента, включая его средний балл
# 4) Редактирование студента
# 5) Удаление студента
# 6) Просмотр среднего балла студентов у конкретной группы

import sqlite3

class Student:
    def __init__(self, name, surname, patronymic, group, evaluations):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.group = group
        self.evaluations = evaluations

    def info_name(self):
        return self.name
    def info_surname(self):
        return self.surname
    def info_patronymic(self):
        return self.patronymic
    def info_group(self):
        return self.group
    def info_evaluations(self):
        return self.evaluations

class DataBas:
    def __init__(self, db_name="StudentsOfEmpire.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.connect_db()
        self.create_table()

    def connect_db(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS student (
            name TEXT,
            surname TEXT,
            patronymic TEXT,
            "group" TEXT,
            evaluations TEXT
        )""")
        self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()

    def add_student(self, student):
        self.cursor.execute("INSERT INTO student VALUES (?, ?, ?, ?, ?)", (
            student.info_name(), student.info_surname(), student.info_patronymic(),
            student.info_group(), str(student.info_evaluations())))
        self.connection.commit()
        print("Student added successfully.")

    def view_all_students(self):
        self.cursor.execute("SELECT * FROM student")
        students = self.cursor.fetchall()
        if students:
            for student in students:
                print(student)
        else:
            print("А может гранату бросить? -Так ведь нет никого...")

db_manager = DataBas()

print("_Здравствуйте в Базе данных студентов_", "\n", "Правила:", "\n",
        1, "- начать работу", "\n",
        0, "- выход", "\n")

exit_code = int(input("Вы выбрали: "))

while exit_code != 0:
    print("\nЗдравствуйте в Базе данных студентов:")
    print("Правила:")
    print("1 - ДОБАВИТЬ НОВОГО СТУДЕНТА")
    print("2 - ПРОСМОТР ВСЕХ СТУДЕНТОВ")
    print("3 - ПРОСМОТР 1 СТУДЕНТА ВКЛЮЧАЯ ЕГО СР.БАЛ")
    print("4 - РЕДАКТИРОВАНИЕ СТУДЕНТА")
    print("5 - УДАЛЕНИЕ СТУДЕНТА")
    print("6 - ПРОСМОТР СР.БАЛ КОНКРЕТНЫХ СТУДЕНТОВ ОПРЕДЕЛЁННОЙ ГРУППЫ")
    print("0 - выход")

    choice = int(input("Вы выбрали: "))
    if choice == 1:
        name = input("Введите Имя Студента: ")
        surname = input("Введите Фамилию Студента: ")
        patronymic = input("Введите Отчество Студента: ")
        group = input("Введите Группу Студента: ")
        evaluations = []
        for i in range(4):
            grade = int(input(f"Введите оценку {i + 1}: "))
            evaluations.append(grade)
        Student1 = Student(name, surname, patronymic, group, evaluations)
        db_manager.add_student(Student1)
    elif choice == 2:
        db_manager.view_all_students()
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass
    elif choice == 0:
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите номер из меню.")

    print("\nВы не забыли о своих возможностях?", "\n", "Правила:", "\n",
            1, "- вы хотите продолжить? ", "\n",
            0, "- выход", "\n")
    exit_code = int(input("Вы выбрали: "))

db_manager.close()
print("Программа завершена. Или нет...")