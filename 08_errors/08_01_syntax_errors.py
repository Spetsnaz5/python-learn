"""
語法錯誤（SyntaxError） vs 例外（Exception）

1. 語法錯誤：程式在「剖析階段」就出問題，連執行都不會開始。
2. 例外：程式語法正確，但執行中遇到異常狀況。可用 try/except 處理。

常見內建例外階層（節錄）：
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 └── Exception
      ├── ArithmeticError  (ZeroDivisionError, OverflowError)
      ├── LookupError      (IndexError, KeyError)
      ├── OSError          (FileNotFoundError, PermissionError)
      ├── TypeError
      ├── ValueError
      ├── AttributeError
      ├── NameError
      ├── ImportError      (ModuleNotFoundError)
      └── StopIteration / RuntimeError ...

慣例：except 盡量捕捉「最具體」的例外型別；避免 bare `except:` 吞掉所有錯誤。
"""

# -- 語法錯誤（此行若取消註解，整個檔案會完全不能執行）--
# while True print('Hello')    # SyntaxError: Missing parentheses

# -- 執行期例外 --
try:
    10 / 0
except ZeroDivisionError as e:
    print("捕捉到例外：", type(e).__name__, "-", e)

try:
    int("abc")
except ValueError as e:
    print("捕捉到例外：", type(e).__name__, "-", e)
