"""
例外（Exceptions）總覽

- 例外是「物件」，擁有型別、訊息與 traceback。
- 可以用 isinstance() 或 except 的繼承關係匹配。
- except 子句按宣告順序檢查，第一個匹配的會被執行。

常見例外：
    ValueError         型別對但值不合理           int("abc")
    TypeError          型別不對                  len(3)
    ZeroDivisionError  除以零                    1/0
    IndexError         序列索引超出範圍           [1,2][5]
    KeyError           dict 無此鍵               {}['x']
    AttributeError     物件無此屬性              None.foo
    NameError          變數未定義                print(undef)
    FileNotFoundError  檔案不存在                open("no.txt")
    ImportError        匯入失敗                  import no_mod
    StopIteration      迭代結束
    KeyboardInterrupt  使用者按 Ctrl+C（繼承自 BaseException，不建議隨意捕捉）
"""

# 同一個 except 可匹配多個型別
try:
    raise KeyError("x")
except (KeyError, IndexError) as e:
    print("查詢失敗:", type(e).__name__, e)

# 利用繼承關係一次捕捉
try:
    [1, 2][99]
except LookupError as e:        # LookupError 是 IndexError 與 KeyError 的父類
    print("LookupError:", e)

# 重新拋出
try:
    try:
        1 / 0
    except ZeroDivisionError:
        print("先記錄日誌...")
        raise                    # 不帶參數 -> 重拋目前例外
except ZeroDivisionError as e:
    print("外層收到:", e)
