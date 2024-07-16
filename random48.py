import random
import string

def random_hex():
    """Random 48 bit hexadecimal number"""

    random_48 = ""
    hexadecimals = [x for x in string.hexdigits if x.isdigit() or x.isupper()]

    for _octet in range(0, 6):
        octet = "".join(map(str, random.sample(hexadecimals, 2)))
        random_48 += octet + ":"

    return random_48[:-1]

if __name__ == '__main__':
    print(random_hex())
