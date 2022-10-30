a=0
b=1
c=a+b
n=0
print(a)
a=b
b=c
while n<=10:
    print(a)
    c=a+b
    a=b
    b=c
    n+=1