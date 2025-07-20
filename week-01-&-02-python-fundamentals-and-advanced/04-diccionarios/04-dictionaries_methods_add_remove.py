
user = {
    'name': 'Emilio',
    'age': 28,
    'greet': 'Hola Mundo',
    'numbers': [1, 2, 3]
}

# .copy()

user_copy = user.copy()
user_copy['age'] = 20

print(user)
print(user_copy)

# .pop()
user.pop('age')
print(user) # 'name': 'Emilio', 'greet': 'Hola Mundo', 'numbers': [1, 2, 3]

# .popitem()
user.popitem()
print(user) # 'name': 'Emilio', 'greet': 'Hola Mundo'

# .update()
user.update({'name': 'Adriane'})
user.update({'dogs': 2})
print(user) # 'name': 'Adriane', 'greet': 'Hola Mundo', 'dogs': 2

# .append()
user['skills'] = user.get('skills', [])
user['skills'].append('Python')
user['skills'].append('Django')
print(user) # 'name': 'Adriane', 'greet': 'Hola Mundo', 'dogs': 2, 'skills': ['Python', 'Django']