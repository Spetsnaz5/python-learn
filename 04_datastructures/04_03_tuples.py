"""
tuple 是一種有序、不可變的資料型別，用來儲存多個項目
"""

# 空 tuple
empty = ()

# 一個元素的 tuple（注意逗號）
single = (1,)

# 混合型別
mixed = (1, "two", 3.0)

# 巢狀 tuple
nested = (1, (2, 3), [4, 5])

t = (10, 20, 30)

# 存取元素
print(t[0])  # ➜ 10

# 切片
print(t[1:])  # ➜ (20, 30)

# 遍歷
for item in t:
    print(item)
    
# 為什麼是「不可變」
t = (1, 2, 3) # t[0] = 100  # ❌ TypeError: 'tuple' object does not support item assignment

# 可包含可變物件
t = (1, 2, [3, 4])
t[2][0] = 99
print(t)  # ➜ (1, 2, [99, 4])

# tuple 與 list 互轉
l = [1, 2, 3]
t = tuple(l)
l2 = list(t)
print(t, l2)  # ➜ (1, 2, 3) [1, 2, 3]