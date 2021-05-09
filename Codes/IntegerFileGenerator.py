
#Practice In Python
import math

print("hi")
x=5
y=9
z = x + y
print(x, "+ ", y, "=", z)

for i in range(5):
    print ("Hi:", i)

name = input("What is your name:")
print("Name entered is :", name)

b = 23
print(bin(23), "-", oct(23), "-", hex(23))

x=None
if x is None:
    print("Not initialized ")

""" This is multi line comments
    THis is just a test 
"""


a = [1, 9, 8]
print(a)


def test(x):
    print(x)

def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner("raj kamal ")

iterable = ["winter", "summer", "spring", "monsoon"]

iterator = iter(iterable);

print(next(iterator))
print(next(iterator))

def getiter(iterator):
    try:
        return next(iterator)
    except StopIteration:
        print("Iterator ended")
        #raise ValueError("Iterator is empty")


list_com = [x * x for x in range(1, 10)]
print(list_com)

def is_prime(x):
    if x < 2 :
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True

filter_com = [x for x in range(1, 100) if is_prime(x)]
print(filter_com)


#flight -> SN060
class Flight:
    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError(f"No Airline Code in '{number}'")
        if not number[:2].isupper():
            raise ValueError(f"Invalie Airline Code '{number}'")
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("F invalid Route Number '{number}'")
        self.number = number

    def getNumber(self):
        return self.number

    def airline(self):
        return self.number[:2]


f = Flight("SN060")
print(f.getNumber(), "-", f.airline())


def main():
    print("running main")
    test(10)
    iterable = ["winter", "summer", "spring", "monsoon"]
    iterator = iter(iterable)
    data = getiter(iterator)
    banner(data)
    """
    data = getiter(iterator)
    banner(data)
    data = getiter(iterator)
    banner(data)
    data = getiter(iterator)
    banner(data)
    data = getiter(iterator)
    banner(data)
    data = getiter(iterator)
    banner(data)
    """

main()
if __name__ == '___main__;':
    test(10)