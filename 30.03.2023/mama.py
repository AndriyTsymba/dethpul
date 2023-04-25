a='AbeCeda'
for i in range(len(a)):
    if a[i] in 'aeiouAEIUO':
        #print(a[i])
        print(end='*')
    else:
        print(a[i], end='')
#spiski nabir dannyh
colors=['red', 'blue', 'purple', 2334, 756.55, True]
print(colors)
print(colors[0] + colors[1], colors[-1])
colors[0]='pink'
print(colors)
numbers=[1, 34, 56, 77, 55, 5]
print(colors + numbers)
print(type(numbers))
print(type(colors))
print(list("12345678"))
numbers.append(5)
print(numbers)
#ryadki i spiski
text="Hello! world"
l=text.split("!")
print(l)
new_text="!".join(i.upper() for i in l)
print(new_text)
char_count=sum(i in '! _H' for i in text)
print(char_count)
#zbir znachen v spisok
numbers=input().split(' ')
numbers=[int(i) for i in numbers]
print(numbers)