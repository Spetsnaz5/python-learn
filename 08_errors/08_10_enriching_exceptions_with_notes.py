def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        e.add_note("參數 b 不可以是 0，請確認傳入值")
        raise

try:
    divide(10, 0)
except ZeroDivisionError as e:
    print(f"錯誤：{e}")
    raise  # 重拋錯誤，traceback 中會看到附註