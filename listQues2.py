numbers=[1,2,3,4,5,2,6]
num1 = numbers.index(2)
numbers.pop(num1)
numbers.insert(num1,200)
print(numbers)