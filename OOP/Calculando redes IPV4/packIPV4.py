import re

class CalcIPV4:
    def __init__(self, ip, cidr=None, mascara=None):
        self.ip = ip
        self.cidr = cidr
        self.mascara = mascara
        self._set_broadcast()
        self._set_rede()
    
    def exibe(self):
        print(f'IP: {self.ip}')
        print(f'Máscara: {self.mascara}')
        print(f'Rede: {self.rede}')
        print(f'Broadcast: {self.broadcast}')
        print(f'Prefixo: {self.cidr}')
        print(f"Número de IP's da rede: {self.nro_ips}")
    
    @property
    def ip(self):
        return self._ip
    
    @ip.setter
    def ip(self, valor):
        if not self._valida_ip(valor):
            raise ValueError('IP inválido!')
        self._ip = valor
        self._ip_bin = self._ip_to_bin(valor)
    
    @property
    def cidr(self):
        return self._cidr

    @cidr.setter
    def cidr(self, valor):
        if not valor:
            return 
        if not isinstance(valor, int):
            raise TypeError('Prefixo precisa ser um inteiro!')
        if valor > 32:
            raise TypeError('Prefixo precisa ter 32 Bits!')

        self._cidr = valor
        self._mascara_bin = (valor * '1').ljust(32, '0')
        if not hasattr(self, 'mascara'):
            self.mascara = self._bin_to_ip(self._mascara_bin)
    
    @property
    def mascara(self):
        return self._mascara
    
    @mascara.setter
    def mascara(self, valor):
        if not valor:
            return 
        if not self._valida_ip(valor):
            raise ValueError('Máscara inválida!')

        self._mascara = valor
        self._mascara_bin = self._ip_to_bin(valor)
        if not hasattr(self, 'cidr'):
            self.cidr = self._mascara_bin.count('1')
    
    @staticmethod
    def _valida_ip(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )

        if regexp.search(ip):
            return True
    
    @staticmethod
    def _ip_to_bin(ip):
        blocos = ip.split('.')
        blocos = [bin(int(val))[2 : ].zfill(8) for val in blocos]
        return ''.join(blocos)

    @staticmethod
    def _bin_to_ip(ip):
        n = 8
        blocos = [str(int(ip[i : n + i], 2)) for i in range(0, 32, n)]
        return '.'.join(blocos)
    
    def _set_broadcast(self):
        host_bits = 32 - self.cidr
        self._broadcast_bin = self._ip_bin[ : self.cidr] + (host_bits * '1')
        self._broadcast = self._bin_to_ip(self._broadcast_bin)
        return self._broadcast
    
    @property
    def broadcast(self):
        return self._broadcast

    def _set_rede(self):
        host_bits = 32 - self.cidr
        self._rede_bin = self._ip_bin[ : self.cidr] + (host_bits * '0')
        self._rede = self._bin_to_ip(self._rede_bin)
        return self._rede
    
    @property
    def rede(self):
        return self._rede

    def _nro_ips(self):
        return 2 ** (32 - self.cidr)

    @property
    def nro_ips(self):
        return self._nro_ips() 