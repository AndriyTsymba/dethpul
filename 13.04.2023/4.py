"""import random
b=input()
if b=="easy":
    def f1():
        a=[random.randint(-10, 10) for i in range(5)]
        return a
    print(f1())
elif b=="norm":
    def f2():
        b=[random.randint(-10, 10) for i in range(7)]
        return b
    print(f2())
elif b=="hard":
    def f3():
        c=[random.randint(-10, 10) for i in range(10)]
        return c
    print(f3())"""

import random
b=input()
def f1(l):
    a=[random.randint(-10, 10) for i in range(l)]
    print(a)
if b=="easy":
     f1(8)
elif b=="norm":
     f1(16)
elif b=="hard":
      f1(24)