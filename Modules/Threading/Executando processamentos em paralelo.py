'''
Executando processamentos em paralelo com
o módulo threading
'''
from threading import Thread
from time import sleep

class MyThread(Thread):
    def __init__(self, text, time):
        self._text = text
        self._time = time

        super().__init__()
    
    def run(self):
        sleep(self._time)
        print(self._text)

thread_1 = MyThread('Thread 1', 5)
thread_1.start()

thread_2 = MyThread('Thread 2', 3)
thread_2.start()

thread_3 = MyThread('Thread 3', 2)
thread_3.start()

for i in range(20):
    print(i + 1)
    sleep(1)