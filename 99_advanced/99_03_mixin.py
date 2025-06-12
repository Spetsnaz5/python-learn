"""
Mixin 是一種輔助類別：不是為了單獨實例化，而是用來「混入功能」給其他類別。
使用多重繼承的特性把功能注入主類別，避免重複程式碼。
通常命名為 XxxMixin, 如: LoggableMixin, SerializableMixin。

# Mixin 的設計原則
    單一責任：一個 mixin 負責一個功能。
    不應該單獨使用：不能被單獨實例化。
    不維護 state：不要有自己的 __init__()，或極簡的初始化。
"""

import json

class JsonMixin:
    def to_json(self):
        return json.dumps(self.__dict__)

class Person(JsonMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
print(p.to_json())  # 👉 {"name": "Alice", "age": 30}