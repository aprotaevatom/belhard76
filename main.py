# TASK 3 1
# n = int(input("n="))
# numbers = [2 ** i for i in range(1, n+1)]
# print(numbers)

# TASK 3 2
# text = input()
# symbol_counter = {i: text.count(i) for i in text}

# TASK 3 3
# data = {
#     i: {
#         "name": input(f"name {i}="),
#         "email": input(f"email {i}=")
#     }
#     for i in range(1, int(input("n="))+1)
# }
# print(data)

# a = int(input("a="))
# if a > 0:
#     print("a is positive")
# elif a == 0:
#     print("a is zero")
# else:
#     print("a is negative")

# print(True and True and True and False)
# print(False or False or False or True)
# print(False or True or False)
# print(True or False and True)


# x = True
# y = False
# z = False
# if not x or y:  # 0 + 0 = 0
#     print(1)
# elif not x or not y and z:  # 0 + 1 * 0 = 0 + 0 = 0
#     print(2)
# elif not x or y or not y and x:  # 0 + 0 + 1 * 1 = 1
#     print(3)
# else:
#     print(4)

# print(all([]))
# print(any([]))

# a = "Hello"
# BAD PRACTICE
# if type(a) is str or type(a) is int or type(a) is float:
#     print("string")
# if isinstance(a, (str, int, float)):
# python 3.10+
# if isinstance(a, str | int | float):
#     print("string")

# a = True
# print(isinstance(a, int))
# print(isinstance(a, bool))

# print(issubclass(bool, (int, float)))
# numbers = []
# # GOOD
# if numbers:
#     pass
#
# # SO SO
# if bool(numbers):
#     pass
#
# # BAD
# if bool(numbers) == True:
#     pass
#
# # GOOD?
# if len(numbers) > 0:
#     pass

# a = int(input("a="))
# is_even = "NO" if a % 2 else "YES"
#
# if a % 2:
#     is_even = "NO"
# else:
#     is_even = "YES"

# print(156 or "TEXT")
# print(156 and "TEXT")

# default_value = "default"
# user_value = ""
# data = {
#     # "or": user_value if user_value else default_value,
#     "or": user_value or default_value,
#     # "and": default_value if user_value else user_value
#     "and": user_value and default_value
# }
# print(data)

# numbers = [3, 4, 5, 6, 7]
# for number in numbers:
#     print(number ** 2)

# for i in range(1, 100, 2):
#     print(i)

# numbers = [2, 4, 6, 8, 10]
# for i, j in enumerate(numbers):
#     print(i, j)

# objs = [(1, 2, 3), (4, 5, 6, 10), (7, 8)]
# for i, j, *k in objs:
#     print(i, j, k)

# for i in "hello world":
#     print(i)

# data = {
#     "key1": "value1",
#     "key2": "value2",
#     "key3": "value3",
#     "key4": "value4",
# }
# for key, val in data.items():
#     print(key, val)
# for word in ["hello", "world", "python"]:  # O(n)
#     print(word)
#     for letter in word:  # O(m)
#         print(letter)

# for i in range(1, 7):
#     if i % 7 == 0:
#         break
#     print(i)
# else:
#     print("FINISH!")

# a = 0
# while a < 10:
#     print(a)
#     a += 1

# a = 0
# while True:
#     if a == 10:
#         break
#     a += 1

# for _ in range(10, 100):
    # for _ in range(5):
    #     print(_)
    # print("HELLO")
#


# for i in range(1, 10):
#     i += 5


# numbers = [1, 2, 3, 4]
# for number in numbers.copy():
#     numbers.append(number)

# n = 5
# numbers = [2 ** i for i in range(1, n+1)]
# for i in range(1, n+1):
#     numbers.append(2 ** i)


# n = 5
# numbers = [(2 ** i) if i % 3 == 0 else (2 ** 0) for i in range(1, n+1) if i % 2]
# numbers = [2 ** i for i in range(1, n+1) if i % 2]

# for i in range(1, n+1):
#     if i % 2:
#         if i % 3 == 0:
#             numbers.append(2 ** i)
#         else:
#             numbers.append(2 ** 0)

# data = [("vasya", "vasya@gmail.com"), ("petya", None), ("max", "max@yahoo.con")]
# data = [
#     {
#         "name": name,
#         "email": email
#     }
#     for name, email in data if email
# ]
# print(data)

# numbers = [2, 4, 6, 6, 8, 10]
# for i in range(len(numbers)):
#     if numbers[i] % 4 == 0:
#         del numbers[i]
# i = 0
# while i < len(numbers):
#     if numbers[i] % 3 == 0:
#         del numbers[i]
#     i += 1
#
# print(numbers)

# numbers = [2, 4, 6, 6, 6, 8, 10]
# for number in numbers:
#     if number % 3 == 0:
#         numbers.remove(number)
#
# print(numbers)

# try:
#     a = int(input("a="))
#     b = int(input("b="))
#     c = a / b
# except (ZeroDivisionError, ValueError) as exc:
#     print("введено не число или B равно 0")
# except Exception as e:
#     print(e)
#     print("неизвестная ошибка")
# else:
#     print("в ошибок не было")
# finally:
#     print("выполняется всегда")
# try:
#     a = int(input())
# finally:
#     print("что-то")

# try:
#     exit()
# finally:
#     print("BYE!")

# try:
#     a = int(input("a="))
#     b = int(input("b="))
#     c = a / b
# except (ZeroDivisionError, ValueError):
#     print("неверные данные")
#
# a = input("a=")
# b = input("b=")
# if a.isdigit():
#     a = int(a)
# else:
#     print("не число")
#
# if b.isdigit():
#     b = int(b)
# else:
#     print("не число")
#
# if isinstance(a, int) and isinstance(b, int):
#     c = a / b


# email = "vasya@gmail.com"
# try:
#     email.index("@")
# except:
#     print("email invalid")
# else:
#     print("email valid")
# sobaka_exist = email.find("@")
# if sobaka_exist != -1:
#     print("email valid")

# a = 5
# assert a > 5

# N = 34
# 2 4 6 8 10
# 12 14 16 18 20
# 22 24 26 28 30
# 32 34
