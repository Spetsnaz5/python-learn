"""
json：JSON 序列化 / 反序列化

json.dumps(obj)       物件 -> 字串
json.loads(s)         字串 -> 物件
json.dump(obj, fp)    物件 -> 檔案
json.load(fp)         檔案 -> 物件

常用參數：
    indent=2           美化輸出
    ensure_ascii=False 保留中文（不要轉成 \\uXXXX）
    sort_keys=True     鍵名排序
    default=func       自訂不支援型別的轉換方式
"""

import json
from pathlib import Path
from datetime import datetime

data = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "SQL"],
    "active": True,
    "score": None,
}

# 物件 -> 字串
s = json.dumps(data, indent=2, ensure_ascii=False)
print(s)

# 字串 -> 物件
obj = json.loads(s)
print(obj["skills"])

# 物件 -> 檔案 / 檔案 -> 物件
tmp = Path(__file__).with_name("_demo.json")
tmp.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
loaded = json.loads(tmp.read_text(encoding="utf-8"))
print("檔案讀回:", loaded["name"])
tmp.unlink()

# 處理 JSON 不支援的型別：datetime
def json_default(o):
    if isinstance(o, datetime):
        return o.isoformat()
    raise TypeError(f"Type {type(o)} not serializable")

print(json.dumps({"now": datetime.now()}, default=json_default))
