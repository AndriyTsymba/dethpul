text=input()
l=text.split(". ")
l=[i.capitalize() for i in l]
new_text=". ".join(i for i in l)
print(new_text)
k=0
for i in range(len(new_text)):
    if new_text[i].isnumeric():
        k=k+1
print(k)
k1=0
for i in range(len(new_text)):
    if new_text[i]=="!":
        k1=k1+1
print(k1)
k2=0
for i in range(len(new_text)):
    if new_text[i]=="?" or new_text[i]=="." or new_text[i]=="!":
        k2=k2+1
print(k2)