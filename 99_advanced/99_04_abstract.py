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
