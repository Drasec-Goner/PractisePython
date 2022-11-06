import sys

print(sys.getrecursionlimit(2000))

def hello():
    print("Hello World")
    hello()

