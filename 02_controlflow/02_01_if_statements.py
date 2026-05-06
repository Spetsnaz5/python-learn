"""
if / elif / else 條件判斷

- 條件可以是任意會回傳布林值（或可被轉為布林）的運算式。
- 邏輯運算子：and、or、not（短路求值）。
- 比較可串接：1 < x < 10 等同 (1 < x) and (x < 10)。
- Python 沒有 switch（3.10 起用 match 取代，見 04_07）。
- Tuple/list 可直接整體比較（逐元素）。
"""

x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
    
    
    
if 1 == 1 and 0 == 0:
    pass
elif 1 == 1 or 0 == 0:
    pass
else:
    pass

x, y = 5, 5
end = (5, 5)
if (x, y) == end:
    print((x, y) == end)
