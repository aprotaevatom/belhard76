# # # # # start = 2
# # # # # stop = 44
# # # # # step = 3
# # # # # line_count = 4
# # # # # for i in range(start, stop + 1, step * line_count):
# # # # #     for j in range(i, i + step * line_count - 1, step):
# # # # #         if j <= stop:
# # # # #             print(j, end=" ")
# # # # #         else:
# # # # #             break
# # # # #     print()
# # # #
# # # #
# # # # def foo():
# # # #     print("FOO")
# # # #     print("FOO")
# # # #     print("FOO")
# # # #     print("FOO")
# # # #     return "HELLO", "WORLD"
# # # #
# # # #
# # # # def bar(a, b=None, *args, c=6, **kwargs):
# # # #     print(a)
# # # #     print(b)
# # # #     print(c)
# # # #     print(args)
# # # #     print(kwargs)
# # # #
# # # #
# # # # def baz(e, *, a, b, c, d):
# # # #     print(a)
# # # #     print(b)
# # # #     print(c)
# # # #     print(d)
# # # #     print(e)
# # # #
# # # #
# # # # def fu(a, b, c, d, e):
# # # #     print(a, b, c, d, e)
# # # #
# # # #
# # # # def func(a):
# # # #     a["key"] = "value"
# # # #
# # # #
# # # # # data = {}
# # # # # func(data)
# # # # # print(data)
# # # #
# # # #
# # # # def ll(b, a=None):
# # # #     if a is None:
# # # #         a = []
# # # #     a.append(b)
# # # #     print(a)
# # # #
# # #
# # #
# # # a = 5
# # #
# # #
# # # def foo():
# # #     a = 4
# # #
# # #     def bar():
# # #         nonlocal a
# # #         print(a)
# # #
# # #     bar()
# # #
# # #
# # # # f = globals().get("foo")
# # # # f()
# # #
# # #
# # # # callback
# # # def wrapper(func):
# # #     func()
# # #
# # #
# # # def decorator():
# # #     def wrapped():
# # #         print("wrapped")
# # #
# # #     return wrapped
# #
# #
# # # anonim = lambda x, y: (x * y) ** 2
# #
# #
# # # objs = [3, 4, "-2", -54, 2, 5, "45", "-234"]
# # # # [3, 4, 2, 54, 2, 5, 45, 234]
# # # print(min(objs, key=lambda x: abs(int(x))))
# # # print(objs)
# #
# #
# # def geom_range(start, step, count):
# #     while count:
# #         count -= 1
# #         yield start
# #         start *= step
# #
# #
# # numbers = [1, 2, 3, (1, 2, 3, {1, 2, 3}, 4, 5, 6), 4, 5, 6]
# #
# #
# # def recursive_multiply(numbers):
# #     s = 1
# #     for number in numbers:
# #         if isinstance(number, (int, float)):
# #             s *= number
# #         elif isinstance(number, (list, tuple, set)):
# #             s *= recursive_multiply(number)
# #     return s
#
#
# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"была вызвана функция {func.__name__}")
#         print(f"{args=}")
#         print(f"{kwargs=}")
#         result = func(*args, **kwargs)
#         print(f"{result=}")
#         return result
#
#     return wrapper
#
#
# def decorator(a):
#     def wrapper(func):
#         def wrapped(*args):
#             numbers = [number * a for number in args]
#             return func(*numbers)
#
#         return wrapped
#     return wrapper
#
#
# # @decorator(2)
# # @log
# # def multiply(*args):
# #     m = 1
# #     for i in args:
# #         m *= i
# #     return m
# #
# #
# # print(multiply(1, 2, 3))
#
#
# def bread(func):
#     def wrapped():
#         print("/-------\\")
#         func()
#         print("\\_______/")
#
#     return wrapped
#
#
# def onion(func):
#     def wrapped():
#         print("=========")
#         func()
#         print("=========")
#
#     return wrapped
#
#
# @bread
# @onion
# def beef():
#     print("*********")
#
#
# def foo(x, y):
#     return x ** y
#
#
# numbers = [2, 4, 6, 8, 10]
# result = map(foo, numbers, numbers)
#
#
# # words = ["Hello", "age", "apple", "belhard", "aa"]
# # res = filter(lambda x: len(x) < 5, words)
# # from itertools import zip_longest
# # from functools import reduce
#
# # text = "Hell"
# # numbers = [1, 2, 3, 4, 5]
# # objs = (True, False, None)
# # z = zip_longest(text, numbers, objs, fillvalue="НЕТУ")
# # for i in z:
# #     print(i)
#
# # numbers = [2, 4, 6, 8]
# # result = reduce(lambda x, y: x * y, numbers)
# # print(result)
# from typing import Union, Dict
#
# def foo(a: list[dict]) -> int:
#     return "rdftgyhujiko"
#
#
# data: Dict[str, Union[str, int]] = {}


def foo(a: list, *args: str, **kwargs: list) -> None:
    for i in a:  # type: int
        pass
