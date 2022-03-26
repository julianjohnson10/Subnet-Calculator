import re

class Model():
    def __init__(self, ip_cidr):
        self.ip_cidr = ip_cidr
    
    @property
    def ip_addr(self):
        return self.__ip_addr
    
    @property
    def cidr(self):
        return self.__cidr
    
    def is_valid_ip(self,ip_cidr):
        regex = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip_cidr)
        return bool(regex) and all(map(lambda n: 0<=int(n)<=255, regex.groups()))

    def cidr_to_ip(self,ip_cidr):
        self.ip_cidr = ip_cidr
        ip_addr = str(ip_cidr.split('/')[0])
        cidr = str(ip_cidr.split('/')[1])
        
        print(f"CIDR: {cidr}\nIP Address: {ip_addr}")

        if self.is_valid_ip(ip_addr):
            hosts = (32-int(cidr))
            return f'Hosts: {hosts}'
        else:
            return f'{ip_addr} is an invalid IP address.'

    def subnet_mask(self,args):
        network_address = ('1' * int(args))
        host_address = ('0' * (32-int(args)))
        bits = network_address + host_address
        first_octet = bits[:8]
        second_octet = bits[8:16]
        third_octet = bits[16:24]
        fourth_octet = bits[24:32]
        mask = first_octet + '.' + second_octet + '.' + third_octet + '.' + fourth_octet
        subnet_mask = str(int(first_octet,2)) + '.' + str(int(second_octet,2)) + '.' + str(int(third_octet,2)) + '.' + str(int(fourth_octet,2))
        print("Binary: " + mask)
        print("Subnet mask: "+ subnet_mask)

    def wildcard_mask(self, args):
        network_address = ('1' * int(args))
        host_address = ('0' * (32-int(args)))
        bits = network_address + host_address
        bits = bits.replace('0', '%temp%').replace('1', '0').replace('%temp%', '1')
        first_octet = bits[:8]
        second_octet = bits[8:16]
        third_octet = bits[16:24]
        fourth_octet = bits[24:32]
        mask = first_octet + '.' + second_octet + '.' + third_octet + '.' + fourth_octet
        wildcard_mask = str(int(first_octet,2)) + '.' + str(int(second_octet,2)) + '.' + str(int(third_octet,2)) + '.' + str(int(fourth_octet,2))
        print("Binary: " + mask)
        print("Subnet mask: "+ wildcard_mask)
    
    if __name__ == '__main__':
        
        cidr_to_ip(ip_cidr='192.168.100.100/16')