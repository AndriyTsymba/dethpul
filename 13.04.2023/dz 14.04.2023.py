import random
a=[random.randint(-10, 10) for i in range(5)]
b=[random.randint(-10, 10) for i in range(5)]
print(a)
print(b)
c=a+b
print(c)
print(set(c))
max=c[0]
min=c[0]
for i in c:
    if i>max:
        max=i
print(max)
for i in c:
    if i<min:
        min=i
print(min)
d=[]