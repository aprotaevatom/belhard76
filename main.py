# numbers = [2, 4, 6, 8, 10]
# numbers[0:2] = "Hello"
# print(numbers)
# numbers += numbers
# print(numbers * 23)
# print(len(numbers))

# text = "Hello World"
# s = list(text)
# print(s)

# numbers = [i * 2 for i in "HELLO"]
# print(numbers)

# numbers = [i ** 2 for i in range(101)]
# print(numbers)
# numbers = list(range(101))
# print(numbers)

# numbers = [2, 4, 6, 8]
# numbers.append([1, 2, 3])
# print(numbers)

# a = [1, 2, 3]
# b = a.copy()
# a.append(4)
# print(b)

# a = [[1, 2, 3], 4, 5, 6]
# b = a.copy()
# a[0].append(10)
# print(b)

# a = [1, 2, 3]
# b = []
# b.append(a)
# c = b.copy()
# a.append(4)
# print(b[0] is a is c[0])

# a = []
# a.append(a)
# print(a)
# a = [2, 4, 6, 43, 2, 4]
# print(a.count(2))
# a.extend("HELLO WORLD")
# print(a)

# a = [1, 2, 3, 4, 5, 3, 3, 6]
# a.insert(2, "object")
# print(a)
# b = a.pop(2)
# print(b)
# print(a)
# a.remove(3)
# print(a)
# a.reverse()
# print(a)
# a.sort()
# print(a)


# a = [5, 2, -5, 3, 6, -8, 7, 3, -65, 2]
# a.sort(key=abs)
# print(a)
# a = ["hello", "bye", "worldddd", "apple"]
# a.sort(key=len)
# print(a)

# a = ["apple", "BYE"]
# a.sort(key=str.lower)
# print(a)


# a = [1, 2, 3, 4, 5, 6, 7, 8]
# del a[1:4]
# print(a)

# a = [4, 5, 6, 7]
# print(reversed(a))
# print(sorted(a, reverse=True))


# a = [1, 2, 3, [7, 8, [9, "HELLO", 10], 11, 12, 13], 4, 5, 6, ]
# print(a[3][2][1][-1])

# a = 1, 2, 3, 4, 5
# b = tuple("HELLO")
# print(a)
# print(b)

# not tuple
# a = (i for i in range(10))
# print(a)


# a = (1, 2, 3, 4, (5, 6, [], 7), 8, 9)
# print(a)

# allowed_methods = ("GET", "POST")
# user_method = "PUT"
# print(user_method in allowed_methods)


# def foo():
#     print("foo")


# a = (foo,)
# print(hash(foo))
# from time import sleep
# sleep(60)
# print(hash(foo))


# data = {
#     "name": "Alex",
#     "surname": "Pavlov",
#     1: True
# }
# data2 = {
#     "age": 34,
#     "lang": "ru",
#     "surname": "Maximov"
# }
# print(data | data2)
# print({**data, **data2})

# a = dict([("name", "Alex"), ("languages", ["ru", "en"])])
# print(a)
# a = dict.fromkeys(["name", "city"], "Н/У")
# print(a)

# a = {i: ord(i) for i in "HELLO"}
# print(a)

# data = {
#     "name": "Alex",
#     "city": "Minsk"
# }
# print(data.keys())
# print(list(data))
# print(data.values())
# print(data.items())
# data.update({"city": "Mogilev", "age": 34})
# data |= {"city": "Mogilev", "age": 34}
# print(data)
# print(data.get("city", "Н/У"))
# print(data.setdefault("age"))
# print(data)
# print(data.pop("age", None))
# print(data)
# print(data.popitem())
# print(data)
# data = dict(["ab", "cd", "ef", (1, 4), ((True, False), "booool")])
# print(data)

# data = {
#     (1, 2, []): "tuple"
# }
# print(data[(1, 2, [])])

# a, *b, c = (1, 2, 3, 4, 5)
# print(a)
# print(b)
# print(c)
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [*a, *b]
# print(c)

# print(a := input())
# print(a)

# if (age := int(input())) > 18:
#     print("oldest")

# a = {5, 6, 21, 3, -4, 5, 34, 6, 2, 1, 9, 10}
# print(a)

# a = set("HELLO WORLD")

# from collections import *


# User = namedtuple("User", ("first_name", "last_name", "email"))
#
# vasya = User(first_name="Vasya", last_name="Pupkin", email="vasya@pupkin.com")
# print(vasya.first_name)
# print(vasya.email)
# print(vasya._asdict())

# q = deque([1, 2, 3, 4, 5, 6, 7])
# q.rotate(-2)
# print(q)

# data = defaultdict(list)
# data["age"].extend([1, 2, 3, 4])
# print(data)

# data = OrderedDict({"name": "Alex", "email": "alex@gmail.com", "age": 32})
# data.popitem(last=False)
# data.move_to_end("email", last=True)

# text = "HELLO"
# c = Counter(text)
# print(c.most_common(2))
# print(list(c.elements()))

# data1 = {"a": "B", "c": "D"}
# data2 = {"c": "E", "f": "G"}
#
# chain = ChainMap(data1, data2)
# chain["c"] = "K"
# chain.parents["i"] = "O"
# print(chain)
