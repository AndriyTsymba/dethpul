#spiski
my_dict={"red": 12, "pi": 3.14, 2: 2, "False": True}
print(my_dict)
print(type(my_dict))
print(list(my_dict))
my_dict['purple']=345 #dodavannya pary kluch znachennya
print(my_dict)
my_dict['purple']+=1000 #zmina znachennya po zvernennyu po kluchu
print(my_dict)
import random
numbers=[random.randint(1, 10) for i in range(5)]
card={'a': [], 'b': [], 'c': []}
card['a']=numbers
print(card)
dict_1={}
for i in range(3):
    key=int(input(f"vveditb {i+1} kluch "))
    value="value_"+str(i+1)
    dict_1[key]=value
print(dict_1)
#perevirka nayavnosti klucha
if 1 in dict_1:
    print("+")
else:
    print("-")
dict_1.pop(1) #vidalennya
print(dict_1)
#perevirka nayavnosti znachenb
if 'value_3' in dict_1.values():
    print("+++")
else:
    print("---")
#vivid znachenb asociyovanih z kluchem
for value in dict_1:
    print(f"{value}:{dict_1[value]}") #value - vivid yogo klucha. dict_1[value - vivid yogo znachennya
dict_1[key] = 'value_2' #perezapis znachennya ostannyoi pary
print(dict_1)
#zapis usih kluchey z odnakovimy znachennyamy v spisok found key
found_key=[]
for key, value in dict_1.items():
    if value =='value_2':
        found_key.append(key)
print(found_key)