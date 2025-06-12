class CountUpTo:
    def __init__(self, max):
        self.max = max
        self.current = 1

    def __iter__(self):  # 取得迭代器
        return self

    def __next__(self):  # 回傳下一個值
        if self.current > self.max:
            raise StopIteration
        else:
            num = self.current
            self.current += 1
            return num

# 使用
for number in CountUpTo(5):
    print(number)