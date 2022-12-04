def isEven(i):
    return i%2==0

list1 = [3, 2, 8, 16, 11, 34, 17]

output1 = list(filter(isEven,list1))
print(output1)
output2 = list(filter(lambda x:x>15,list1))
print(output2)

output3 = list(map(lambda x:x+2,list1))
print(output3)

output4 = list(map(lambda x:x**2,list1))
print(output4)