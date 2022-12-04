"""↓ collaborations ↓"""
# a = {}
# print(a)
# print(type(a))

# a = {'a': 1, 'b': 2}
# print(a)

# a = dict([(1, 2), [4, 5]])
# print(a)

# a = {'a': 1}
# a['a'] = 4
# a['b'] = 2
# print(a)

# a = {2: 1}
# print(a)
# a.clear()
# print(a)

# a = {2: 1}
# b = a.copy()
# c = a
# print(b)
# print(b is a)
# print(c is a)

# a = {2: 1}
# print(a.get(2, 3))
# print(a.get(1, 3))

# a = {2: 1, 'a': 4}
# print(a.items())

# a = {2: 1, 'a': 4}
# print(a.keys())
# a = {2: 1, 'a': 4}
# b = a.pop('a')
# print(b)
# print(a)

# a = {2: 1, 'a': 4}
# b = a.popitem()
# print(b)
# print(a)

# a = {2: 1, 'a': 4}
# a.setdefault(3)
# print(a)

# a = {2: 1}
# a.update({'a': 2})
# print(a)

# a = {2: 1, 'a': 2}
# print(a.values())

# a = {2: 1, 'a': 2}
# for key in a:
#     print(key)
# for key, value in a.items():
#     print(key, value)
# for item in a.items():
#     print(item)

# set1 = {1, 3, 4}
# set1.add(2)
# print(set1)

# set2 = {1, 2, 3}
# set2.update([4, 5, 6])
# print(set2)  # {1, 2, 3, 4, 5, 6}

# set1 = {1, 2, 3, 4, 'a', 'p'}
# set1.remove(2)
# print(set1)

# list1 = [1, 2, 1, 3]
# list1 = set(list1)
# list1 = list(list1)
# print(list1)

# dict_a = {1: 10, 2: 20}
# dict_b = {3: 30, 4: 40}
# dict_c = {5: 50, 6: 60}
# result = {}
# for d in (dict_a, dict_b, dict_c):
#     result.update(d)


"""↓ personal work ↓"""
dict_a = {1: 10, 2: 20}
dict_b = {3: 30, 4: 40}
dict_c = {5: 50, 6: 60}
dict_a.update(dict_b)
dict_a.update(dict_c)
print(dict_a)
