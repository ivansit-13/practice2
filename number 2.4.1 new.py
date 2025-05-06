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
        print("Студент был добавлен.")

    def view_all_students(self):
        self.cursor.execute("SELECT * FROM student")
        students = self.cursor.fetchall()
        if students:
            for student in students:
                print(student)
        else:
            print("А может гранату бросить? -Так ведь нет никого...")

    def viev_student_and_ball(self,surname):
        self.cursor.execute("SELECT * FROM student WHERE surname = ?", (surname,))
        student_data = self.cursor.fetchone()
        if student_data:
            name, surname, patronymic, group, evaluations_str = student_data
            # strip удаляет [], а split разбивает строку на список подстрок, используя указанный разделитель
            evaluations = [int(i) for i in evaluations_str.strip("[]").split(", ")]  # Преобразование строки в список
            average_grade = sum(evaluations) / len(evaluations)
            print("Информация о студенте:", name, surname, patronymic, "Группы: ", group)
            print("Его оценки: ", evaluations)
            print("Средний балл: ", average_grade)
        else:
            print("Студент с такой фамилией не найден.")

    def edit_student(self,surname):
        self.cursor.execute("SELECT * FROM student WHERE surname = ?", (surname,))
        student_data = self.cursor.fetchone()
        if student_data:
            name, surname, patronymic, group, evaluations = student_data
            new_name = input("Введите новое Имя Студента: ")
            new_surname = input("Введите новую Фамилию Студента: ")
            new_patronymic = input("Введите новое Отчество Студента: ")
            new_group = input("Введите новую Группу Студента: ")
            new_evaluations = []
            for i in range(4):
                grade = int(input(f"Введите новую оценку {i + 1}: "))
                new_evaluations.append(grade)
            Student1 = Student(new_name, new_surname, new_patronymic, new_group, str(new_evaluations))
            self.cursor.execute("UPDATE student SET name = ? WHERE name = ?", (Student1.info_name(), name))
            self.cursor.execute("UPDATE student SET surname = ? WHERE surname = ?",
                                  (Student1.info_surname(), surname))
            self.cursor.execute("UPDATE student SET patronymic = ? WHERE patronymic = ?",
                                  (Student1.info_patronymic(), patronymic))
            self.cursor.execute("UPDATE student SET 'group' = ? WHERE 'group' = ?", (Student1.info_group(), group))
            self.cursor.execute("UPDATE student SET evaluations = ? WHERE evaluations = ?",
                                  (Student1.info_evaluations(), evaluations))
            # Фиксируем изменения (сохраняем добавление).
            self.connection.commit()
        else:
            print("Студент с такой фамилией не найден.")

    def del_student(self,surname):
        self.cursor.execute("SELECT * FROM student WHERE surname = ?", (surname,))
        student_data = self.cursor.fetchone()
        if student_data:
            self.cursor.execute("DELETE FROM student WHERE surname=?", (surname,))
        else:
            print("Студент с такой фамилией не найден.")
        self.connection.commit()

    def view_group_average(self,group):
        # Используйте параметры запроса для защиты от SQL-инъекций и у мменя тут была проблема с \"group\"
        self.cursor.execute("SELECT evaluations FROM student WHERE \"group\" = ?", (group,))
        evaluations_mas = self.cursor.fetchall()
        if evaluations_mas:
            counter = 0
            counter_student = 0
            for evaluations_tuple in evaluations_mas:
                evaluations_str = evaluations_tuple[0]
                evaluations = [int(i) for i in evaluations_str.strip("[]").split(", ")]
                grade = sum(evaluations) / len(evaluations)
                counter += grade
                counter_student += 1
            a = counter / counter_student
            print(f"Средний балл для группы = ", a)
        else:
            print("Группа не найдена")

db_manager = DataBas()

print("_Здравствуйте вы в Базе данных студентов_", "\n", "Правила:", "\n",
        1, "- начать работу", "\n",
        0, "- выход", "\n")

exit_code = int(input("Вы выбрали: "))

while exit_code != 0:
    print("\nЗдравствуйте вы в Базе данных студентов:")
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
        surname = input("Введите фамилию студента для поиска: ")
        db_manager.viev_student_and_ball(surname)
    elif choice == 4:
        surname = input("Введите фамилию студента для редакции: ")
        db_manager.edit_student(surname)
    elif choice == 5:
        surname = input("Введите фамилию студента для УДАЛЕНИЯ)- ")
        db_manager.del_student(surname)
    elif choice == 6:
        group = input("Введите группу студентов для узнания ср.бала: ")
        db_manager.view_group_average(group)
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