# try:
#     from orjson import loads, dumps
# except ImportError:
#     from json import loads, dumps
#
# # # with as
# # # from time import sleep
# # #
# # # with (
# # #     open("input.txt", "r", encoding="utf-8") as file,
# # #     open("output.txt", "a", encoding="utf-8") as file2
# # # ):
# # #     while True:
# # #         file2.write("hello\n")
# # #         sleep(1)
# #
# #
# # class A:
# #
# #     def __init__(self):
# #         self.closed = False
# #
# #     def close(self):
# #         print("CLOSED")
# #         self.closed = True
# #
# #     def __enter__(self):
# #         return self
# #
# #     def __exit__(self, exc_type, exc_val, exc_tb):
# #         self.close()
# #         # if exc_type is ValueError:
# #         #     print(f"отловили ValueError с текстом {exc_val}")
# #         #     return True
# #
# #
# # # with A() as a:
# # #     print(a.closed)
# # #     raise ValueError("some value")
# # # print(a.closed)
# # from json import load, loads, dumps, dump
#
# # with open("input.json", "r") as file:
# #     data = loads(file.read())
# #     print(data)
#
# # text = '{"name": "alex"}'
# # сериализация
# # де сериализация
#
# # data = {"name": "alex", "city": "МИНСК"}
# # with open("output.json", "w") as file:
# #     dump(data, file, indent=2, ensure_ascii=False)
#
#
# # with open():
# #     pass
#
# # class ExceptValueError:
# #
# #     def __enter__(self):
# #         return self
# #
# #     def __exit__(self, exc_type, exc_val, exc_tb):
# #         if exc_type is ValueError:
# #             return True
# #
# #
# # with ExceptValueError():
# #     a = int("FYguhjk")
# #
#
# # from yaml import safe_load
# #
# # with open("config.yaml", "r") as file:
# #     data = safe_load(file)
# #     print(data)
# # from configparser import ConfigParser
# #
# # parser = ConfigParser()
# # parser.read(filenames="config.ini")
# # from os import getenv
# # from dotenv import load_dotenv
# #
# # load_dotenv()
# # print(getenv("KEY"))
# from csv import DictReader, DictWriter
#
# with open("input.csv", "w") as file:
#     w = DictWriter(file, fieldnames=["name", "age", "city"])
#     w.writeheader()
#     w.writerows(
#         [
#             {"name": "Alex", "city": "Minsk", "age": 44},
#             {"name": "Alex", "city": "Minsk", "age": 44},
#             {"name": "Alex", "city": "Minsk", "age": 44},
#             {"name": "Alex", "city": "Minsk", "age": 44},
#         ]
#     )
#
#     # r = DictReader(file, delimiter=";")
#     # for line in r:
#     #     print(line)
