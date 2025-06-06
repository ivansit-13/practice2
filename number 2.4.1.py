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

# Подключаемся к базе данных "StudentsOfEmpire.db"
dbStudent = sqlite3.connect("StudentsOfEmpire.db")
# Создаем курсор для выполнения SQL-запросов
sql_dbStudent = dbStudent.cursor()

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

# Создаем таблицу "student", если она еще не существует.
# Обратите внимание на использование кавычек вокруг "group", т.к. это зарезервированное слово в SQL.
sql_dbStudent.execute(""" CREATE TABLE IF NOT EXISTS student (
    name TEXT,
    surname TEXT,
    patronymic TEXT,
    "group" TEXT,
    evaluations TEXT
)""")
# Фиксируем изменения в базе данных (сохраняем изменения)
dbStudent.commit()

# ЭТО ДЛЯ ВЫХОДА И ВХОДА В ПРОГРАММУ
print("_Здравствуйте в Базе данных студентов_","\n","Правила:","\n",
      1, "- начать работу", "\n",
      0, "- выход","\n")
exit_code = int(input("Вы выбрали: "))
while exit_code != 0:
    print("Здравствуйте в Базе данных студентов:", "\n", "Правила:", "\n",
          1, "- ДОБАВИТЬ НОВОГО СТУДЕНТА", "\n",
          2, "- ПРОСМОТР ВСЕХ СТУДЕНТОВ", "\n",
          3, "- ПРОСМОТР 1 СТУДЕНТА ВКЛЮЧАЯ ЕГО СР.БАЛ", "\n",
          4, "- РЕДАКТИРЫВАНИЕ СТУДЕНТА", "\n",
          5, "- УДАЛЕНИЕ СТУДЕНТА", "\n",
          6, "- ПРОСМОТР  СР.БАЛ КОНКРЕТНЫХ СТУДЕНТОВ ОПРЕДЕЛЁННОЙ ГРУППЫ", "\n",
          0, "- выход", "\n")
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
        Student1 = Student(name,surname,patronymic,group,str(evaluations))
        sql_dbStudent.fetchone()
        # Используем параметризованный запрос (знаки вопроса), чтобы избежать SQL-инъекций.
        sql_dbStudent.execute(f"INSERT INTO student VALUES (?, ?, ?, ?, ?)", (
        Student1.info_name(), Student1.info_surname(), Student1.info_patronymic(), Student1.info_group(),
        Student1.info_evaluations()))
        # Фиксируем изменения (сохраняем добавление).
        dbStudent.commit()
    elif choice == 2:
        # Выводим данные таблицы.
        for i in sql_dbStudent.execute("SELECT * FROM student"):
            print(i)
    elif choice == 3:
        surname = input("Введите фамилию студента для поиска: ")
        sql_dbStudent.execute("SELECT * FROM student WHERE surname = ?", (surname,))
        student_data = sql_dbStudent.fetchone()
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
    elif choice == 4:
        surname = input("Введите фамилию студента для редакции: ")
        sql_dbStudent.execute("SELECT * FROM student WHERE surname = ?", (surname,))
        student_data = sql_dbStudent.fetchone()
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
            sql_dbStudent.execute("UPDATE student SET name = ? WHERE name = ?",(Student1.info_name(),name))
            sql_dbStudent.execute("UPDATE student SET surname = ? WHERE surname = ?", (Student1.info_surname(),surname))
            sql_dbStudent.execute("UPDATE student SET patronymic = ? WHERE patronymic = ?", (Student1.info_patronymic(),patronymic))
            sql_dbStudent.execute("UPDATE student SET 'group' = ? WHERE 'group' = ?", (Student1.info_group(),group))
            sql_dbStudent.execute("UPDATE student SET evaluations = ? WHERE evaluations = ?", (Student1.info_evaluations(),evaluations))
            # Фиксируем изменения (сохраняем добавление).
            dbStudent.commit()
        else:
            print("Студент с такой фамилией не найден.")
    elif choice == 5:
        surname = input("Введите фамилию студента для УДАЛЕНИЯ)- ")
        sql_dbStudent.execute("SELECT * FROM student WHERE surname = ?", (surname,))
        student_data = sql_dbStudent.fetchone()
        if student_data:
            sql_dbStudent.execute("DELETE FROM student WHERE surname=?",(surname,))
        else:
            print("Студент с такой фамилией не найден.")
        dbStudent.commit()
    elif choice == 6:
        group = input("Введите группу студентов для узнания ср.бала: ")
        # Используйте параметры запроса для защиты от SQL-инъекций и у мменя тут была проблема с \"group\"
        sql_dbStudent.execute("SELECT evaluations FROM student WHERE \"group\" = ?", (group,))
        evaluations_mas = sql_dbStudent.fetchall()

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

    # ЭТО ДЛЯ ВЫХОДА И ПРОДОЛЖЕНИЯ РАБОТЫ С ПРОГРАММОЙ, ДА Я ЗАБЫЛ ОТЖАТЬ CAPS_LOOK
    print("Вы не забыли о своих возможностях?", "\n", "Правила:", "\n",
          1, "- вы хотите продолжить? ", "\n",
          0, "- выход", "\n")
    exit_code = int(input("Вы выбрали: "))

# Закрываем соединение с базой данных. Это важно делать!
dbStudent.close()