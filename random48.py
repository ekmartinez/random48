import re
import os
import sys
import string
import random

usage = """\nUsage options:
    --h | -help : Display usage options.
    --s | -set :  Sets MAC address to provided value.
    --r | -rand:  Sets random MAC address.

    Interface name: Ex: wlan0, enp0s1
    Valid MAC format: A1:B2:C3:D4:E5:F6

    Show usage:
        python random48.py -help

    Set MAC address to specific value:
        python random48.py -set <interface> <MAC>

    Set MAC address to random value:
        python random48.py -rand <interface>
    """

def random_hex():
    """Random MAC Address Generator"""

    random_48 = ""
    hexadecimals = [x for x in string.hexdigits if x.isdigit() or x.isupper()]

    for _octet in range(0, 6):
        octet = "".join(map(str, random.sample(hexadecimals, 2)))
        random_48 += octet + ":"

    return random_48[:-1]

def regx_mac(mac_addr):
    """MAC address validator"""

    mac_regex = r'^([0-9A-F]{2}:){5}[0-9A-F]{2}$'

    if re.match(mac_regex, mac_addr):
        return True
    else:
        print(usage)
        print("\nInvalid mac Address format")
        return False

def set_mac(iface, mac_addr):
    """Sets MAC address"""
    if regx_mac(mac_addr):
        print(mac_addr)
        cmd = f'sudo ip link set {iface} address {mac_addr}'
        os.system(cmd)

if __name__ == '__main__':
    try:
        option = sys.argv[1]
        match option:
            case '--h' | '-help':
                print(usage)
            case '--s' | '-set':
                set_mac(sys.argv[2], sys.argv[3])
            case '--r' | '-rand':
                random_mac = random_hex()
                set_mac(sys.argv[2], random_mac)
            case _:
                print(usage)
    except IndexError:
        print(usage)

