import random
import threading
import time


class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            random_number = random.randint(50, 500)
            self.balance += random_number
            print(f"Пополнение: {random_number}. Баланс: {self.balance}")
            if self.balance>=500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            random_number = random.randint(50, 500)
            print(f"Запрос на {random_number}")
            if random_number<=self.balance:
                self.balance -= random_number
                print(f"Снятие: {random_number}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()

            time.sleep(0.001)


bk = Bank(0)


th1 = threading.Thread(target=Bank.deposit, args=(bk,))

th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()

th2.start()

th1.join()

th2.join()

print(f'Итоговый баланс: {bk.balance}')