class Person:
    def __init__(self):
        self.name = "Alice"
        self.age = 30

p = Person()

print(getattr(p, "name"))      # ➜ Alice
print(getattr(p, "age"))       # ➜ 30
print(getattr(p, "gender", "N/A"))  # ➜ N/A（屬性不存在時使用預設值）