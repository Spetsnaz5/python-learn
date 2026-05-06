while True:
    try:
        num = int(input("請輸入一個整數："))
        result = 10 / num
        break
    except ValueError:
        print("輸入不是有效的整數！")
    except ZeroDivisionError:
        print("不能除以 0！")
    except Exception as e:
        print("發生未知錯誤：", e)
    finally:
        print("結束程式。")
