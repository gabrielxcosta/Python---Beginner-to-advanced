'''
Herança múltipla de classes
'''
from LogMixin import LogMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            print(f'{self._nome} já está ligado!')
            return
        
        print(f'O aparelho foi ligado...')
        self._ligado = True
    
    def desligar(self):
        if not self._ligado:
            print(f'{self._nome} já está desligado!')
            return
        
        print(f'O aparelho foi desligado...')
        self._ligado = False

class SmartPhone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            error = f'{self._nome} está desligado!'
            print(error)
            self.log_error(error)
            return
        if self._conectado:
            error = f'{self._nome} já está conectado!'
            print(error)
            self.log_error(error)
            return

        info = 'O aparelho agora está conectado...'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._ligado:
            error = f'{self._nome} está desligado!'
            print(error)
            self.log_info(error)
            return
        if not self._conectado:
            error = f'{self._nome} já está desconectado!'
            print(error)
            self.log_error(error)
            return
            
        info = 'O aparelho agora está desconectado...'
        print(info)
        self.log_info(info)
        self._conectado = False

smartphone = SmartPhone('Samsung J8')
smartphone.conectar()
smartphone.desligar()
smartphone.ligar()
smartphone.conectar()
smartphone.conectar()
smartphone.conectar()
smartphone.desligar()
smartphone.conectar()
smartphone.desconectar()
smartphone.desconectar()
