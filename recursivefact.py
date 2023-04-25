def fib(n):
    if(n<2):
        return n
    return fib(n-1)+fib(n-2)

k=int(input("Enter a number"))
print(fib(k))