def isEven(i):
    return i%2==0

list1 = [3, 2, 8, 16, 11, 34, 17]

output = list(filter(isEven,list1))
print(output)