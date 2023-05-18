# Dictionary to stores squares of a number
# keys are immutable
# numbers tuples strings are immutable
d={}
num=int(input());
for i in range(1,num+1):
    d[i]=i*i

d[1]=0    
print(d)    