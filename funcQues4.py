# a static list of 10 numbers


a =[32,21,64,100,13]
even,odd =0
def evenOdd(a):
    global even
    global odd
    for i in a:
        if i%2==0:
            even+=1
        else:
            odd+=1
evenOdd(a)
print("Even:",even)
print("Odd:",odd)