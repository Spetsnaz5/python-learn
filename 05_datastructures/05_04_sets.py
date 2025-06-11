"""
set 是一種無序、元素唯一、可變動的資料型別，常用來去除重複項目、進行集合運算（交集、聯集、差集）等操作。
"""

# 空 set
empty = set()   # ❗ 不要用 {}，那是空的 dict

# 含重複值，自動去除
nums = {1, 2, 2, 3}
print(nums)  # ➜ {1, 2, 3}

# 字串集合
chars = set("hello")
print(chars)  # ➜ {'h', 'e', 'l', 'o'}（順序不定）

# 加入元素
s = {1, 2}
s.add(3)         # ➜ {1, 2, 3}
s.update([4, 5]) # ➜ {1, 2, 3, 4, 5}

# 遍歷
for item in s:
    print(item)
    
# 移除元素
s.remove(2)      # 若元素不存在會錯
s.discard(10)    # 不存在也不會報錯
s.pop()          # 移除任一元素（無序）
s.clear()        # 清空整個集合

# 集合
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # 聯集：{1, 2, 3, 4, 5}
print(a & b)   # 交集：{3}
print(a - b)   # 差集：{1, 2}
print(a ^ b)   # 對稱差集：{1, 2, 4, 5}

# set comprehensions
a = {x for x in 'abracadabra' if x not in 'abc'} # {'r', 'd'}