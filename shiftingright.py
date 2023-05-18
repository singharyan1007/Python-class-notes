n=[1,2,3,4,5]
# for i in range(int(input())):
#     n.insert(0,n.pop())
# print(n)    


# for i in range(int(input())):
#     n.insert(len(n)-1,n.pop(0))
# print(n)    

y=n[-2:]+n[:len(n)-2]
print(y)

