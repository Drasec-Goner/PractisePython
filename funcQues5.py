#Create a function that will display how many items in the list have more than 5 character
#name =["Atul","Shubham", "Anurag","Rahul", "Dev", "Roy"]
name =["Atul","Shubham", "Anurag","Rahul", "Dev", "Roy"]

def length(n):
    count=0
    for i in n:
        l = len(i)
        if l>5:
            count+=1
            print(i)
    return count

count=length(name)
print(count)