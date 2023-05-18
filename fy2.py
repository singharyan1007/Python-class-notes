a=open('file.txt','w')
s="Mvit"
a.write(s)
a.close()

x=open("file.txt",'r')
print(x.read())