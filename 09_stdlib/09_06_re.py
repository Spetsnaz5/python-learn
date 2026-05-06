r"""
re：正規表達式

常用函式：
    re.match(p, s)     從字串開頭比對
    re.search(p, s)    在字串中任意位置搜尋第一個匹配
    re.findall(p, s)   回傳所有匹配（list）
    re.finditer(p, s)  回傳所有 match 物件（迭代器）
    re.sub(p, repl, s) 取代
    re.split(p, s)     以 pattern 切分

旗標（flags）：
    re.IGNORECASE / re.MULTILINE / re.DOTALL / re.VERBOSE

常用 meta：
    .  任意字元      \d 數字      \w 字母/數字/底線
    \s 空白          ^  開頭      $  結尾
    *  0+            +  1+        ?  0 或 1
    {n,m}  次數      [] 字元類    () 群組
    (?P<name>...) 具名群組

⚠️ pattern 常含反斜線，建議使用 raw string（r"..."）。
"""

import re

text = "Alice: 25, Bob: 30, Charlie: 35"

# findall 抓所有數字
print(re.findall(r"\d+", text))        # ['25', '30', '35']

# 具名群組
for m in re.finditer(r"(?P<name>\w+): (?P<age>\d+)", text):
    print(m.group("name"), "→", m.group("age"))

# 驗證 email（示意，非嚴謹寫法）
EMAIL = re.compile(r"^[\w.+-]+@[\w-]+\.[\w.-]+$")
for s in ["a@b.com", "not-an-email"]:
    print(s, "→", bool(EMAIL.match(s)))

# 取代
print(re.sub(r"\d+", "#", text))        # Alice: #, Bob: #, Charlie: #

# 切分
print(re.split(r",\s*", text))

# 編譯後重複使用更快
WORD = re.compile(r"\b\w+\b")
print(WORD.findall("Hello, world!"))
