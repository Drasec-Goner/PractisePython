colors = ["Red", "Blue", "Red", "Black"]
for x in range(len(colors)):
    print(colors[x])

x=0
cars = ["TATA","NANO","ALTO","Jeep"]
while x < len(cars):
    print(cars[x])
    x+=1

[print(x) for x in cars]
list2=[]
for i in cars:
    if "A" in i or "a" in i:
        list2.append(i)

print(list2)

newList = [x for x in cars if x == "TATA"]

print(newList)

newList =  [x.lower() for x in cars]

cars.sort()
colors.sort(reverse=True)
print(colors)
colors.sort(reverse=False)
print(colors)

