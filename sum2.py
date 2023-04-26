def digsum(k):
    s=sum(k)
    if s>9:
        k=[int(i) for i in str(sum(k))]
        digsum(k)
    return sum(k)
n=[int(i) for i in input()]
print(digsum(n))
