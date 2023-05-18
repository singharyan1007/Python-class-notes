x=open("file.txt",'w')
x.write('Hi\n')
x.write('Hello\n')
x.close()

x=open('file.txt','a')
x.write("Goodbye\n")
x=open('file.txt','r')
print(x.read())