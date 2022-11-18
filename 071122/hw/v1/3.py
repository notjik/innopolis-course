lst = [1, 2, 3, 4, 5, 6]
lst = list(map(lambda x: x // 2, filter(lambda x: not (x % 2), lst)))
print(lst)
