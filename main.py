# # # # # # # # # start = 2
# # # # # # # # # stop = 44
# # # # # # # # # step = 3
# # # # # # # # # line_count = 4
# # # # # # # # # for i in range(start, stop + 1, step * line_count):
# # # # # # # # #     for j in range(i, i + step * line_count - 1, step):
# # # # # # # # #         if j <= stop:
# # # # # # # # #             print(j, end=" ")
# # # # # # # # #         else:
# # # # # # # # #             break
# # # # # # # # #     print()
# # # # # # # #
# # # # # # # #
# # # # # # # # def foo():
# # # # # # # #     print("FOO")
# # # # # # # #     print("FOO")
# # # # # # # #     print("FOO")
# # # # # # # #     print("FOO")
# # # # # # # #     return "HELLO", "WORLD"
# # # # # # # #
# # # # # # # #
# # # # # # # # def bar(a, b=None, *args, c=6, **kwargs):
# # # # # # # #     print(a)
# # # # # # # #     print(b)
# # # # # # # #     print(c)
# # # # # # # #     print(args)
# # # # # # # #     print(kwargs)
# # # # # # # #
# # # # # # # #
# # # # # # # # def baz(e, *, a, b, c, d):
# # # # # # # #     print(a)
# # # # # # # #     print(b)
# # # # # # # #     print(c)
# # # # # # # #     print(d)
# # # # # # # #     print(e)
# # # # # # # #
# # # # # # # #
# # # # # # # # def fu(a, b, c, d, e):
# # # # # # # #     print(a, b, c, d, e)
# # # # # # # #
# # # # # # # #
# # # # # # # # def func(a):
# # # # # # # #     a["key"] = "value"
# # # # # # # #
# # # # # # # #
# # # # # # # # # data = {}
# # # # # # # # # func(data)
# # # # # # # # # print(data)
# # # # # # # #
# # # # # # # #
# # # # # # # # def ll(b, a=None):
# # # # # # # #     if a is None:
# # # # # # # #         a = []
# # # # # # # #     a.append(b)
# # # # # # # #     print(a)
# # # # # # # #
# # # # # # #
# # # # # # #
# # # # # # # a = 5
# # # # # # #
# # # # # # #
# # # # # # # def foo():
# # # # # # #     a = 4
# # # # # # #
# # # # # # #     def bar():
# # # # # # #         nonlocal a
# # # # # # #         print(a)
# # # # # # #
# # # # # # #     bar()
# # # # # # #
# # # # # # #
# # # # # # # # f = globals().get("foo")
# # # # # # # # f()
# # # # # # #
# # # # # # #
# # # # # # # # callback
# # # # # # # def wrapper(func):
# # # # # # #     func()
# # # # # # #
# # # # # # #
# # # # # # # def decorator():
# # # # # # #     def wrapped():
# # # # # # #         print("wrapped")
# # # # # # #
# # # # # # #     return wrapped
# # # # # #
# # # # # #
# # # # # # # anonim = lambda x, y: (x * y) ** 2
# # # # # #
# # # # # #
# # # # # # # objs = [3, 4, "-2", -54, 2, 5, "45", "-234"]
# # # # # # # # [3, 4, 2, 54, 2, 5, 45, 234]
# # # # # # # print(min(objs, key=lambda x: abs(int(x))))
# # # # # # # print(objs)
# # # # # #
# # # # # #
# # # # # # def geom_range(start, step, count):
# # # # # #     while count:
# # # # # #         count -= 1
# # # # # #         yield start
# # # # # #         start *= step
# # # # # #
# # # # # #
# # # # # # numbers = [1, 2, 3, (1, 2, 3, {1, 2, 3}, 4, 5, 6), 4, 5, 6]
# # # # # #
# # # # # #
# # # # # # def recursive_multiply(numbers):
# # # # # #     s = 1
# # # # # #     for number in numbers:
# # # # # #         if isinstance(number, (int, float)):
# # # # # #             s *= number
# # # # # #         elif isinstance(number, (list, tuple, set)):
# # # # # #             s *= recursive_multiply(number)
# # # # # #     return s
# # # # #
# # # # #
# # # # # def log(func):
# # # # #     def wrapper(*args, **kwargs):
# # # # #         print(f"была вызвана функция {func.__name__}")
# # # # #         print(f"{args=}")
# # # # #         print(f"{kwargs=}")
# # # # #         result = func(*args, **kwargs)
# # # # #         print(f"{result=}")
# # # # #         return result
# # # # #
# # # # #     return wrapper
# # # # #
# # # # #
# # # # # def decorator(a):
# # # # #     def wrapper(func):
# # # # #         def wrapped(*args):
# # # # #             numbers = [number * a for number in args]
# # # # #             return func(*numbers)
# # # # #
# # # # #         return wrapped
# # # # #     return wrapper
# # # # #
# # # # #
# # # # # # @decorator(2)
# # # # # # @log
# # # # # # def multiply(*args):
# # # # # #     m = 1
# # # # # #     for i in args:
# # # # # #         m *= i
# # # # # #     return m
# # # # # #
# # # # # #
# # # # # # print(multiply(1, 2, 3))
# # # # #
# # # # #
# # # # # def bread(func):
# # # # #     def wrapped():
# # # # #         print("/-------\\")
# # # # #         func()
# # # # #         print("\\_______/")
# # # # #
# # # # #     return wrapped
# # # # #
# # # # #
# # # # # def onion(func):
# # # # #     def wrapped():
# # # # #         print("=========")
# # # # #         func()
# # # # #         print("=========")
# # # # #
# # # # #     return wrapped
# # # # #
# # # # #
# # # # # @bread
# # # # # @onion
# # # # # def beef():
# # # # #     print("*********")
# # # # #
# # # # #
# # # # # def foo(x, y):
# # # # #     return x ** y
# # # # #
# # # # #
# # # # # numbers = [2, 4, 6, 8, 10]
# # # # # result = map(foo, numbers, numbers)
# # # # #
# # # # #
# # # # # # words = ["Hello", "age", "apple", "belhard", "aa"]
# # # # # # res = filter(lambda x: len(x) < 5, words)
# # # # # # from itertools import zip_longest
# # # # # # from functools import reduce
# # # # #
# # # # # # text = "Hell"
# # # # # # numbers = [1, 2, 3, 4, 5]
# # # # # # objs = (True, False, None)
# # # # # # z = zip_longest(text, numbers, objs, fillvalue="НЕТУ")
# # # # # # for i in z:
# # # # # #     print(i)
# # # # #
# # # # # # numbers = [2, 4, 6, 8]
# # # # # # result = reduce(lambda x, y: x * y, numbers)
# # # # # # print(result)
# # # # # from typing import Union, Dict
# # # # #
# # # # # def foo(a: list[dict]) -> int:
# # # # #     return "rdftgyhujiko"
# # # # #
# # # # #
# # # # # data: Dict[str, Union[str, int]] = {}
# # # #
# # # #
# # # # def foo(a: list, *args: str, **kwargs: list) -> None:
# # # #     for i in a:  # type: int
# # # #         pass
# # # #
# # # #
# # # # number = 0
# # # # if number > 0:
# # # #     binary = ""
# # # #     while number >= 0:
# # # #         remainder = number % 2
# # # #         binary = f"{remainder}" + binary
# # # #         number = number // 2
# # # # else:
# # # #     binary = "0"
# # # # print(binary)
# # #
# # # # Код Морзе
# # #
# # # morse_code = {
# # #     'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
# # #     'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
# # #     'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
# # #     'Y': '-.--', 'Z': '--..',
# # #     '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
# # #     '7': '--...', '8': '---..', '9': '----.', " ": " "
# # # }
# # #
# # #
# # # def morse_encode(text: str):
# # #     return " ".join(
# # #         morse_code.get(symbol)
# # #         for symbol in text.upper()
# # #         if symbol in morse_code
# # #     )
# #
# #
# # objs = [3, 4, 5, "Hello", "WORLD", 5, "PYTHON"]
# #
# # for i in range(len(objs) - 1, -1, -1):
# #     if not isinstance(objs[i], str):
# #         objs.pop(i)
# # print(objs)
#
# # Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# # словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# # имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# # пустая строка)
#
# users_data = {
#     1: {'name': 'Иван', 'surname': 'Иванов', 'phone': '123-456-789', 'email': 'ivan@example.com'},
#     2: {'name': 'Петр', 'surname': 'Петров', 'phone': '987-654-321', 'email': 'petr@example.com'},
#     3: {'name': 'Мария', 'surname': 'Сидорова', 'phone': '111-222-333', 'email': 'maria@example.com'},
#     4: {'name': 'Елена', 'surname': 'Павлова', 'phone': '555-666-777', 'email': None},
#     5: {'name': 'Алексей', 'surname': 'Смирнов', 'phone': '999-888-777'},
#     6: {'name': 'Ольга', 'surname': 'Иванова', 'phone': '444-555-666', 'email': 'olga@example.com'},
#     7: {'name': 'Николай', 'surname': 'Кузнецов', 'phone': '333-222-111', 'email': 'nick@example.com'},
#     8: {'name': 'Татьяна', 'surname': 'Федорова', 'phone': '777-888-999', 'email': ''},
#     9: {'name': 'Сергей', 'surname': 'Морозов', 'phone': '666-555-444'},
#     10: {'name': 'Евгения', 'surname': 'Алексеева', 'phone': '000-111-222', 'email': 'evgenia@example.com'}
# }
#
#
# def get_name_without_email(data: dict):
#     for value in data.values():
#         if not value.get("email"):
#             print(value.get("name"))
#
#
# get_name_without_email(users_data)


def vowels_count(text: str) -> int:
    c = 0
    for i in text.lower():
        if i in "aeiou":
            c += 1
    return c
