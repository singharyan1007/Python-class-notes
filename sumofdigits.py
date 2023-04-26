n=[int(i) for i in input()]
k=[int(i) for i in str(sum(n))]
print(k)
while len(k)>1:
    if sum(k)>9:
        k=[int(i) for i in str(sum(k))]
        continue
    else:
        break

print(sum(k))
