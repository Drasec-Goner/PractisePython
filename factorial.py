num = int(input("Enter a Number: "))
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
ft= fact(num)
print(ft)