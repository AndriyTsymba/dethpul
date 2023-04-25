# теорія
a=5
b=10
def swap(a, b):
    a,b = b,a
    return a,b
print(f"до обміну : a= {a}, b  = {b}")
a,b = swap(a,b)
print(f"після обміну : a= {a}, b  = {b}")