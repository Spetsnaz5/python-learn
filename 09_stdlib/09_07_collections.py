"""
collections：常用的容器擴充

- Counter        計數器
- defaultdict    有預設值的 dict
- deque          雙端佇列（兩端 O(1) 操作）
- OrderedDict    保留插入順序（3.7+ 後 dict 本身已保留，較少用）
- namedtuple     具名 tuple（見 09_07）
- ChainMap       合併多個 dict 檢視
"""

from collections import Counter, defaultdict, deque, ChainMap

# ---- Counter ----
words = "the quick brown fox jumps over the lazy dog the fox".split()
c = Counter(words)
print(c)                         # Counter({'the': 3, 'fox': 2, ...})
print(c.most_common(3))          # 前三名
print(c["fox"])                  # 2
c.update(["fox", "cat"])
print(c["fox"], c["cat"])        # 3 1


# ---- defaultdict ----
groups = defaultdict(list)       # 找不到 key 時預設值是 []
for name, team in [("Alice", "A"), ("Bob", "B"), ("Carol", "A")]:
    groups[team].append(name)
print(dict(groups))              # {'A': ['Alice', 'Carol'], 'B': ['Bob']}

count = defaultdict(int)
for ch in "banana":
    count[ch] += 1               # 不用先檢查 key
print(dict(count))


# ---- deque ----
d = deque([1, 2, 3])
d.appendleft(0)                  # 頭部插入 O(1)
d.append(4)                      # 尾部插入
print(d)                         # deque([0, 1, 2, 3, 4])
d.popleft()
print(d)                         # deque([1, 2, 3, 4])

# 固定長度：可當 ring buffer / 最近 N 筆記錄
recent = deque(maxlen=3)
for x in range(5):
    recent.append(x)
print(recent)                    # deque([2, 3, 4], maxlen=3)


# ---- ChainMap ----
defaults = {"theme": "light", "lang": "zh-TW"}
user     = {"theme": "dark"}
settings = ChainMap(user, defaults)      # user 優先
print(settings["theme"], settings["lang"])  # dark zh-TW
