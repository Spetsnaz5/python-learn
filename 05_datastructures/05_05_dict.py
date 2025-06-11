"""
dictionary 是一種用來儲存「鍵值對」的資料結構，也稱為 dict。它非常適合用來表示「對應關係」，例如姓名對電話、ID 對物件、設定名稱對值等等。
| 方法               | 說明                           |
| ---------------- | ---------------------------- |
| `.get(key)`      | 安全地取得值                       |
| `.keys()`        | 回傳所有 key                     |
| `.values()`      | 回傳所有 value                   |
| `.items()`       | 回傳 (key, value) 組成的 tuple 列表 |
| `.pop(key)`      | 刪除並回傳某個鍵的值                   |
| `.update(dict2)` | 合併另一個字典                      |
| `.clear()`       | 清空字典                         |
"""

dict = {
    "name": "Alice",
    "age": 30,
    "city": "Taipei"
}

print(dict["name"])  # ➜ Alice

# 使用 .get() 可避免找不到時發生錯誤
print(dict.get("gender"))       # ➜ None
print(dict.get("gender", "N/A"))  # ➜ N/A

dict["age"] = 31       # 修改
dict["gender"] = "F"   # 新增
print(dict)  # ➜ {'name': 'Alice', 'age': 31, 'city': 'Taipei', 'gender': 'F'}

# 刪除
del dict["city"]
dict.pop("age")

# 清空
# dict.clear()

# 檢查 key 是否存在
if "name" in dict:
    print("Yes")

# 遍歷
for key in dict:
    print(key, dict[key])

for key, value in dict.items():
    print(f"{key} ➜ {value}")
    
# dict 的方法
dict(sape=4139, guido=4127, jack=4098) # ➜ {'sape': 4139, 'guido': 4127, 'jack': 4098}

# dict comprehensions
print({x: x**2 for x in (2, 4, 6)}) # {2: 4, 4: 16, 6: 36}