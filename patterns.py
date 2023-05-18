n=[]
r=int(input());
for i in range(1,r+1):
    ro=[]
    for j in range(i):
        ro.append(j+1) 
    n.append(ro)
print(n)     

for i in range(r+1):
    for j in range(i):
        print(j+1,end=" ")
    print()   