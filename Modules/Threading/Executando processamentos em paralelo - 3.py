from threading import Thread
from threading import Lock
from time import sleep

class Tickets:
    """
    Classe que vende ingressos
    """
    def __init__(self, inventory):
        """ Inicializando...

        :param estoque: quantidade de ingressos em estoque
        """
        self._inventory = inventory
        # Nosso cadeado
        self._lock = Lock()

    @property
    def inventory(self):
        return self._inventory

    def buy(self, quantity):
        """
        Compra determinada quantidade de ingressos
        :param quantidade: A quantidade de ingressos que deseja comprar
        :type quantidade: int
        :return: Nada
        :rtype: None
        """
        # Tranca o método
        self._lock.acquire()

        if self._inventory < quantity:
            print("We don't have enough tickets...")
            # Libera o método
            self._lock.release()
            return

        sleep(1)

        self._inventory -= quantity
        print(f'You purchased {quantity} ticket(s).',
              f'We still have {self._inventory} in inventory...')

        # Libera o método
        self._lock.release()


if __name__ == '__main__':
    print('The box office is open...\n')
    tickets = Tickets(10)

    threads = []  # Lista para manter as threads
    for i in range(1, 20):
        t = Thread(target=tickets.buy, args=(i,))
        threads.append(t)

    # Inicia as threads
    for t in threads:
        t.start()

    # Verifica se todas as threads terminaram
    running = True
    while running:
        running = False

        for t in threads:
            if t.is_alive():
                running = True
                break
    
    print()            
    print('Tickets inventory:', tickets.inventory)