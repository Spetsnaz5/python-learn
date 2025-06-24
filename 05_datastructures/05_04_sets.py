"""
set 是一種無序、元素唯一、可變動的資料型別，常用來去除重複項目、進行集合運算（交集、聯集、差集）等操作。
| 操作                              | 說明                           |
| --------------------------------- | ------------------------------ |
| `items.add("orange")`             | 加入元素                       |
| `items.remove("banana")`          | 移除元素（若不存在會報錯）     |
| `items.discard("mango")`          | 安全移除元素（不存在也不會錯） |
| `items.pop()`                     | 隨機移除並回傳一個元素         |
| `items.clear()`                   | 清空 set                       |
| `items.update([1, 2])`            | 加入多個元素                   |
| `len(items)`                      | 取得元素個數                   |
| `"apple" in items`                | 測試元素是否存在               |
| `set1.union(set2)`                | 聯集                           |
| `set1.intersection(set2)`         | 交集                           |
| `set1.difference(set2)`           | 差集（set1 - set2）            |
| `set1.symmetric_difference(set2)` | 對稱差集                       |
| `set1.issubset(set2)`             | 子集合判斷                     |
| `set1.issuperset(set2)`           | 母集合判斷                     |
| `set1.isdisjoint(set2)`           | 是否無交集                     |
| `set()`                           | 建立空集合                     |
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