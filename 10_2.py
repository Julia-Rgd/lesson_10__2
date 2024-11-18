from threading import Thread
import time

class Knight (Thread):
    def __init__(self, name, power):
        super().__init__()
        self.power = power
        self.name = name
    def run(self):
        enemies = 100
        day = 0
        print(f"Сир {self.name} на нас напали!")
        for i in range(enemies):
            if enemies > 0:
                time.sleep(1)
                day += 1
                enemies -= self.power
                print(f"{self.name} сражается {day} день ...., осталось {enemies} воинов.")
                if enemies <= 0:
                    print(f"{self.name} одержал победу спустя {day} дней!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все сражения закончены!")


"C:\Users\User\PycharmProjects\HELLO WORLD\.venv\Scripts\python.exe" "C:\Users\User\PycharmProjects\HELLO WORLD\module_10_2.py" 
Сир Sir Lancelot на нас напали!
Сир Sir Galahad на нас напали!
Sir Lancelot сражается 1 день ...., осталось 90 воинов.
Sir Galahad сражается 1 день ...., осталось 80 воинов.
Sir Galahad сражается 2 день ...., осталось 60 воинов.Sir Lancelot сражается 2 день ...., осталось 80 воинов.

Sir Galahad сражается 3 день ...., осталось 40 воинов.Sir Lancelot сражается 3 день ...., осталось 70 воинов.

Sir Galahad сражается 4 день ...., осталось 20 воинов.Sir Lancelot сражается 4 день ...., осталось 60 воинов.

Sir Galahad сражается 5 день ...., осталось 0 воинов.Sir Lancelot сражается 5 день ...., осталось 50 воинов.
Sir Galahad одержал победу спустя 5 дней!

Sir Lancelot сражается 6 день ...., осталось 40 воинов.
Sir Lancelot сражается 7 день ...., осталось 30 воинов.
Sir Lancelot сражается 8 день ...., осталось 20 воинов.
Sir Lancelot сражается 9 день ...., осталось 10 воинов.
Sir Lancelot сражается 10 день ...., осталось 0 воинов.
Sir Lancelot одержал победу спустя 10 дней!
Все сражения закончены!

Process finished with exit code 0
