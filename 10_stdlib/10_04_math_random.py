"""
math / random / statistics

math     數學常數與函式（sqrt, log, sin, gcd, factorial...）
random   偽亂數（可重現：random.seed()）
statistics  基本統計（mean, median, stdev...）

⚠️ random 不具密碼學強度，安全相關用 secrets 模組。
"""

import math
import random
import statistics

# ---- math ----
print("pi =", math.pi, "| e =", math.e)
print("sqrt(2) =", math.sqrt(2))
print("log(100, 10) =", math.log(100, 10))
print("gcd(12, 18) =", math.gcd(12, 18))
print("factorial(5) =", math.factorial(5))
print("floor(3.7)=", math.floor(3.7), " ceil(3.2)=", math.ceil(3.2))

# ---- random ----
random.seed(42)                              # 設定種子可重現
print("random()      =", random.random())   # 0~1
print("randint(1,10) =", random.randint(1, 10))
print("uniform(0,1)  =", random.uniform(0, 1))
print("choice        =", random.choice(['a', 'b', 'c']))
print("sample        =", random.sample(range(10), 3))

nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print("shuffled      =", nums)

# ---- statistics ----
data = [1, 2, 2, 3, 4, 5, 5, 5, 6]
print("mean   =", statistics.mean(data))
print("median =", statistics.median(data))
print("mode   =", statistics.mode(data))
print("stdev  =", round(statistics.stdev(data), 3))
