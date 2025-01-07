import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.timer(self.name,self.power)

    def timer(self, name, power, enemies = 100):
        counter = 0
        while enemies:
            counter += 1
            time.sleep(1)
            enemies -= power
            print(f"{name} сражается {counter} день(дня) ..., осталось {enemies} воинов.")


        print(f"{name} одержал победу спустя {counter} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")