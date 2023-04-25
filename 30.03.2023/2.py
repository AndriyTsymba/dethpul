k=0
a=input()
b=int(input())
a1=a.split(" ")
numbers=[int(i) for i in a1]
for i in numbers:
    if i == b:
        k=k+1
print(k)