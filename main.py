# 6-1 Person library
person = {
    'first_name': 'matilde',
    'last_name': 'thala mønsted svennesen',
    'age': 11,
    'city': 'brabrand',
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])
print("\n")

# 6-2 Favorite number
favorite_numbers = {
    'matilde': 7,
    'henrik': 10,
    'iza': 13
}

num = favorite_numbers['matilde']
print(f"Matilde's favorite number is {num}.")

num = favorite_numbers['henrik']
print(f"Henrik's favorite number is {num}.")

num = favorite_numbers['iza']
print(f"iza's favorite number is {num}.")

print("\n")

# 6-3 Glossary
glossary = {
    'List Comprehension': 'En List Comprehension er kode der genererer en ny liste ud fra en en eksiterende liste, '
                          'f.eks en range(a, b)',
    'Slice': 'Del af en liste, tilgået ved at bruge liste(a:b)',
    'Tuple': 'En liste der ikke kan ændres ved at assigne, såkaldt "immutable" data. Den skal defineres igen, '
             'hvis den skal ændres. En Tuple defineres med () i stedet for en listes [].',
    'Indentation': 'Python bruger ikke, som Java, {} til at indkapsle kode i klasser, funktioner, statements osv, '
                   'men i stedet for kan man bruge tabulator til at fortælle parseren at her kommer en blok kode.',
    'PEP 8': 'K. Reitz har skrevet en style guide til python, der beskriver meget nøjagtigt hvordan koden skal se ud',
    'PEP 257': 'Style guide til Docstrings'
}
print(f"List Comprehension: \n{glossary.get('List Comprehension')}")
print(f"\nSlice: \n{glossary.get('Slice')}")
print(f"\nTuple: \n{glossary.get('Tuple')}")
print(f"\nIndentation: \n{glossary.get('Indentation')}")
print(f"\nPEP 8: \n{glossary.get('PEP 8')}")
print(f"\nPEP 257: \n{glossary.get('PEP 257')}")
print("\n")

# 6-4 Glossary 2.0
glossary = {
    'List Comprehension': 'En List Comprehension er kode der genererer en ny liste ud fra en en eksiterende liste, '
                          'f.eks en range(a, b)',
    'Slice': 'Del af en liste, tilgået ved at bruge liste(a:b)',
    'Tuple': 'En liste der ikke kan ændres ved at assigne, såkaldt "immutable" data. Den skal defineres igen, '
             'hvis den skal ændres. En Tuple defineres med () i stedet for en listes [].',
    'Indentation': 'Python bruger ikke, som Java, {} til at indkapsle kode i klasser, funktioner, statements osv, '
                   'men i stedet for kan man bruge tabulator til at fortælle parseren at her kommer en blok kode.',
    'PEP 8': 'K. Reitz har skrevet en style guide til python, der beskriver meget nøjagtigt hvordan koden skal se ud',
    'PEP 257': 'Style guide til Docstrings',
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
}
for key, definition in glossary.items():
    print(f"\n{key.title()}: \n{definition}")

# 6-5 Rivers
rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
}

for river, country in rivers.items():
    print(f"\n{river.title()}: \n{country}")

for river in rivers.keys():
    print(f"\n{river.title()}")

for country in rivers.values():
    print(f"\n{country.title()}")

# 6-6
print("\n")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is: {language.title()}")

coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']

for coder in coders:
    if coder in favorite_languages.keys():
        print(f"Thank you for taking the poll: {coder.title()}")
    else:
        print(f"\t{coder.title()}, what is your favorite language?")
# 6-7 People
# Make an empty list to store people in.
people = []

# Define some people, and add them to the list.
person = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 46,
    'city': 'sitka',
}
people.append(person)

person = {
    'first_name': 'lemmy',
    'last_name': 'matthes',
    'age': 2,
    'city': 'sitka',
}
people.append(person)

person = {
    'first_name': 'willie',
    'last_name': 'matthes',
    'age': 11,
    'city': 'sitka',
}
people.append(person)
print("\n")
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = f"{person['age']}"
    city = f"{person['city'].title()}"
    print(f"{name} of {city}, is {age} years old.")

# 6-8 Pets
# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)

for pet in pets:
    print(f"Here is what i know about {pet['name'].title()}")
    for key, value in pet.items():
        print(f"\t{key}: {value}")

# 6-9 Favorite places
favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'erin': ['hawaii', 'iceland'],
    'willie': ['mt. verstovia', 'the playground', 'new hampshire']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")

# 6-10 Favourite numbers
favorite_numbers = {
    'matilde': [7, 45, 0],
    'henrik': [10, 34, 345, 8],
    'iza': [13, 5, 76, 23]
}
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")
print("\n")

# 6-11 Cities
cities = {
    'santiago': {
        'country': 'chile',
        'population': 6_310_000,
        'nearby mountains': 'andes',
    },
    'talkeetna': {
        'country': 'united states',
        'population': 876,
        'nearby mountains': 'alaska range',
    },
    'kathmandu': {
        'country': 'nepal',
        'population': 975_453,
        'nearby mountains': 'himilaya',
    }
}
for city, info in cities.items():
    counry = info['country'].title()
    population = info['population']
    mountains = info['nearby mountains'].title()

    print(f"\n{city.title()} is in {country}")
    print(f"The population is {population}")
    print(f"The nearest mountains are {mountains}")

# 6-12 Computers

# Example of dictionaries of ready made computers stored in a list
computers = []
computer = {
    'Brand': 'Dell',
    'Type': 'Inspiron 3880 Desktop',
    'CPU': 'Intel Core i5-10400',
    'Memory': '12',
    'MB': 'Ethernet, WIFI, Bluetooth',
    'GPU': 'Onboard',
    'Storage': '256GB SSD',
    'Software': 'None',
    'Price': 589.99
}
computers.append(computer)

computer = {
    'Brand': 'Dell',
    'Type': 'Inspiron 3880 Desktop',
    'CPU': 'Intel Core i7-10700',
    'Memory': '12',
    'MB': 'Ethernet, WIFI, Bluetooth',
    'GPU': 'Onboard',
    'Storage': '512GB SSD',
    'Software': 'Windows',
    'Price': 929.99
}
computers.append(computer)

computer = {
    'Brand': 'HP',
    'Type': 'Spectre x360 Laptop',
    'CPU': 'Intel Core i7-6500',
    'Memory': '8',
    'MB': 'WIFI, Bluetooth, Card reader, Touch screen',
    'GPU': 'Onboard',
    'Storage': '256 SSD',
    'Software': 'Windows 10',
    'Price': 1600
}
computers.append(computer)

computer = {
    'Brand': 'Føniks',
    'Type': 'Gamer Computer Bundle',
    'CPU': 'Intel Core i5-10400F',
    'Memory': '8',
    'MB': 'WIFI, Bluetooth',
    'GPU': 'Nvidia GTX 1650 4GB',
    'Storage': '500 GB SSD',
    'Software': 'None',
    'Price': 800
}
computers.append(computer)

for computer in computers:
    print(f"Here's what i recommend from {computer['Brand'].title()}")
    for key, value in computer.items():
        print(f"\t{key}: \t{value}")
    print("\n")

# Computers with optional choices
custom_computers = []
custom_computer = {
    'Brand': 'Dell',
    'Type': 'Inspiron 3880 Desktop',
    'CPU': 'Intel Core i5-10400',
    'Memory': '12',
    'MB': 'Ethernet, WIFI, Bluetooth',
    'GPU': 'Onboard',
    'Storage': '256GB SSD',
    'Software': 'None',
}
custom_computers.append(computer)

custom_computer = {
    'Brand': 'Dell',
    'Type': 'Inspiron 3880 Desktop',
    'CPU': 'Intel Core i7-10700',
    'Memory': '12',
    'MB': 'Ethernet, WIFI, Bluetooth',
    'GPU': 'Onboard',
    'Storage': '512GB SSD',
    'Software': 'Windows',
}
custom_computers.append(computer)

custom_computer = {
    'Brand': 'HP',
    'Type': 'Spectre x360 Laptop',
    'CPU': 'Intel Core i7-6500',
    'Memory': '8',
    'MB': 'WIFI, Bluetooth, Card reader, Touch screen',
    'GPU': 'Onboard',
    'Storage': '256 SSD',
    'Software': 'Windows 10',
}
custom_computers.append(computer)

custom_computer = {
    'Brand': 'Føniks',
    'Type': 'Gamer Computer Bundle',
    'CPU': 'Intel Core i5-10400F',
    'Memory': '8',
    'MB': 'WIFI, Bluetooth',
    'GPU': 'Nvidia GTX 1650 4GB',
    'Storage': '500 GB SSD',
    'Software': 'None',
}
custom_computers.append(computer)

# her bør arbejdes lidt mere med kap 6
