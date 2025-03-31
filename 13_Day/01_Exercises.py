#num_1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered = [n for n in numbers if(n<=0)]
print(filtered)


#num_2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
one_dimensional = [x for lst in list_of_lists for l in lst for x in l]
print(one_dimensional)


#num_3
lst = [(a,b,a,a**2,a**3,a**4,a**5) 
        for a in range(0,11)
        for b in [1]
      ]

print(lst)


#num_4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

new_list = [[item[0].upper(),item[0].upper()[:3],item[1].upper()]  for country in countries for item in country ]
print(new_list)


#num_5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

new_list = [
            {'country' : item[0].upper(), 'city' : item[1].upper()}
            for country in countries
            for item in country
]

print(new_list)


#num_6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

new_list = ["{} {}".format(item[0], item[1]) 
            for tuples in names for item in tuples 
           ]

print(new_list)


#num_7
# Lambda function to calculate the slope (m) given two points (x1, y1) and (x2, y2)
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x1 != x2 else None

# Lambda function to calculate the y-intercept (b) given a point (x, y) and a slope (m)
y_intercept = lambda x, y, m: y - m * x

# Example usage:
m = slope(1, 2, 3, 6)  # Calculate slope (m)
b = y_intercept(1, 2, m)  # Calculate y-intercept (b)

print(f"Slope (m): {m}")
print(f"Y-Intercept (b): {b}")