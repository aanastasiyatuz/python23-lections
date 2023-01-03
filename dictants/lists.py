db = [
    ['Nastya', 13, 'Mentor'],
    ['Aigerim', 21, 'Python dev'],
    ['Nurkamila', 56, 'Backend dev'],
    ['Eljaz', 9, 'Game dev'],
]

# если возраст > 15
'Hello, name, you are mentor'
# если <= 15
'name, you are young'

# loops
# if - else
# fstrings

for person in db:
    name, age, prof = person
    # name = person[0]
    # age = person[1]
    # prof = person[2]
    if age > 15:
        print(f'Hello, {name}, you are {prof}')
    else:
        print(f'{name}, you are young')