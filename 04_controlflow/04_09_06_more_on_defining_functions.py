# lambda-expressions
add = lambda x, y: x + y

print(add(2, 3))  # ➜ 5

# map：將每個元素乘以 2
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))  # ➜ [2, 4, 6, 8]
print(doubled)

# filter：只取偶數
even = list(filter(lambda x: x % 2 == 0, nums))  # ➜ [2, 4]
print(even)

# reduce：累加總和（需要先 import）
from functools import reduce
total = reduce(lambda x, y: x + y, nums)  # ➜ 10
print(total)
