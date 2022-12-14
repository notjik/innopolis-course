"""
Задача 2. Треугольники для детей (100 баллов)
Имя исходного файла triangle.in
Имя выходного файла: triangle.out
Ограничение времени: 1 секунда на тест
Ограничение по памяти: 128 Мб
Семиклассник Арсений Ибатуллин изучает
геометрию. Любознательный Арсений прочитал о признаках подобия треугольников.
Один из признаков звучит так: два треугольника подобны, если стороны одного треугольника пропорции сторонам другого, углы,
лежащие между равны.
Напишите программу, которая по известным сторонам двух прямоугольных треугольников определяет,
являются ли эти треугольники подобными.
Формат входных данных:
На вход программе подается три строки. В каждой из них представлены длины сторон дух прямоугольных треугольников
подлежащих сравнению между собой - для разделенные точкой с запятой. Тройка чисел - это длины сторон одного треугольника,
запись через запятую. Причем в каждой тройке чисел сначала указана длина гипотенузы, а затем д катетов,
Длины катетов являются натуральными числами и не превосходит 10000 Длины гипотенуз указаны с точностью 1 знак после запятой.
Формат выходных данных:
Ваша программа должна сравнить два треугольника в каждой строке и вывести в файл triangle out три соответствующих строки
с вердиктами, В каждой строке программа должна выводить слово similar, если треугольники, описанные в этой строке подобны,
фразу similar and equal, если треугольники одинаковые, и фразу not similar triangles, в случае,
треугольники подобными не являются.
"""
from math import acos
import time

start = time.time()


with open('data/2/triangle.in') as f:
    data = list(map(lambda x: list(map(lambda y: list(map(lambda z: float(z.strip()), y.split(','))), x.split(';'))),
                    f.readlines()))

res = {}
for i, elem in enumerate(data):
    a1, b1, c1 = sorted(elem[0], reverse=True)
    a2, b2, c2 = sorted(elem[1], reverse=True)
    alpha1 = acos((b1 ** 2 + c1 ** 2 - a1 ** 2) / (2 * b1 * c1))
    alpha2 = acos((b2 ** 2 + c2 ** 2 - a2 ** 2) / (2 * b2 * c2))
    beta1 = acos((a1 ** 2 + c1 ** 2 - b1 ** 2) / (2 * a1 * c1))
    beta2 = acos((a2 ** 2 + c2 ** 2 - b2 ** 2) / (2 * a2 * c2))
    gamma1 = acos((a1 ** 2 + b1 ** 2 - c1 ** 2) / (2 * a1 * b1))
    gamma2 = acos((a2 ** 2 + b2 ** 2 - c2 ** 2) / (2 * a2 * b2))
    simular = (alpha1 == alpha2 and beta1 == beta2)
    if simular:
        equal = set(elem[0]) == set(elem[1])
        if equal:
            res[i] = 'similar and equal'
        else:
            res[i] = 'similar'
    else:
        res[i] = 'not similar triangles'

with open('data/2/triangle.out', 'w') as f:
    for i in res:
        f.write('{} {}\n'.format(i, res[i]))

print("Execution time of the program is", time.time() - start)
