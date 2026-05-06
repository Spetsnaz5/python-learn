"""
類別變數 vs 實例變數（延伸 09_03）

類別變數：放在 class 區塊最外層，所有實例共享「同一份」。
實例變數：在 __init__ 中以 self.xxx = ... 定義，每個實例各自一份。

⚠️ 可變（list/dict/set）類別變數極容易被誤用，造成所有實例共享狀態。
"""

# ---- 錯誤示範：共用可變類別變數 ----
class DogBad:
    tricks = []                    # ⚠️ 所有實例共享這個 list

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d1 = DogBad("旺財")
d2 = DogBad("小白")
d1.add_trick("坐下")
d2.add_trick("握手")
print(d1.tricks)   # ['坐下', '握手']  ← 意外混在一起
print(d2.tricks)   # ['坐下', '握手']


# ---- 正確作法：可變狀態放 __init__ ----
class DogGood:
    species = "Canis familiaris"   # 不可變的類別變數 OK

    def __init__(self, name):
        self.name = name
        self.tricks = []           # 每隻狗各自一份

    def add_trick(self, trick):
        self.tricks.append(trick)

a = DogGood("旺財")
b = DogGood("小白")
a.add_trick("坐下")
b.add_trick("握手")
print(a.tricks)   # ['坐下']
print(b.tricks)   # ['握手']


# ---- 技巧：用 @classmethod 當工廠 ----
class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h

    @classmethod
    def square(cls, side):
        return cls(side, side)     # 呼叫 Rectangle(side, side)

s = Rectangle.square(5)
print(s.w, s.h)   # 5 5
