import threading as thr
import random
import time

class Bank:
    def __init__(self, balance= 0):
        self.balance = balance
        self.lock = thr.Lock()


    def deposit(self):
        if self.lock.locked() and self.balance < 500:
            self.lock.release()
        for i in range(100):
            self.lock.acquire()
            x = random.randint(50,500)
            self.balance += x
            print(f'Пополнение: {x}. Баланс: {self.balance}')
            self.lock.release()
            time.sleep(0.1)


            



    def take(self):
        for i in range(100):
            self.lock.acquire()
            x = random.randint(50, 500)
            print(f"Запрос на {x}")
            if x <= self.balance:
                self.balance -= x
                print(f'Снятие {x}. Баланс: {self.balance}')
                self.lock.release()
                time.sleep(0.1)
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.release() , time.sleep(0.1)




bk = Bank()

th1 = thr.Thread(target=Bank.deposit, args=(bk,))
th2 = thr.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')