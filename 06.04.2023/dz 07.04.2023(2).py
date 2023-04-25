a=input()
c=input("введіть ОДНЕ слово для пошуку ")
b=a.split(" ")
for i in b:
    if i==c:
        x=i.upper()
print(a.replace(c, x))