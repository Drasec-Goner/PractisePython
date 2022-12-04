mySet1 = {"car", "boat", "train"}
mySet2 = {1,2,3,4}
mySet1.add("jet")
print(mySet1)
mySet1.update(mySet2)
print(mySet1)
mySet1.discard("boat")
print(mySet1)
mySet1.remove(1)
print(mySet1)
mySet3 = {4,5,6}
res = mySet1.union(mySet3)
print(res)
res1 = mySet2.intersection(mySet3)
print(res1)
res2 = mySet2.symmetric_difference(mySet3)
print(res2)