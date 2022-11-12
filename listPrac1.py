colors = ["Red","Blue","Red","Black", 22]
colors[0:2] = ["Yellow","Purple"]
print(colors)
colors.insert(2, "Indigo")
print(colors)
colors.append("BMW")
print(colors)

cars= ["TATA","FORD","MARUTI SUZUKI"]
players = ("Dhoni","Messi", "Dravid")
colors.extend(cars)
print(colors)
colors.extend(players)
print(colors)
colors.remove("Red")
print(colors)

colors.pop(1)
print(colors)

del colors[0]
print(colors)

colors.clear()
print(colors)