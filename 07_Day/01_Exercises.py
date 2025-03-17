#num_1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))
#num_2
it_companies.add('Twitter')
print(it_companies)
#num_3
it_companies.update(['Tesla','Xiaomi','NVIDIA'])
print(it_companies)
#num_4
it_companies.remove('Xiaomi')
print(it_companies)
#num_5
"""
la diferencia entre remove: es que al momento de eliminar un elemento y no lo encuentra, da error; y 
discard: no da ningun tipo de error si no encuentra el elemento
"""