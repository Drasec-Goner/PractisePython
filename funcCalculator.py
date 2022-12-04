
def calc(n1,n2,ch):
    if ch == 1:
        print(n1+n2)
    elif ch == 2:
        print(n1-n2)
    elif ch == 3:
        print(n1*n2)
    elif ch == 4:
        print(n1/n2)
    elif ch == 5:
        print(n1**n2)
    else:
        print("Invalid")


num1 = int(input("Enter The Number: "))
num2 = int(input("Enter The Number: "))

print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Expotential")

choice = int(input("Enter the Choice(1/2/3/4/5): "))

calc(num1,num2,choice)

