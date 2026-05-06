"""
range(stop) / range(start, stop) / range(start, stop, step)

- 回傳的是一個「惰性序列」（range 物件），不會一次產生所有數字，記憶體友善。
- 支援索引與切片，例如 range(10)[2:5]。
- 常搭配 enumerate() 取得 (index, value)；搭配 zip() 同時走訪多個序列。
"""

for i in range(5):
    print(i)

print(sum(range(10)))      # 0+1+...+9 = 45

print(sum(range(4, 7)))    # 4+5+6 = 15

# enumerate：取得索引
for idx, word in enumerate(['a', 'b', 'c']):
    print(idx, word)

# zip：同時走訪多個序列
for x, y in zip([1, 2, 3], ['a', 'b', 'c']):
    print(x, y)

# reversed：反向走訪
for i in reversed(range(5)):
    print(i)
