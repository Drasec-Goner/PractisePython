#packing and unpacking

# tuple1 = (1,2,3,4,5)
# (a, b, c, d, e) = tuple1
# print(a,b,c,d,e)

tuple2 = ("car", "bike", "boat", "cycle", "jet")
(item1, *item2, item3) = tuple2
print(item1)
print(item2)
print(item3)