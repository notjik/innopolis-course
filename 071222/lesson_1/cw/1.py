"""↓ collaborations ↓"""

# def draw_box():
#     for _ in range(5):
#         print('*' * 7)
#
#
# draw_box()
# print()
# draw_box()
# print()
# draw_box()


# def print_message():
#     print('Я - Артур,')
#     print('король британцев. ')
#
#
# print_message()


# def draw_box(height, width):  # функция принимает два параметра
#     for i in range(height):
#         print('*' * width)
#
#
# draw_box(3, 3)
# print()
# draw_box(5, 5)
# print()
# draw_box(4, 10)

# def func(side1, side2):
#     area = side1 * side2
#     perimetr = (side1 + side2) * 2
#     print(area, perimetr)


"""↓ personal work ↓"""


# def s_and_p(a: float, b: float) -> None:
#     print(a * b, (a + b) * 2)


def s_and_p(*args) -> None:
    a = int(args[0])
    b = int(args[-1])
    print(a * b, (a + b) * 2)


while True:
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')
    if a.strip().isdigit() and b.strip().isdigit():
        s_and_p(a, b)
        break
