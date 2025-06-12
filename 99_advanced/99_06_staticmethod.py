"""
@staticmethod 是一種不需要傳入 self（實例）或 cls（類別）的靜態方法。它屬於類別的一部分，
但本身不依賴實例或類別的任何狀態，就像「放在類別裡的普通函式」，用來表示它是這個類別的一部分邏輯。

| 特性       | `@staticmethod` | `@classmethod` |
| -------- | --------------- | -------------- |
| 第一個參數    | 無               | `cls`（類別）      |
| 可存取內容    | 無法存取類別或實例屬性     | 可存取/修改類別屬性     |
| 用途       | 工具函式、純邏輯        | 工廠方法、共用設定      |
| 類別/實例可呼叫 | ✅ 都可以           | ✅ 都可以          |
"""

class User:
    def __init__(self, username):
        self.username = username

    @staticmethod
    def is_valid_username(username):
        return username.isalnum()

print(User.is_valid_username("alice123"))  # ➜ True
print(User.is_valid_username("alice!"))    # ➜ False