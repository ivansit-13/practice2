# Задание 3.
# Для данного задания требуется ознакомиться со следующим
# материалом:
# 1) https://docs-python.ru/packages/modul-psutil-python/
# Разработайте приложение Системный монитор. Приложение должно
# давать следующую информацию:
# 1) Мониторинг загрузки CPU
# 2) Мониторинг использованной оперативной памяти
# 3) Процентное соотношение загруженности диска
# Все данные должны сохраняться в базу данных со временем, когда
# был проведет мониторинг компьютера.
# Так же должна быть возможность посмотреть сохраненные данные

import datetime
import sqlite3
import psutil

class DataBas:
    def __init__(self, db_name="MonitoringPC.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.connect_db()
        self.create_table()

    def connect_db(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS monitor (
            time TEXT,
            CPU_percent REAL,
            memory_percent REAL,
            disk_percent REAL
        )""")
        self.connection.commit()

    def insert_data(self, cpu_percent, memory_percent, disk_percent):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Получаем текущее время в виде строки
        self.cursor.execute("INSERT INTO monitor (time, CPU_percent, memory_percent, disk_percent) VALUES (?, ?, ?, ?)",
                            (timestamp, cpu_percent, memory_percent, disk_percent))
        self.connection.commit()

    def view_all_monitoringPC(self):
        self.cursor.execute("SELECT * FROM monitor")
        monitor = self.cursor.fetchall()
        if monitor:
            for i in monitor:
                print(i)
        else:
            #Отсылка на Советский анекдот
            print("-А может гранату бросить? -Так ведь нет никого...")

    def close(self):
        if self.connection:
            self.connection.close()


monitoring = DataBas()
print("_Здравствуйте вы в Базе данных вашего ПК_", "\n", "Правила:", "\n",
        1, "- начать работу", "\n",
        0, "- выход", "\n")

exit_code = int(input("Вы выбрали: "))

while exit_code != 0:
    print("\nЗдравствуйте вы в Базе данных вашего ПК:")
    print("Правила:")
    print("1 - Просмотреть текущее состояние ПК")
    print("2 - ПРОСМОТР сохранённых данных о вашем ПК")
    print("0 - выход")
    choice = input("Вы выбрали: ")

    if choice == "1":
        #psutil.cpu_percent() текущая загрузка ЦП в процентах
        CPU = psutil.cpu_percent()
        print(f"Использование CPU: {CPU}%")
        #psutil.virtual_memory() статистика об использовании системной памяти RAM
        #.percent это процент загрузки
        RAM = psutil.virtual_memory().percent
        print(f"Использование памяти: {RAM}%")
        #psutil.disk_usage() статистика использования диска для раздела
        # '/' диск C (Возвращает данные корневого раздела)
        #.percent это процент загрузки
        SSD = psutil.disk_usage('/').percent
        print(f"Использование диска: {SSD}%")
        monitoring.insert_data(CPU, RAM, SSD)
    elif choice == "2":
        monitoring.view_all_monitoringPC()
    elif choice == "0":
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите номер из меню.")

    print("\nВы не забыли о своих возможностях?", "\n", "Правила:", "\n",
            1, "- вы хотите продолжить? ", "\n",
            0, "- выход", "\n")
    exit_code = int(input("Вы выбрали: "))

monitoring.close()
print("Программа завершена. Или нет...")