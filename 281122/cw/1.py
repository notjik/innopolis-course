"""↓ collaborations ↓"""
# a = [1, 2, 3, 'a', True]
# for i in a:
#     print(i)

# a = [1, 2, 3, 'a', True]
# for i in range(len(a)):
#     print(a[i])

# a = [1, 2, 3, 'a', True]
# print(*a)

# languages = 'Python C# Java'.split()
# print(languages)
# numbers = '1 2 3 4 5'.split()
# print(numbers)

# words = 'To be or not to be that is the question'.split()
# print(words)
# ip = '192.168.1.1'.split('.')
# print(ip)
# terms = '1 + 2 + 3 + 4 = 10'.split(' + ')
# print(terms)

# languages = ' '.join(['Python', 'C#', 'Java'])
# print(languages)
# numbers = ' '.join(['1', '2', '3', '4', '5'])
# print(numbers)
# words = ' '.join(['To', 'be', 'or', 'not', 'to', 'be', 'that', 'is',
#                   'the', 'question'])
# print(words)
# ip = '.'.join(['192', '168', '1', '1'])
# print(ip)
# terms = ' + '.join(['1', '2', '3', '4 = 10'])
# print(terms)

# user_list = input().split()
# print(user_list[1])

# a = ['hello', 'world']
# b = ' '.join(a)
# c = ''
# for letter in a:
#     c += letter
#     c += ' '
# print(b)
# print(c)


"""↓ personal work ↓"""
# print(input('Введите имя и класс: ').split()[-1])

a = ['hello', 'world']
res1 = ' '.join(a)
print(res1)
res2 = ''
for i in a[:-1]:
    res2 += i+' '
res2 += a[-1]
print(res2)


