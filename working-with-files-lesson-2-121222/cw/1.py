"""↓ collaborations ↓"""
# import os
#
# os.system('mkdir test')

# import json
# from pprint import pprint
#
# filename = "file.json"
#
# info = {
#     "ФИО": "Иванов Иван Иванович",
#     "Оценки": {
#         "Математика": 4,
#         "Физика": 5,
#         "Информатика": 5
#     },
#     "Хобби": ["Программирование", "Плавание"],
#     "Возраст": 14,
#     "ДомЖивотные": None
# }
#
# with open(filename, "w", encoding="utf-8") as file:
#     file.write(json.dumps(info, ensure_ascii=False, indent=4))
#
# with open(filename, encoding="utf-8") as file:
#     info_2 = json.loads(file.read())
#
# pprint(info_2)

# import csv
#
# filename = "test.csv"
#
# shop_list = {"картофель": [2, 100], "яблоки": [3, 250], "морковь": [1, 35]}
#
# with open(filename, "w", encoding="utf-8", newline="") as file:
#     writer = csv.writer(file, quoting=csv.QUOTE_ALL)
#     writer.writerow(["Наименование", "Вес", "Цена/кг."])
#     for name, values in sorted(shop_list.items()):
#         writer.writerow([name, *values])
#     writer.writerow(["мука", "4", "70"])
#
# rows = []
# with open(filename, "r", encoding="utf-8") as file:
#     row = list(csv.reader(file))
#
# for row in rows:
#     print(row)

# import pickle
#
# filename = "test.txt"
#
# shop_list = {"овощи": ["картофель", "капуста"],
#              "бакалея": ["мука"],
#              "бюджет": 500}
#
# with open(filename, "wb") as file:
#     pickle.dump(shop_list, file)
#
# with open(filename, "rb") as file:
#     shop_list_2 = pickle.load(file)
# print(shop_list_2)

# import json
#
# dict_person = {}
# while len(dict_person) != 3:
#    name = input('Введите имя: ')
#    age = input('Введите возраст: ')
#    if name not in dict_person:
#        dict_person[name] = age
#    else:
#        print('Данное имя уже существует')
#
# with open('text.txt', "w", encoding="utf-8") as file:
#    file.write(json.dumps(dict_person, ensure_ascii=False, indent=4))

"""↓ personal work ↓"""
'''
Задача 1
Написать программу, которая запрашивает у пользователя имя и возраст и записывает в словарь. 
Ввод продолжается до тех пор, пока количество пар(ключ/значение) в словаре не равно 3. 
Если пользователь ввел повторное имя, то программа должна вывести соответствующее сообщение. 
После окончания ввода данные записываются в файл test.txt в формате json. 
'''
import json

res = {}
while len(res) != 3:
    n, a = input('Введите имя: '), input('Введите возраст: ')
    if a.isdigit() and n.isalpha() and n not in res:
        res[n] = int(a)
    else:
        print('Введите корректные значения')

with open('test.txt', "w", encoding="utf-8") as f:
    f.write(json.dumps(res, ensure_ascii=False, indent=4))
