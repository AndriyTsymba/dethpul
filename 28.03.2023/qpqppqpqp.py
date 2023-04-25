s="Hello world!!!"
print(s*3)
print(s+str(1))
s1=str(123456)
print(s1+s)
print(s[0])
print(s[0]+s1[0])
a=s[6]
print(a)
print(s[:6]+s[:-8])
print(s[2:4])
print(s[::-1])
print(s[::2])
print(s.find("l"))
print(s.rfind("l"))
print(s.replace("world", "OLeg"))
print()
print(s.upper())
print(s.lower())
print(s.count("l"))
"""st="erigj3o04390u0gri"
print(st.isnumeric())
for sss in st:
    print(sss)
    if sss.isnumeric():
        print("+")
    else:
        print(":(")"""
import random
password=""
for i in range(15):
    r=random.choice("odpjwpj93u5t8hfgge")
    password+=r
print(password)