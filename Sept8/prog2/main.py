import random
a = random.randint(0,9999999999)
b = random.randint(0,9999999999)
c = 0
print (f'{a}\n{b}')
if a > b:
    c = random.randint(b,a)
elif b > a:
    c = random.randint(a,b)
else:
    c = random.randint(a-1, b+1)
    print('a = b!')

print (c)