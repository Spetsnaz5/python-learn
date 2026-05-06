"""
命名空間（Namespaces）與 作用域（Scopes）

Namespace：名稱到物件的對應表。Python 中常見的 namespace：
    - 內建（built-in）：print、len ...
    - 模組全域（global）：整個 .py 檔
    - 函式區域（local）：函式內的變數
    - 類別區域：class 內的 body

LEGB 查找順序：Local → Enclosing → Global → Built-in

想在內層函式「寫入」外層變數，需要宣告：
    - global    → 對應「模組全域」
    - nonlocal  → 對應「外一層（非全域）」的區域
"""

# ---- LEGB 範例 ----
x = "global x"

def outer():
    x = "outer x"

    def inner():
        # 只讀取時，Python 會沿 LEGB 找
        print("inner 讀到:", x)

    inner()

outer()
print("外面讀到:", x)


# ---- global：在函式裡修改全域變數 ----
counter = 0

def bump():
    global counter
    counter += 1

bump(); bump(); bump()
print("counter =", counter)   # 3


# ---- nonlocal：修改「上一層」的區域變數 ----
def make_counter():
    n = 0
    def inc():
        nonlocal n
        n += 1
        return n
    return inc

c = make_counter()
print(c(), c(), c())          # 1 2 3 ← 閉包 (closure)


# ---- 注意：在函式裡「賦值」會建立新的 local ----
y = 10
def wrong():
    # print(y)    # ❌ 會報 UnboundLocalError，因為下一行讓 y 變成 local
    y = 20
    print("local y =", y)

wrong()
print("global y =", y)        # 仍是 10
