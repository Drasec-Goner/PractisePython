n = int(input("Enter the no of terms: "))
print("Enter the Numbers: ")
tuple1= []
for i in range(n):
    inpo = int(input())
    tuple1[i] = inpo
print(tuple(tuple1))