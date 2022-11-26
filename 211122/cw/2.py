"""↓ collaborations ↓"""

# word = 'hello world'
# print(word.capitalize())

# word = 'hello world'
# print(word.swapcase())

# word = 'hello world'
# print(word.title())

# word = 'HELLO world'
# print(word.lower())

# word = 'HELLO world'
# print(word.upper())

# word = 'hello world'
# print(word.count('l'))

# word = 'hello world'
# print(word.startswith('he'))

# word = 'hello world'
# print(word.endswith('rld'))

# word = 'hello world'
# print(word.find('o'))

# word = 'hello world'
# print(word.index('o'))

# word = '   hello world   '
# print(word.strip())

# word = 'hello world'
# print(word.replace('w', 'wooo'))

# name = input()
# last_name = input()
# correct_name = 'Иван'
# correct_last_name = 'Иванов'
# if name.title() == correct_name and last_name.title() == correct_last_name:
#     print(f'Привет {name.title()} {last_name.title()}')

"""↓ personal work ↓"""
'''Проверка на регистр'''
while True:
    name = input('Ваше имя: ').strip()
    surename = input('Ваша фамилия: ').strip()
    if name == name.title() and surename == surename.title():
        print('Привет %s %s' % (name, surename))
        break
    else:
        print('Введите корректное значение')

'''Исправление написания'''
name = input('Ваше имя: ').split()[0].strip()
surename = input('Ваша фамилия: ').split()[0].strip()
print('Привет, %s %s' % (name.title(), surename.title()))
