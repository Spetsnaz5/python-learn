# intermezzo-coding-style
"""
PEP 8 — Python 官方程式碼風格指南重點

1. 縮排使用 4 個空格，不要混用 tab 與空格。
2. 每行不超過 79 字元（註解/docstring 建議 72）。
3. 函式、類別定義前後空兩行；類別內方法間空一行。
4. 匯入順序：
   (a) 標準函式庫
   (b) 第三方套件
   (c) 本地模組
   每組之間空一行；一行一個 import。
5. 命名慣例：
   - 變數 / 函式 / 模組：snake_case
   - 類別：CapWords（PascalCase）
   - 常數：UPPER_CASE_WITH_UNDERSCORES
   - 「私有」：前綴單底線 _name；name mangling 用雙底線 __name
6. 與 None 比較要用 `is` / `is not`，不要用 `==`。
7. 布林判斷不要寫 `if flag == True:`，直接 `if flag:`。
8. 不要用可變預設值（list/dict/set）當參數預設值，見範例。
9. 字串使用 f-string（Python 3.6+）為首選。
10. 使用 with 開檔確保資源釋放。

工具：
- 格式化：black、ruff format、autopep8
- 靜態檢查：ruff、flake8、pylint
- 型別檢查：mypy、pyright
"""


# ---- 命名範例 ----
MAX_RETRY = 3                    # 常數
class HttpClient:                # 類別：CapWords
    def send_request(self):      # 方法：snake_case
        pass


# ---- 和 None 比較 ----
value = None
if value is None:                # ✅
    pass
# if value == None:              # ❌ 不建議


# ---- 可變預設值陷阱 ----
def bad_append(item, target=[]):     # ❌ 同一個 list 會被所有呼叫共用
    target.append(item)
    return target

print(bad_append(1))   # [1]
print(bad_append(2))   # [1, 2]  ← 驚喜！

def good_append(item, target=None):  # ✅ 用 None 當哨兵
    if target is None:
        target = []
    target.append(item)
    return target

print(good_append(1))  # [1]
print(good_append(2))  # [1]