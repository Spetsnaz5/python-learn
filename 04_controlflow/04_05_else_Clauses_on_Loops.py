"""
迴圈的 else 子句：
- 當迴圈「正常結束」（沒有被 break 中斷）時會執行 else。
- 被 break 中斷則「不會」執行 else。
- 常用於「搜尋失敗」場景：在迴圈中找到目標就 break，沒找到則 else 處理。
"""

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} = {x} * {n // x}")
            break
    else:
        # 沒有任何因數被 break 出來 => 質數
        print(n, 'is a prime number')