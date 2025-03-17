#num_1
dog = dict()

#num_2
dog = {"name": "Dumbo", "color": "Black", "breed": "Basset hound", "legs": 4, "age": 14}

#num_3
student_dictionary = {
    "first_name": "Alita",
    "last_name": "Yoko",
    "gender": "W",
    "age": 22,
    "marital_status": "unmarried",
    "skills": ["battle angel"],
    "country": "EEUU",
    "city": "Iron city",
    "address": "earth 26",
}

#num_4
print(len(student_dictionary))

#num_5
print(student_dictionary["skills"])
print(type(student_dictionary["skills"]))

#num_6
student_dictionary["skills"].append("Sleeping")

#num_7
list_keys = list(student_dictionary.keys())

#num_8
list_values = list(student_dictionary.values())

#num_9
list_of_tuples = [(k, v) for k, v in student_dictionary.items()]

#num_10
student_dictionary.pop("marital_status")

#num_11
del dog