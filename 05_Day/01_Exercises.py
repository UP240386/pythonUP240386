#Level 1

#num_1
empty_list = []
#num_2
my_list = [1, 2, 3, 4, 5]
#num_3
list_length = len(my_list)
print("list length:", list_length)
#num_4
first_item = my_list[0]
middle_item = my_list[len(my_list) // 2]
last_item = my_list[-1]
print("first item:", first_item)
print("middle item", middle_item)
print("last item", last_item)
#num_5
mixed_data_types = ["Esteban", 18, 1.75, "Single", "Aguascalientes"]
print("Mixed data list:", mixed_data_types)
#num_6
it_companies = ['Facebook', "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
#num_7
print("list of companies:", it_companies)
#num_8
print("Number of companies:", len(it_companies))
#num_9
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]

print("Firts company:", first_company)
print("Middle company:", middle_company)
print("Last company:", last_company)
#num_10
it_companies[2] = "NVIDIA"
print("list after modified:", it_companies)
#num_11
it_companies.append("Xiaomi")
print("list with one more company:", it_companies)
#num_12
it_companies.insert(len(it_companies) // 2, "Lenovo")
print("List after inserting into the middle:", it_companies)
#num_13
it_companies[1] = it_companies[1].upper()
print("list with google in uppercase:", it_companies)
#num_14
joined_companies = "#;  ".join(it_companies)
print("united companies:", joined_companies)
#num_15
company_to_check = "NVIDIA"
exists = company_to_check in it_companies
print(f"{company_to_check} is it on the list?:", exists)
#num_16
it_companies.sort()
print("ordered list:", it_companies)
#num_17
it_companies.reverse()
print("inverted list:", it_companies)
#num_18
first_three = it_companies[:3]
print("first three companies:", first_three)
#num_19
last_three = it_companies[-3:]
print("last three companies:", last_three)
#num_20
it_companies = it_companies[0:len(it_companies) // 2] + it_companies[len(it_companies) // 2 + 1:]
#num_21
it_companies.pop(0)
print("List after removing the first company:", it_companies)
#num_22
it_companies.pop(len(it_companies) // 2)
#num_23
it_companies.pop()
print("List after removing the last company:", it_companies)
#num_24
it_companies.clear()
print("List after removing all companies:", it_companies)
#num_25
del it_companies
#num_26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print("combined list:", full_stack)
#num_27
full_stack.insert(full_stack.index("Redux") + 1, "Python")
full_stack.insert(full_stack.index("Python") + 1, "SQL")
print("List with Python and SQL added:",full_stack)



#   Level 2

#num_1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print("age min:",ages[0])
print("age max:",ages[-1])
print('Median age',format((ages[len(ages)//2] + ages[~(len(ages)//2)])/2))
print('Average age ',format(sum(ages) / len(ages)))
print('range of the ages:',ages[-1] - ages[0])
print(abs(ages[0] - sum(ages) / len(ages)))
print(abs(ages[-1] - sum(ages) / len(ages)))
countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombia',
    'Comoros',
    'Congo (Brazzaville)',
    'Congo',
    'Costa Rica',
    "Cote d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor Timur)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia, The',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia and Montenegro',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe',
]

#num_1.1
print('Middle country:',[countries[i]for i in range((len(countries) // 2) - (1 if int(len(countries)) % 2 == 0 else 0), len(countries) // 2 + 1)])
#num_2
length = len(countries)
if length % 2 == 0:
    first_half = countries[:length // 2]
    second_half = countries[length // 2:]
else:
    first_half = countries[:length // 2 + 1]
    second_half = countries[length // 2 + 1:]
#num_3
scandic_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway','Denmark'][3:]