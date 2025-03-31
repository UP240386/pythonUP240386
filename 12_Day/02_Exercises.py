import random 

#num_1
def list_of_hexa_colors():
    str ="#"
    str = str + "%06x" % random.randint(0, 0xFFFFFF)
    return str

print(list_of_hexa_colors())    

#num_2
def list_of_rgb_colors():
    r = lambda: random.randint(0,255)
    str = "rgb({},{},{})".format(r(),r(),r())
    return str

print(list_of_rgb_colors()) 


#num_3
def generate_colors(color_type,num):
    colors=[]
    if(num>0):
     
        if(color_type =="hexa"):
            for i in range(1, num+1):
                str ="#"
                str = str + "%06x" % random.randint(0, 0xFFFFFF)
                colors.append(str)
        elif(color_type =="rgb"):
            r = lambda: random.randint(0,255)
            for i in range(1, num+1):                
                str = "rgb({},{},{})".format(r(),r(),r())
                colors.append(str)

    return colors

print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))