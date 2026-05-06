class MyClass:
    def __init__(self):
        self._hidden = 42  # _ 表示「應該被視為私有」
        self.__secret = "shh" # 雙底線 __ 開頭的變數會被 Python 進行「名稱改寫（name mangling）」，以防止子類別覆寫，避免衝突 (不會改寫以 __ 結尾的名稱)

obj = MyClass()

print(obj._hidden)  # 可以存取，只是慣例上不鼓勵

print(obj._MyClass__secret)  # 真正名稱其實是改寫後的