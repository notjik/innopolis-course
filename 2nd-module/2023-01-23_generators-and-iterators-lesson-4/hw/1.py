"""
Напишите выражение-генератор, возводящее в куб числа от 1 до 10 включительно и выведите все значение в виде списка.
"""
generator_expression = (i**3 for i in range(1, 11))
print(list(generator_expression))
