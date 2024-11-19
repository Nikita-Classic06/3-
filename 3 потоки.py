import random
import threading
import time
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()


    def deposit(self):
        for i in range(100):
            dep = random.randint(50, 500)
            self.balance += dep
            print(f"Пополнение: {dep}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += dep
            print(f"Пополнение: {dep}. Баланс: {self.balance}")

            time.sleep(0.001)


    def take(self):

        for i in range(100):
            t = random.randint(50, 500)
            print(f"Запрос на {t}")
            if t <= self.balance:
                self.balance -= t
                print(f"Снятие: {t}. Баланс: {self.balance}")
            else:
                print(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()




bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()


print(f'Итоговый баланс: {bk.balance}')