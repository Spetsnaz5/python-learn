"""
定義函式：def name(params): ...

- 第一行可以放 docstring（使用三雙引號），用來描述函式。
- 函式得到的參數採「傳物件參考」（pass by object reference）。
- 沒有 return 或僅寫 return 的函式會回傳 None。
- 函式是「第一類物件」（first-class object），可以被賦值給變數、當參數傳遞、或放進容器。
"""

def fib(n):    # write Fibonacci series less than n
    """
    Print a Fibonacci series less than n.
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)


def fib2(t):
    return t

for i in range(5):
    x, y = fib2((i, i**2))
    print(x, y)
    
