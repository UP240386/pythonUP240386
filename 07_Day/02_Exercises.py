A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#num_1
print(A.union(B))
#num_2
print(A.intersection(B))
#num_3
print(A.issubset(B))
#num_4
print(A.isdisjoint(B))
#num_5
print(A.union(B))
print(B.union(A))
#num_6
print('The symmetrical difference is:',A.symmetric_difference(B))
#num_7
del A
del B