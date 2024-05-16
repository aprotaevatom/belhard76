# class User:
#     group = ""
#
#     def __init__(self, first_name):
#         self.first_name = first_name
#
#     def __str__(self):
#         return "USER"
#
#
# class Manager(User):
#
#     def __init__(self, first_name, last_name):
#         super().__init__(first_name)
#         self.last_name = last_name
#
#     def __str__(self):
#         return "MANAGER"
#
#
# class A:
#     name = "a"
#
#
# class B:
#     _name = "b"
#
#
# class C(A, B):
#     __key = "iehjvefbhi"
#
#     def _get(self, columns, table) -> tuple:
#         pass
#
#     def get(self, columns, table) -> dict:
#         data = self._get(columns=columns, table=table)
#         ...
#         return {}
#
#
# class DebitCard:
#
#     def __init__(self, card_number: str) -> None:
#         self.__card_number = None
#         self.card_number = card_number
#
#     @property
#     def card_number(self) -> str:
#         return self.__card_number[:7] + "** **** ****" + self.__card_number[-4:]
#
#     @card_number.setter
#     def card_number(self, value: str) -> None:
#         if not isinstance(value, str):
#             raise TypeError
#
#         if len(value.replace(" ", "")) != 16:
#             raise ValueError
#
#         if not value.replace(" ", "").isdigit():
#             raise ValueError
#
#         self.__card_number = value
#
#
# class Engine:
#
#     def __init__(self, engine_type: str, volume: int):
#         self.type = engine_type
#         self.volume = volume
#
#
# class Car:
#
#     def __init__(self, engine_type: str, volume: int):
#         self.engine = Engine(engine_type=engine_type, volume=volume)
#
#
# class Car2:
#
#     def __init__(self, engine: Engine):
#         self.engine = engine
#
#
# from abc import ABC, abstractmethod
#
#
# class AbstractDriver(ABC):
#
#     @abstractmethod
#     def get(self, name):
#         pass
#
#     @abstractmethod
#     def upload(self, file):
#         pass
#
#     @classmethod
#     @abstractmethod
#     def download(cls, path):
#         pass
#
#
# class Music(AbstractDriver):
#
#     def upload(self, file):
#         pass
#
#     @classmethod
#     def download(cls, path):
#         pass
#
#     def get(self, name):
#         return name
#
#
# class Movie(AbstractDriver):
#
#     def upload(self, file):
#         pass
#
#     @classmethod
#     def download(cls, path):
#         pass
#
#     def get(self, name):
#         return name
#
#
# # SOLID
# # S - single responsibility principle
# # O - Open/Close principle
# # L - Liskov substitution principle
# # I - interface segregation principle
# # D - dependency inversion principle
#
#
# class AbstractPhone(ABC):
#
#     @abstractmethod
#     def call(self, number):
#         pass
#
#
# class SMSMixin:
#
#     def sms(self, message, number):
#         print(message, number)
#
#
# class MobilePhone(SMSMixin, AbstractPhone):
#     def call(self, number):
#         pass
#
#
# class StaticPhone(AbstractPhone):
#     def call(self, number):
#         pass
#
#
# class AbstractRepository(ABC):
#
#     @abstractmethod
#     def get(self):
#         pass
#
#
# class Repository(AbstractRepository):
#
#     def get(self):
#         pass
#
#
# class Service(AbstractRepository):
#
#     def __init__(self, repository: Repository):
#         self.repository = repository
#
#     def get(self):
#         return self.repository.get()
#
#
# from dataclasses import dataclass
#
#
# @dataclass(frozen=True)
# class Person:
#     name: str
#     surname: str
#     email: str
#
#
# class Cat:
#     __slots__ = ("name", "color")
#
#     def __init__(self, color, name):
#         self.color = color
#         self.name = name
#
#
# class Dog(Cat):
#     __slots__ = ("eye", "__dict__")
#
#
# class Foo:
#
#     def __init_subclass__(cls, **kwargs):
#         # print(kwargs)
#         return cls
#
#
# class Bar(Foo, model="Some Model"):
#     pass
#
#
# class Base:
#     __tablename__: str
#
#     def __init_subclass__(cls, **kwargs):
#         if "tablename" not in kwargs:
#             raise AttributeError
#
#         cls.__tablename__ = kwargs.get("tablename")
#         return cls
#
#
# class Category(Base, tablename="categories"):
#     pass
#
#
#
from copy import deepcopy


def info(self):
    return "CAT"


def constructor(self, name, color):
    self.name = name
    self.color = color


eye = "green"


# Cat = type("Cat", (), {"eye": eye, "__str__": info, "__init__": constructor})
# cat = Cat(name="vasya", color="black")


class Dog(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        attrs["__str__"] = lambda self: "CAT"
        return super().__new__(cls, name, bases, attrs, **kwargs)


class Cat(metaclass=Dog):
    pass


from pydantic import BaseModel, Field


# class Paginator:
#
#     def __class_getitem__(cls, item):
#         return type(
#             f"{item.__name__}Paginator",
#             (BaseModel, ),
#             {
#                 "__annotations__": {
#                     "result": list[item],
#                     "prev": int,
#                     "next": int,
#                     "count": int
#                 },
#                 "result": [],
#                 "prev": 0,
#                 "next": 0,
#                 "count": 0
#             }
#         )
#
#
# class Category(BaseModel):
#     name: str
#
#
# class Product(BaseModel):
#     article: str
#     price: float


class MetaValidator(type):

    def __new__(cls, name, bases, attrs, **kwargs):
        for key, value in attrs.items():
            if key in attrs.get("__annotations__", {}):
                if not isinstance(value, attrs.get("__annotations__", {}).get(key)):
                    try:
                        value = attrs.get("__annotations__", {}).get(key)(value)
                    except ValueError:
                        raise TypeError
                    else:
                        attrs[key] = value
        return super().__new__(cls, name, bases, attrs, **kwargs)


def meta_validator(name, bases, attrs, **kwargs):
    for key, value in attrs.items():
        if key in attrs.get("__annotations__", {}):
            if not isinstance(value, attrs.get("__annotations__", {}).get(key)):
                try:
                    value = attrs.get("__annotations__", {}).get(key)(value)
                except ValueError:
                    raise TypeError
                else:
                    attrs[key] = value
    return type(name, bases, attrs, **kwargs)


class Test(metaclass=meta_validator):
    name: str = 456789
    is_active: bool = 56
    age: int = "66"


print(Test.is_active)
