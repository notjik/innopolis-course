"""↓ collaborations ↓"""

# numbers = [1, 2, 3, 4]
# result = (x * x for x in numbers)
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
#
# for num in result:
#     print(num)


# f = open('test.txt')
# lines = (t.strip() for t in f)
# comments = (t for t in lines if t[0] == '#')
# for c in comments:
#     print(c)
# comment_list = list(comments)


# def func(num):
#     while num > 0:
#         yield num
#         num -= 1
#
#
# result = func(5)
# print(next(result))
# print(next(result))
# print(result.__next__())
# print(result.__next__())


# import sys
#
# sys.set_int_max_str_digits(23432)
#
#
# def fib(n):
#     fib0 = 1
#     yield fib0
#     fib1 = 1
#     yield fib1
#     for i in range(n - 2):
#         fib0, fib1 = fib1, fib0 + fib1
#         yield fib1
#
#
# for num in fib(112121):
#     pass
# print(num)
