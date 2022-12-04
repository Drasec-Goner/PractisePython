# list2 = [34,88,30,22,10,15,18]
#Print out all the multiples of 5 using filter and lambda

list2 = [34,88,30,22,10,15,18]

output = list(filter(lambda x:x%5==0,list2))
print(output)