# Tuples - store multiple items in a single variable
# non-homogenous
# ordered
# immutable/unchangeable

myTuple = (1,2,3,4,5)

print(myTuple)
print(len(myTuple))

tuple1 = ("apple", 1, 420.69)
print(tuple1)

tuple2 = ("car", "bike", "boat", "jet")
print(tuple2[:3])
list1 = list(tuple2)
list1.append("cycle")
tuple2 = tuple(list1)
print(tuple2)

tuple3 = (10,20,30,40,50)
#reverse it
tuple3 = list(tuple3)
tuple3.sort(reverse=True)
tuple3 = tuple(tuple3)
print(tuple3)

name = ('Soumya', 'Manna')
print(name)

tuple4 = ("apple", "orange", "pineapple")
del tuple4
print(tuple4)

tuple5 = (1,2,3,[6,7],4,5)
print(tuple5[3][0], tuple5[4])

tuple6 = (1,2,3,[6,7],4,5)
tuple6[3][0] = 8
print(tuple6)