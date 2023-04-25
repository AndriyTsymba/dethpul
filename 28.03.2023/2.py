a=str(input())
k1=0
k2=0
for i in a:
    if i.isnumeric():
        k1=k1+1
    elif i.isalpha():
        k2=k2+1
print(k1,k2,sep=" ")