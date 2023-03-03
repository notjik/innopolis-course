'''↓ collaborations ↓'''

# i = 0
# while i < 10:
#     print('Привет')
#     i += 1

# i = 0
# while i < 10:
#     print('Привет')
#     i += 1
#
# num = int(input())
# while num != -1:
#     print('Квадрат вашего числа равен:', num * num)
#     num = int(input())
#
# while True:
#     num = input()
#     if num == 'stop':
#         break

# i = 0
# total = 0
# while i < 10:
#     total += i

# result = 0
# for i in range(10):
#     num = int(input())
#     if num < 0:
#         break
#     result += num
# print(result)

# n = int(input())
# flag = False
# while n != 0:
#     last_digit = n % 10
#     if last_digit == 7:
#         flag = True
#         break
#     n //= 10
# if flag == True:
#     print('Число', n, 'содержит цифру 7')
# else:
#     print('Число', n, 'не содержит цифру 7')

# for i in range(1, 101):
#     if i == 7 or i == 17 or i == 29 or i == 78:
#         continue  # переходим на следующую итерацию
#     print(i)

# for i in range(1, 101):
#     if i != 7 and i != 17 and i != 29 and i != 78:
#         print(i)

# a = 1
# while a < 5:
#     print('условие верно')
#     a = a + 1
# else:
#     print('условие неверно')

# for seconds in range(60):
#     print(seconds)

# for minutes in range(60):
#     for seconds in range(60):
#         print(minutes, ':', seconds)

# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours, ':', minutes, ':', seconds)

# for i in range(3):
#     for j in range(4):
#         print(i, j)

# for i in range(3):
#     for j in range(4):
#         if i == j:
#             break
#         print(i, j)

# for i in range(3):
#     for j in range(4):
#         if i == j:
#             continue
#         print(i, j)

# flag = False
# for i in range(3):
#     for j in range(3):
#         if (j == 1) and (i == 2):
#             flag = True
#             break
#         print(i, j)
#     if flag == True:
#         break

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328,
           615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950,
           626, 949, 687, 217, ]
for x in numbers:
    if x == 237:
        break
    elif x % 2 == 0:
        print(x)
