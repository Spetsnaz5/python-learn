"""
list 有序、可變動的資料結構，可以儲存任意類型的多個項目
| 操作                        | 說明                   |
| --------------------------- | ---------------------- |
| `fruits[0]`                 | 取得第一個元素         |
| `fruits[1:3]`               | 切片從索引 1 到 2      |
| `fruits.append("orange")`   | 加入元素至最後面       |
| `fruits.insert(1, "grape")` | 在索引 1 插入元素      |
| `fruits.remove("banana")`   | 刪除特定元素（第一個） |
| `fruits.pop()`              | 移除並回傳最後一個元素 |
| `fruits.index("cherry")`    | 傳回對應元素的索引位置 |
| `fruits.count("apple")`     | 計算元素出現次數       |
| `fruits.reverse()`          | 原地反轉               |
| `fruits.sort()`             | 原地排序（字母或數字   |
| `new_list = fruits.copy()`  | 複製一份新的 list      |
"""

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', ['banana', 'kiwi']]
for fruit in fruits:
    print(fruit)
    
print(fruits[1])  # apple

print(fruits[1:4])  # ['apple', 'pear', 'banana']

print(fruits[:3])  # ['orange', 'apple', 'pear']

print(fruits[5:])  # ['apple', ['banana', 'kiwi']]

a = [1, 2]
b = [3, 4]
c = a + b
print(c)  # [1, 2, 3, 4]

# List Comprehensions
print([x**2 for x in range(10)])

# List Comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)]) # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# 等同以下
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)