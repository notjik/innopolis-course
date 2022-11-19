x = 5
if x >= 5:
    print('YES')
if x == 5:
    print('YES')
if x != 10:
    print('YES')
else:
    print('NO')

age = int(input('Введите свой возраст: '))
if age >= 14:
    print('Вам больше  14 или 14 лет')
elif age >= 18:
    print('Вам больше или 18 лет')
elif age >= 21:
    print('Вам больше или 21 год')
elif age > 45:
    print('Вам больше 45 лет')

age = 12
if age > 11:
    if age < 15:
        print('Да')

age = 12
if age > 11 and age < 15:
    print('Да')

age = 12
if 11 < age < 15:
    print('Да')

num = int(input('Введите число'))
print('Четное' if num % 2 == 0 else 'Нечетное')

num = int(input())
if num > 100 or num < -100:
    print('-')
else:
    print('+')

num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 > 10 and num2 > 10 and num3 > 10:
    print('yes')
else:
    print('no')
