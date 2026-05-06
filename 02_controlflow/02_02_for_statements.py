"""
for 迴圈：針對任一可迭代物件（list、tuple、dict、set、str、檔案、生成器 ...）走訪。

- 不同於 C 的 for，Python 的 for 沒有計數器；要計數請用 range()（見 04_03）或 enumerate()。
- 走訪過程中「修改」原集合容易出錯，建議走訪它的 copy() 或用 list comprehension 產生新集合。
- List comprehension：[expr for x in iterable if cond] — 用來取代常見的「建立新列表」for 迴圈。
"""

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('C', 6), ('D', 1)],
    'C': [('A', 5), ('B', 6), ('E', 2)],
    'D': [('B', 1), ('E', 4), ('F', 3)],
    'E': [('C', 2), ('D', 4), ('G', 1)],
    'F': [('D', 3), ('G', 7)],
    'G': [('E', 1), ('F', 7)]
}


print([node for node in graph])

print([[node] * 3 for node in graph])

print([[node + '-' + node2 for node2 in graph] for node in graph])
