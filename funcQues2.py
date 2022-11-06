#Create a function in such a way that can pass any number of arguments to this and it should display each arguments's value

def Argue(*args):
    for i in args:
        print(i)

Argue("Shubham", "Soumya", "Atul", "Anurag", "Onkar", "Vaishnavi", "Ayush", "Jyotsana") 