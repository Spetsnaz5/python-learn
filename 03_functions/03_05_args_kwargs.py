# Arbitrary Argument Lists
"""
| 語法         | 名稱         | 接收內容           |
| ---------- | ---------- | -------------- |
| `*args`    | 任意個「位置」參數  | 一個 tuple       |
| `**kwargs` | 任意個「關鍵字」參數 | 一個 dict（鍵=參數名） |
"""

# *args：收集位置參數
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3))        # ➜ 6
print(add_all(10, 20, 30, 40)) # ➜ 100

# **kwargs：收集關鍵字參數
def print_user(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_user(name="Alice", age=30, role="admin")

# 混合用法
def example(a, b, *args, c=0, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("c:", c)
    print("kwargs:", kwargs)

example(1, 2, 3, 4, 5, c=10, d=20, e=30)
