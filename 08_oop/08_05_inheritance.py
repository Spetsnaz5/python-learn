class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    def greet(self): # 覆寫父類別的方法
        super().greet() # 呼叫父類別
        print("Hello from Child!")

c = Child()
c.greet()  # Hello from Child!

print(isinstance(c, Child))  # True
print(isinstance(c, Parent))  # True
print(issubclass(c.__class__, Parent))  # True


# multiple-inheritance
class A:
    def method(self):
        print("A method")

class B:
    def method(self):
        print("B method")

class C(A, B):
    pass

c = C()
c.method()  # A method ← 預設採用左邊先繼承的類別

print(C.__mro__) # 顯示方法解析順序 (Method Resolution Order, MRO)