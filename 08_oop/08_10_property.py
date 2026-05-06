class Person:
    def __init__(self, name):
        self._name = name  # _name 是私有變數（約定）
    @property 
    def name(self):         # getter
        return self._name
    @name.setter
    def name(self, value):  # setter
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
        
p = Person("Alice")
print(p.name)        # 👉 呼叫 getter，但像在讀屬性
p.name = "Bob"       # 👉 呼叫 setter，但像在設定屬性
print(p.name)
# p.name = ""        # ❌ ValueError