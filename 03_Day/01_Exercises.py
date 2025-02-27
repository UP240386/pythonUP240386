# parte_1
age = 18

# parte_2 
height = float(174)

# parte_3
c_number = complex(3, 4)

# parte_4
print("Area of the triangle:", int(input('Base: ')) * int(input('Height: ')))

# parte_5
print("Perimeter of the triangle:", int(input('a: ')) + int(input('b: ')) + int(input('c: ')))

# parte_6
length = int(input('Enter length: '))
width = int(input('Enter width: '))
print('Area: ', length * width)
print('Perimeter: ', 2 * (length + width))

# parte_7
radius = int(input('Enter radius: '))
print('Area: ', 3.14 * radius * radius)
print('Circumference: ', 2 * 3.14 * radius)

# parte_8
print("X intercept: ", 1)
print("Y intercept: ", -2)
print("Slope: ", 2)

# parte_9
x1, x2, y1, y2 = 2, 6, 2, 10
print('Distance: ')
print('{0:.2f}'.format(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5))
print('Slope:')
print((y2 - y1) / (x2 - x1))

# parte_10
print(2 if 2 < (y2 - y1) / (x2 - x1) else (y2 - y1) / (x2 - x1))

# parte_11
for x in range(0, 10):
    print(x ** 2 + 6 * x + 9)
print(3, -3, "is where y is 0")

# parte_12
print(not len('python') == len('dragon'))

# parte_13
print('on' in 'python' and 'on' in 'dragon')

# parte_14
print('jargon' in "I hope this course is not full of jargon")

# parte_15
print('on' not in 'python' and 'on' in 'dragon')

# parte_16
print(str(float(len('python'))))

# parte_17
number = int(input('Enter number:'))
print("Even" if number % 2 == 0 else "Odd")

# parte_18
value=int(2.7)
print(7//3 == value)

# parte_19
print(type('10') == type(10))

# parte_20
print(int(float('9.8')) == 10)

# parte_21
hours = int(input('Enter hours:'))
rph = int(input('Enter rate per hour:'))
print("Weekly Earning:", hours * rph)

# parte_22
years = int(input('Enter years:'))
print(years * 365 * 24 * 60 * 60 * 60)

# parte_23
for i in range(1, 6):
    print(i, i ** 0, i ** 1, i ** 2, i ** 3)