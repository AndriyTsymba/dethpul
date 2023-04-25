dict={}
for i in range(3):
    key=input()
    value=int(input())
    dict[key]=value
print(dict)
m=[]
c=input()
if c=="key":
    d=input()
    if d in dict:
        print(dict[d])
elif c=="value":
    e=input()
    for key, value in dict.items():
        if value==e:
            m.append(key)
print(m)