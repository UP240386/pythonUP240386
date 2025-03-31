import random

#num_1
def shuffle_list(lst):
    random.shuffle(lst)
    return lst

lst = [2,56,87,23]
print(lst)

print(shuffle_list(lst))


#num_2
def unique_numbers():
   return(random.sample(range(0,9),7))

print(unique_numbers())