import re

class Model():
    def __init__(self, ip_cidr):
        self.ip_cidr = ip_cidr
    
    def is_valid_ip(self, ip_cidr):
        regex = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip_cidr)
        return bool(regex) and all(map(lambda n: 0<=int(n)<=255, regex.groups()))
        
    def ip_check(self, ip_addr):
        if self.is_valid_ip(ip_addr):
            self.__ip_addr = ip_addr
        else:
            raise ValueError(f'Invalid IP address: {ip_addr}')

    def save(self):
        with open('test.txt', 'a') as f:
            f.write(f"{self.cidr}\n")