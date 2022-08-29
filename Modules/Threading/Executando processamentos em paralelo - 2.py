from threading import Thread
from time import sleep

# Outra maneira de usar threads
def gonna_take_time(text, time):
    sleep(time)
    print(text)

thread_1 = Thread(target=gonna_take_time, args=('Thread appeared!...', 10))
thread_1.start()

while thread_1.is_alive():
    print('Waiting the thread...')
    sleep(2)