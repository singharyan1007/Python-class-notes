r=int(input())
c=int(input())
n=[]
k=1
for i in range(r):
    r=[]
    for j in range(c):
        r.append(k)
        k+=1
    n.append(r)    
print(n)

for i in n:
    for j in i:
        print(j,end=" ")
    print()    