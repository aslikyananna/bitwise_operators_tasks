def Swapping(a,b):
    a = a^b
    b = a^b
    a = a^b
    return a,b
print(Swapping(2,5))