
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
