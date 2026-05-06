"""
雜項（Odds and Ends）：幾個重要但常被忽略的工具。

1. dataclass：自動產生 __init__ / __repr__ / __eq__ 等樣板程式碼。
2. namedtuple：具名欄位的 tuple，不可變、輕量。
3. Enum：列舉型別，避免魔術字串/數字散落程式中。
"""

# ---- 1. dataclass ----
from dataclasses import dataclass, field

@dataclass
class Book:
    title: str
    author: str
    price: float = 0.0
    tags: list = field(default_factory=list)   # ✅ 可變預設值要用 default_factory

b = Book("Fluent Python", "Luciano", 1200)
print(b)                       # Book(title='Fluent Python', author='Luciano', price=1200, tags=[])
print(b == Book("Fluent Python", "Luciano", 1200))   # True，自動產生 __eq__

# frozen=True 可讓 dataclass 不可變（像 tuple）
@dataclass(frozen=True)
class Point:
    x: int
    y: int


# ---- 2. namedtuple ----
from collections import namedtuple

Color = namedtuple("Color", ["r", "g", "b"])
red = Color(255, 0, 0)
print(red.r, red.g, red.b)     # 255 0 0
print(red[0])                  # 255  依然可以像 tuple 索引


# ---- 3. Enum ----
from enum import Enum, auto

class Status(Enum):
    PENDING = auto()
    RUNNING = auto()
    DONE = auto()

s = Status.RUNNING
print(s, s.name, s.value)      # Status.RUNNING RUNNING 2
print(s is Status.RUNNING)     # True

# 在 match 中很好搭配
def describe(st):
    match st:
        case Status.PENDING: return "排隊中"
        case Status.RUNNING: return "執行中"
        case Status.DONE:    return "完成"

print(describe(Status.DONE))
