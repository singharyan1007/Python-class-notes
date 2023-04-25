def swwap(n,m):
    temp=n
    n=m
    m=temp

    return n,m



a=int(input("Enter first number "))
b=int(input("Enter the second number "))
print("first number is {} and second number is {}".format(a,b))
a,b=swwap(a,b)
print("swapped a: {} b: {} ".format(a,b))