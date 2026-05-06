def risky_operation(user_input):
    if not isinstance(user_input, int):
        raise TypeError("輸入必須是整數")
    if user_input < 0:
        raise ValueError("輸入不得為負數")
    if user_input == 0:
        raise ZeroDivisionError("除以零")
    return 10 / user_input

try:
    result = risky_operation(int(input("請輸入整數: "))) # 1 0 -1
except TypeError as e:
    print("型別錯誤：", e)
except (ValueError, ZeroDivisionError) as e:
    print("數值或除以零錯誤：", e)