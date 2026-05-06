"""
break：立即跳出「最內層」迴圈。
continue：略過本次迴圈剩下的敘述，直接進入下一輪。
"""

# break 範例：找到因數就跳出
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

# continue 範例：只處理偶數
for num in range(2, 10):
    if num % 2 != 0:
        continue
    print(f"{num} 是偶數")
