x = 10
del x
# print(x)  # NameError: name 'x' is not defined

# 刪除 list 中的元素（根據索引）
fruits = ["apple", "banana", "cherry"]
del fruits[1]
print(fruits)  # ➜ ['apple', 'cherry']

# 刪除字典中的鍵
person = {"name": "Alice", "age": 30}
del person["age"]
print(person)  # ➜ {'name': 'Alice'}

# 刪除物件屬性
class User:
    def __init__(self):
        self.name = "Bob"
        self.age = 25
        self.id = 1

user = User()
del user.age
print(user.__dict__)
