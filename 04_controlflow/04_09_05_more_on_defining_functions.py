# Unpacking Argument Lists
"""
| 符號   | 用途     | 對應收集語法        |
| ---- | ------ | ------------- |
| `*`  | 解包「序列」 | 對應 `*args`    |
| `**` | 解包「字典」 | 對應 `**kwargs` |
"""

# * 解包序列傳入函式
def add(x, y, z):
    return x + y + z

nums = [1, 2, 3]

print(add(*nums))  # 相當於：add(1, 2, 3)

# ** 解包字典傳入函式
def greet(name, age):
    print(f"{name} is {age} years old.")

info = {"name": "Alice", "age": 30}

greet(**info)  # 相當於：greet(name="Alice", age=30)
