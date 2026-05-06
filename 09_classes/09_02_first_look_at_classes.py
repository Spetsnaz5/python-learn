"""
類別語法初探（A First Look at Classes）

class ClassName:
    <statements>

- class 區塊執行時會建立一個新的 namespace。
- __init__ 是建構子，在 ClassName(...) 時被呼叫，負責初始化實例。
- self 是慣例命名，代表「目前這個實例」，第一個位置參數一定是它。
- 類別變數屬於類別本身；實例變數屬於單一物件。
"""

class Point:
    """平面座標點。"""

    dimension = 2                 # 類別變數（所有 Point 共用）

    def __init__(self, x, y):
        self.x = x                # 實例變數
        self.y = y

    def move(self, dx, dy):
        """平移這個點。"""
        self.x += dx
        self.y += dy

    def __repr__(self):           # 給 print() 好看的輸出
        return f"Point({self.x}, {self.y})"


p = Point(1, 2)
print(p)                          # Point(1, 2)
p.move(10, 5)
print(p)                          # Point(11, 7)

print("dimension =", Point.dimension)   # 透過類別存取
print("dimension =", p.dimension)       # 透過實例存取（Python 會自動往類別找）

# 所有物件都有的內建屬性
print(p.__class__)                # <class '__main__.Point'>
print(p.__dict__)                 # {'x': 11, 'y': 7}
print(Point.__doc__)              # 類別的 docstring
