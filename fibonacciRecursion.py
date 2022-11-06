#print fibonacci series by recursion


def fibo(a,b):
    print(a)
    print(b)
    return fibo(b,a+b)

fibo(0,1)