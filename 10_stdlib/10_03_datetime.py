"""
datetime：日期與時間

- date：只有日期
- time：只有時間
- datetime：日期 + 時間
- timedelta：時間差
- timezone：時區（Python 3.9+ 也可用 zoneinfo）

格式化：
    strftime("%Y-%m-%d %H:%M:%S")   物件 -> 字串
    strptime(s, "%Y-%m-%d")         字串 -> 物件
    isoformat() / fromisoformat()   ISO 8601
"""

from datetime import date, datetime, timedelta, timezone

# 當下時間
now = datetime.now()
today = date.today()
print("now   =", now)
print("today =", today)

# 建立指定時間
d = datetime(2025, 1, 1, 8, 30)
print("元旦早上:", d)

# 格式化與解析
print("格式化:", now.strftime("%Y/%m/%d %H:%M:%S"))
parsed = datetime.strptime("2025-04-23 12:00", "%Y-%m-%d %H:%M")
print("解析:", parsed)

# timedelta 運算
print("三天後:", today + timedelta(days=3))
print("距離元旦:", (d.date() - today).days, "天")

# 時區（UTC 與本地）
utc_now = datetime.now(timezone.utc)
print("UTC:", utc_now.isoformat(timespec="seconds"))
