def fact(n):
    if(n==0 or n==1):
        return n
    
    return fact(n-1)*n

k=int(input("Enter the number"))
print(fact(k))
