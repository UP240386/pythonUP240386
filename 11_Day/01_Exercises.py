#num_1
def add_two_numbers(a, b):
    return a + b

#num_2
def area_of_circle(r):
    return 3.14 * r * r

#num_3
def add_all_nums(arr):
    sum_of_nums = 0
    for i in arr:
        if isinstance(i, int):
            sum_of_nums += i
    return sum_of_nums

#num_4
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

#num_5
def check_season(month):
    if month in ["September", "October", "November"]:
        print("Autumn")
    if month in ["December", "January", "February"]:
        print("Winter")
    if month in ["March", "April", "May"]:
        print("Spring")
    else:
        print("Summer")

#num_6
def calculate_slope(x1, x2, y1, y2):
    m = (y2 - y1) / (x2 - x1)
    return m

#num_7
def solve_quadratic_eqn(a, b, c):
    D = b * b - 4 * a * c
    X1 = (-b + D) / (2 * a)
    X2 = (-b - D) / (2 * a)
    print(X1, X2)

#num_8
def print_list(lst):
    for i in lst:
        print(i)

#num_9
def reverse_list(a):
    return a[::-1]

#num_10
def capital_list_terms(a):
    for i in a:
        a[a.index(i)] = i.capitalize()
    return a

#num_11
def add_item(mutable, tba):
    mutable.append(tba)
    return mutable

#num_12
def remove_item(mutable, tbr):
    mutable.remove(tbr)
    return mutable

#num_13
def sum_of_numbers(high):
    sum_of_numbers = 0
    for i in range(high + 1):
        sum_of_numbers += i
    return sum_of_numbers

#num_14
def sum_of_odds(high):
    sum_of_odd_nums = 0
    for i in range(high + 1):
        if i % 2 == 1:
            sum_of_odd_nums += i
    return sum_of_odd_nums

#num_15
def sum_of_even(high):
    sum_of_even_nums = 0
    for i in range(high + 1):
        if i % 2 == 0:
            sum_of_even_nums += i
    return sum_of_even_nums