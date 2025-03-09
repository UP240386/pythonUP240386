# Level 1

#num_1
empty = tuple()
#num_2
sisters = ('Anna', 'Elsa')
brothers = ('Kristoff', 'Oaken')
#num_3
siblings = sisters + brothers
#num_4
print('Number of my siblings:',len(siblings))
family_members = siblings + ('Agnarr', 'Iduna')
print('My family:',family_members)


# Level 2

#num_1
*sibs, father, mother = family_members
print('My sibs:',sibs)
print('My father:',father)
print('My mother:',mother)
#num_2
fruits = ('banana', 'apple')
vegetables = ('Cabbage', 'Cauliflower')
animal_products = ('Milk', 'Leather')
food_stuff_tp = fruits + vegetables + animal_products
#num_3
food_stuff_lt = list(food_stuff_tp)
#num_4
food_stuff_lt = food_stuff_lt[:len(food_stuff_lt) // 2] + food_stuff_lt[len(food_stuff_lt) // 2 + 1:]
food_stuff_tp = tuple(food_stuff_lt)
#num_5
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[len(food_stuff_lt) - 3:]
print(food_stuff_lt)
print(first_three)
print(last_three)
#num_6
del food_stuff_tp
#num_7
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)