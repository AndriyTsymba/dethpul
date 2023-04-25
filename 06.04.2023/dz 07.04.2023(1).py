a=input()
b=a[::-1]
x=a.replace(" ", "")
y=b.replace(" ", "")
c=x.lower()
d=y.lower()
if c==d:
    print("Yes")
else:
    print("No")