#num_1 
import string
import random
def random_user_id():
    str = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=6))
    return str
print(random_user_id())         

#num_2
num_char=int(input("Inggresa la cantidad de caracteres que quieres: "))
num=int(input("Ingresa el valor de ID que quieres generar: "))
def user_id_gen_by_user():
    if((num_char>0) and (num>0)):
        for i in range(1,num+1):
            str = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=num_char))
            print(str)                             
user_id_gen_by_user()


#num_3
def rgb_color_gen():
    r = random.randrange(255)
    g = random.randrange(255)
    b = random.randrange(255)
    str = "rgb({},{},{})".format(r,g,b)
    return(str)


print(rgb_color_gen())