# docs.python.org/3/
import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print(sys.argv[1])

for arg in sys.argv:
    print(arg, end=" ")