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
print(f"List Comprehension: \n{glossary['List Comprehension']}")
print(f"\nSlice: \n{glossary['Slice']}")
print(f"\nTuple: \n{glossary['Tuple']}")
print(f"\nIndentation: \n{glossary['Indentation']}")
print(f"\nPEP 8: \n{glossary['PEP 8']}")
print(f"\nPEP 257: \n{glossary['PEP 257']}")
