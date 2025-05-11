'''Q14: Write a program that accepts n number from user and
calculate Maximum and Minimum value.'''

a = [2,66,88,44,66,33]

min = a[0]
max = a[0]

for i in a:
    if i>max:
        max = i
    if i<min:
        min = i

print(min)
print(max)