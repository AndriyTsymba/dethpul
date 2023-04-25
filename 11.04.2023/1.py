a=input()
b=[]
for i in a:
    if i==".":
        b.append(1)
    if i==",":
        b.append(11)
    if i=="?":
        b.append(111)
    if i=="!":
        b.append(1111)
    if i==":":
        b.append(11111)
    if i=="a":
        b.append(2)
    if i=="b":
        b.append(22)
    if i=="c":
        b.append(222)
    if i=="d":
        b.append(3)
    if i=="e":
        b.append(33)
    if i=="f":
        b.append(333)
    if i=="g":
        b.append(4)
    if i=="h":
        b.append(44)
    if i=="i":
        b.append(444)
    if i=="j":
        b.append(5)
    if i=="k":
        b.append(55)
    if i=="l":
        b.append(555)
    if i=="m":
        b.append(6)
    if i=="n":
        b.append(66)
    if i=="o":
        b.append(666)
    if i=="p":
        b.append(7)
    if i=="q":
        b.append(77)
    if i=="r":
        b.append(777)
    if i=="s":
        b.append(7777)
    if i=="t":
        b.append(8)
    if i=="u":
        b.append(88)
    if i=="v":
        b.append(888)
    if i=="w":
        b.append(9)
    if i=="x":
        b.append(99)
    if i=="y":
        b.append(999)
    if i=="z":
        b.append(9999)
    if i==" ":
        b.append(0)
for i in b:
    print(i, end="")