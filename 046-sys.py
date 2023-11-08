# docs.python.org/3/
from sys import argv

try:
    print("hello, my name is", argv[1])
except IndexError:
    print("Too few parameters")

