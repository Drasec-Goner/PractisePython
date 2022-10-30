#Write a program to accept a number from the user
#calculate the sum of all the numbers from
#1 to given number

#eg user input 10
#+output should be 55
#1+2+3+4+5+6+7+8+9+10

num = int(input("Enter a number:"))

sum=0
for i in range(1,num+1):
    sum+=i

print(sum)