# Lists
the_count = [1, 2, 3, 4, 5]
shopping_list = ["Noodles", "Eggrolls", "Milk", "rice",]

print(shopping_list [0])
print(shopping_list [2])

print(len(shopping_list))
# Going through a list
for item in shopping_list:
    print(item)

for num in the_count:
    print (num * 2)

len(shopping_list) #Gives me the length of the list
range(3) #Gives a list of the numbers 0 through 2
range(len(shopping_list)) # A list of every index in a list

for num in range(len(shopping_list)):
    item = shopping_list[num]
    print("The item at index %d is %s" % (num, item))

# Turn things into a list
str1 = "Hello Class!"
listOne = list(str1)
print(listOne)
listOne[11] = '.'
print(listOne)
print("".join(listOne))

# Add things to a list
shopping_list.append("cereal")
print(shopping_list)
shopping_list.append("meat")
print(shopping_list)

# Removing things from a list
shopping_list.remove("meat")
print(shopping_list)
shopping_list.pop(0)
print(shopping_list)

# the string class
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.punctuation)
print(string.digits)

# Dealing with strings
strTwo = "This iS a Very OdD SenTenCe"
lowercase = strTwo. lower()
print(lowercase)


#Dictionaries - Made up the key: Value pairs
dictionary = {'name': 'Lance', 'age': 23, 'height': 5 * 12 + 7}

# Accessing dictionaries
print(dictionary['name'])
print(dictionary['age'])
print(dictionary['height'])


# Adding to a dictionary
dictionary['weight'] = 280
print(dictionary)


large_dictionary = {
    'CA': 'California',
    'FL': 'Florida',
    'OH':  'Ohio'
}

print('Florida')

larger_dictionary = {
    'CA': [
        'Fresno',
        'Sacremento',
        'Los Angeles'
    ],
    'FL': [
        "Tampa",
        "Orlando",
        "Miami"
    ],
    'OH': [
        "Cleavland",
        "Cincinnati",
    ]
}


print(larger_dictionary['FL'])
print(larger_dictionary["FL"][2])
print(larger_dictionary['OH'][1])

largest_dictionary = {
    'CA': {
        'NAME': 'California',
        'POPULATION': 39250000,
        'BORDER ST': [
            'Oregon',
            'Nevada',
            'Arizona'
        ]
    },
    'AZ': {
        'NAME': 'Arizona',
        'POPULATION': 6931000,
        'BORDER ST': [
            'California',
            'Utah',
            'Nevada',
            'New Mexico'
        ]
    },
    'NY': {
        'NAME': "New York",
        'POPULATION': 19750000,
        'BORDER ST': [
            'Vermont',
            'Massachusetts',
            'Connecticut',
            'Pennsylvania',
            'New Jersey'
        ]
    }
}
current_node = largest_dictionary['CA']
print(current_node)
print(current_node['NAME'])
print(current_node['POPULATION'])