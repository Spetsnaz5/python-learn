"""
ABC 是 abc 模組提供的抽象基底類別，子類若未實作抽象方法，會報錯

@abstractmethod	標記該方法為抽象方法，子類必須實作

繼承 ABC 無法實例化	抽象類別本身不能被直接建立物件
"""

from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def read(self, key):
        pass

    @abstractmethod
    def write(self, key, value):
        pass

class RedisStorage(Storage):
    def read(self, key):
        print(f"從 Redis 讀取 {key}")
    def write(self, key, value):
        print(f"寫入 Redis: {key} = {value}")

class FileStorage(Storage):
    def read(self, key):
        print(f"從檔案讀取 {key}")
    def write(self, key, value):
        print(f"寫入檔案: {key} = {value}")

redis = RedisStorage()
redis.write("name", "Alice")
redis.read("name")

file = FileStorage()
file.write("name", "bill")
file.read("name")


# ------------------------------------------------------------
# 1) 抽象類別不能被實例化
# ------------------------------------------------------------
try:
    Storage()  # ❌ TypeError: Can't instantiate abstract class Storage
except TypeError as e:
    print("無法實例化抽象類別:", e)


# ------------------------------------------------------------
# 2) 子類未實作所有抽象方法 → 一樣不能實例化
# ------------------------------------------------------------
class BrokenStorage(Storage):
    def read(self, key):  # 只實作 read，沒有 write
        pass

try:
    BrokenStorage()  # ❌ TypeError
except TypeError as e:
    print("子類未完整實作:", e)


# ------------------------------------------------------------
# 3) 抽象屬性 / 抽象 classmethod / 抽象 staticmethod
#    @abstractmethod 必須放在最內層（最靠近 def）
# ------------------------------------------------------------
class Shape(ABC):
    @property
    @abstractmethod
    def name(self):
        ...

    @classmethod
    @abstractmethod
    def from_config(cls, cfg):
        ...

    @staticmethod
    @abstractmethod
    def description():
        ...

class Circle(Shape):
    @property
    def name(self):
        return "circle"

    @classmethod
    def from_config(cls, cfg):
        return cls()

    @staticmethod
    def description():
        return "圓形"

c = Circle()
print(c.name, Circle.description())


# ------------------------------------------------------------
# 4) Template Method：抽象類別可以有「具體方法」呼叫抽象方法
#    用來定義固定流程，把可變部分留給子類實作
# ------------------------------------------------------------
class Report(ABC):
    def generate(self):           # 固定流程（具體方法）
        self.load()
        data = self.process()
        self.save(data)

    @abstractmethod
    def load(self): ...
    @abstractmethod
    def process(self): ...
    @abstractmethod
    def save(self, data): ...

class SalesReport(Report):
    def load(self):    print("載入銷售資料")
    def process(self): print("彙總"); return {"total": 100}
    def save(self, data): print("輸出:", data)

SalesReport().generate()


# ------------------------------------------------------------
# 5) 另一種寫法：metaclass=ABCMeta（等效於繼承 ABC）
# ------------------------------------------------------------
from abc import ABCMeta

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def sound(self): ...


# ------------------------------------------------------------
# 6) 子類用 super() 呼叫父類抽象方法的預設邏輯
#    抽象方法仍可有實作內容，子類用 super() 取用
# ------------------------------------------------------------
class Base(ABC):
    @abstractmethod
    def greet(self):
        print("Hello from Base")

class Child(Base):
    def greet(self):
        super().greet()       # 仍可呼叫父類的預設實作
        print("Hello from Child")

Child().greet()

