"""
預先定義的清理動作（Predefined Clean-up Actions）

某些物件（如檔案、鎖、網路連線）本身實作了「context manager 協定」
（__enter__ / __exit__），可以透過 with 語句來確保資源在離開區塊時
被自動釋放——即使途中發生例外也一樣。

with expr as name:
    ...
# 離開 with 區塊時，expr.__exit__() 一定會被呼叫

自訂 context manager 有兩種方式：
1. 實作 __enter__ / __exit__ 方法。
2. 使用 contextlib.contextmanager 裝飾產生器。
"""

# --- 1. 使用內建的 with：開檔自動關閉 ---
with open(__file__, "r", encoding="utf-8") as f:
    first_line = f.readline()
print("第一行：", first_line.strip())
# 離開 with 時檔案已自動關閉，不需呼叫 f.close()


# --- 2. 自訂 context manager：類別作法 ---
class Timer:
    def __enter__(self):
        import time
        self.t0 = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        print(f"耗時 {time.perf_counter() - self.t0:.4f}s")
        # 回傳 False / None 讓例外繼續往外傳；回傳 True 會吞掉例外
        return False

with Timer():
    total = sum(range(1_000_000))
print("total =", total)


# --- 3. 自訂 context manager：contextmanager 裝飾器 ---
from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    try:
        yield
    finally:
        print(f"</{name}>")

with tag("h1"):
    print("Hello")


# --- 4. 同時管理多個資源 ---
# with open("a.txt") as a, open("b.txt") as b:
#     ...
