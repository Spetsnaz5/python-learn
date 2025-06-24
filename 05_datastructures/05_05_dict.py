"""
dictionary 是一種用來儲存「鍵值對」的資料結構，也稱為 dict。它非常適合用來表示「對應關係」，例如姓名對電話、ID 對物件、設定名稱對值等等。
| 操作                              | 說明                         |
| --------------------------------- | ---------------------------- |
| `person["name"]`                  | 取得指定鍵的值               |
| `person["age"] = 26`              | 設定或更新指定鍵的值         |
| `person.get("gender", "unknown")` | 安全取得鍵值（若無則回預設） |
| `person.keys()`                   | 回傳所有鍵                   |
| `person.values()`                 | 回傳所有值                   |
| `person.items()`                  | 回傳所有鍵值對               |
| `"name" in person`                | 測試鍵是否存在               |
| `person.update({"age": 30})`      | 批次更新鍵值                 |
| `person.pop("age")`               | 移除指定鍵並回傳其值         |
| `person.popitem()`                | 移除並回傳最後一對鍵值       |
| `del person["name"]`              | 刪除指定鍵                   |
| `person.clear()`                  | 清空所有鍵值                 |
| `len(person)`                     | 取得鍵值對個數               |
| `new_dict = person.copy()`        | 複製一份新的 dict            |
| `dict()`                          | 建立空字典                   |
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