k=0
s=0
a=input()
a1=a.split(" ")
numbers=[int(i) for i in a1]
for i in numbers:
    s=s+i
    k=k+1
ser=s/k
print(s)
print(k)
print(ser)