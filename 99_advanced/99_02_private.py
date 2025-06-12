class MyClass:
    def __init__(self):
        self.__private_var = 42

    def __do_something(self): # 雙底線 __ 開頭的變數會被 Python 進行名稱改寫
        print("This is a private method.")

    def public_method(self):
        self.__do_something()

obj = MyClass()
obj.public_method()         # 正常呼叫，輸出: This is a private method.
# obj.__do_something()      # AttributeError: 'MyClass' object has no attribute '__do_something'
obj._MyClass__do_something() # 可用這種方式呼叫，但不建議