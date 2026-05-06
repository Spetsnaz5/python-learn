"""
match / case（結構化模式匹配，Python 3.10+）：
不只是 switch，可以「拆解」型別、序列、字典與屬性。

常用模式：
    case value:                    # 字面值匹配
    case [1, 2, *rest]:            # 序列模式
    case {"name": n, "age": a}:    # 字典模式
    case Point(x=0, y=0):          # 類別模式
    case x if x > 0:               # 帶守衛條件
    case _:                        # 通配 (wildcard)
"""

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 500|501|502|503|504:
            return "Server error"
        case _:#通用字元，永遠不會匹配失敗
            return "Something's wrong with the internet"
        
status = int(input("Please enter http status code: "))

print(http_error(status))


# 「拆解」模式範例
def describe(point):
    match point:
        case (0, 0):
            return "原點"
        case (x, 0):
            return f"在 X 軸上，x={x}"
        case (0, y):
            return f"在 Y 軸上，y={y}"
        case (x, y) if x == y:
            return f"對角線上 ({x}, {y})"
        case (x, y):
            return f"一般點 ({x}, {y})"
        case _:
            return "不是點"

print(describe((0, 0)))
print(describe((3, 0)))
print(describe((2, 2)))
print(describe((1, 4)))
