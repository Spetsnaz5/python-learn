class Dog:
    name = None # 類別變數
    def __init__(self, name):      # 建構函式
        self.name = name           # 實例變數

    def bark(self):                # 方法
        print(f"{self.name}：汪汪！")
        
d1 = Dog("小黑")
print(d1.name)   # 小黑
d1.bark()        # 小黑：汪汪！

d2 = Dog("小白")
print(d2.name)   # 小白
d2.bark()        # 小白：汪汪！


d3 = Dog("小白")
d3.name = "小黃" # 小白 => 小黃
print(d3.name)   # 小黃
d3.bark()        # 小黃：汪汪！

# 檢視或動態操作實例屬性
print(d1.__dict__)
print(d1.__class__)

class A:
    x = [] # 類別變數，所有實例共享
    def __init__(self, x=None):
        self.x = [] # 實例變數，每次實例化時都會初始化一個新的空列表
        if x is not None:
            self.x.append(x)
class B:
    x = [] # 類別變數，所有實例共享
    def __init__(self, x=None):
        if x is not None:
            self.x.append(x)

a1 = A(1)
a1.x.append(2)  # 修改實例變數 x
a2 = A(3)
a2.x.append(4)  # 修改實例變數 x

print(a1.x, a2.x)

b1 = B(1)
b1.x.append(2)  # 修改類別變數 x
b2 = B(3)
b2.x.append(4)  # 修改類別變數 x

print(b1.x, b2.x)
