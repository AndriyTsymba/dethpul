#functions
print("jdsgh", 23456, True) #"jdsgh", 23456, True - arguments
print(list(range(1, 10, 4)))
def function_1():
    ... #pass
print(function_1())
def function_2():
    h="Hello function"
function_2()
def function_3():
    h="Hello"
    c="World"
    return h, c
a=function_3()
print(a)
def function_4(h, c):
    suma=h+c
    print(suma)
function_4(int(input()), int(input()))
def appender(var, lst=[]):
    lst.append(var)
    return print(lst)
appender(input())