#Write a program to display only those numbers
#from a list that satisfy following condition

# Number must be divisible by 5
# if the number is greater than 150, then skip it and move to next number
# if the number is greater than 500, stop the loop
# numbers = [12,75,150,180,145]

numbers = [12,75,150,180,145]

for i in numbers:
    if i%5==0:
        if i>150:
            continue
        elif i>500:
            break
        print(i)
    