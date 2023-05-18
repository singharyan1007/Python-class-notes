import random
r=int(input())
n=[]
for i in range(r):
    ro=[]
    for j in range(r):
        k=random.randint(0,10)
        ro.append(k)
        
    n.append(ro)    
print(n)

for i in n:
    for j in i:
        print(j,end=" ")
    print()   