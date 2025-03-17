#num_1
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(set(age)) < len(age))
#La lista es mas grande, ya que "set" quita los elementos repetidos

#num_2
"""
String:It is immutable (you cannot modify a string once it is created), 
It is an ordered sequence of characters, It allows repeated characters.

List: It's mutable (you can modify its elements), 
It's ordered (it maintains the insertion order,
It allows duplicate values.

Tuple: It is immutable (elements cannot be changed once created), 
It is ordered, It allows duplicate values.

Set: It is mutable, but its elements must be immutable, 
It is unordered (the order of elements can change),
Duplicate elements are not allowed.
"""

#num_3
string = 'I am a teacher and I love to inspire and teach people.'
print(len(set(string.split())))