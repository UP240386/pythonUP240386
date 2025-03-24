#num_1
print('with for:')
for e in range(11):
    print(e)
print('with while:')
m = 0
while m <= 10:
    print(m)
    m += 1

#num_2
print('with for:')
for e in range(10, -1, -1):
    print(e)

print('with while:')
m = 10
while m >= 0:
    print(m)
    m -= 1

#num_3
print('triangle:')
hash_string = '#'
for e in range(1, 8):
    print(hash_string * e)

#num_4
print('square:')
for e in range(1, 9):
    for m in range(1, 9):
        print("#", end=' ')
    print()

#num_5
print('multiplications:')
for i in range(0, 11):
    print(i, "x", i, "=", i * i)    

#num_6
for lang in ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']:
    print(lang)

#num_7
print('From 0 to 100 showing only even numbers:')
for i in range(0, 101):
    if i % 2 == 0:
        print(i)

#num_8
print('Odd numbers:')
for i in range(0, 101):
    if i % 2 != 0:
        print(i)