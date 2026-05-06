"""
itertools / functools：函式式工具

itertools（迭代器工具）：
    count(start, step)     無限計數
    cycle(iter)            循環
    repeat(x, n)
    chain(a, b, ...)       串接
    islice(it, stop)       切片
    takewhile / dropwhile  條件取/丟
    groupby(iter, key)     連續分組（注意：先排序！）
    product / permutations / combinations
    accumulate(iter, func) 累積（預設加總）

functools：
    reduce(f, iter, init)  聚合
    partial(f, *args)      固定部分參數
    lru_cache / cache      記憶化（函式結果快取）
    cmp_to_key             舊式比較函式 -> key 函式
    wraps                  裝飾器保留原函式 metadata
"""

import itertools as it
import functools as ft

# ---- itertools ----
print(list(it.islice(it.count(10, 2), 5)))          # [10, 12, 14, 16, 18]
print(list(it.chain([1, 2], [3, 4], [5])))          # [1, 2, 3, 4, 5]
print(list(it.accumulate([1, 2, 3, 4])))            # [1, 3, 6, 10]
print(list(it.combinations("ABCD", 2)))             # [('A','B'), ('A','C'), ...]
print(list(it.product([0, 1], repeat=3)))           # 二進位三位數

# groupby 必須先排序
data = [("A", 1), ("A", 2), ("B", 3), ("B", 4), ("A", 5)]
data.sort(key=lambda x: x[0])
for key, group in it.groupby(data, key=lambda x: x[0]):
    print(key, "->", [v for _, v in group])


# ---- functools ----
print(ft.reduce(lambda a, b: a * b, [1, 2, 3, 4]))   # 24 (1*2*3*4)

add = lambda x, y: x + y
add10 = ft.partial(add, 10)
print(add10(5))                                      # 15

# lru_cache：昂貴的遞迴函式自動記憶化
@ft.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(50))                                       # 即刻完成

# wraps：寫裝飾器的必備
def log_call(func):
    @ft.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"call {func.__name__}({args})")
        return func(*args, **kwargs)
    return wrapper

@log_call
def square(x):
    """平方"""
    return x * x

print(square(5))
print(square.__name__, "-", square.__doc__)         # 保留原名稱與 docstring
