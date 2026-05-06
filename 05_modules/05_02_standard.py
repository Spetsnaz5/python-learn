"""
標準模組導覽（Brief Tour of the Standard Library）

Python 「電池內建」（batteries included）。以下是最常用的標準模組：

| 模組           | 用途                         |
| -------------- | --------------------------- |
| os / os.path   | 作業系統介面、路徑處理         |
| pathlib        | 物件導向的路徑 API（推薦）     |
| sys            | 直譯器相關、命令列參數         |
| shutil         | 檔案/目錄高階操作（複製、搬移）|
| glob           | 檔名萬用字元                  |
| argparse       | 命令列參數解析                |
| re             | 正規表達式                    |
| math / random  | 數學與亂數                   |
| statistics     | 基本統計                      |
| datetime       | 日期時間                      |
| time           | 時間戳與延遲                  |
| json / csv     | 資料序列化                    |
| urllib.request | HTTP 請求                    |
| collections    | Counter / deque / namedtuple |
| itertools      | 迭代器工具                    |
| functools      | 函式工具（reduce、lru_cache）|
| logging        | 日誌                         |
| unittest       | 單元測試                      |
| typing         | 型別註記                      |

詳細範例見 10_stdlib/ 章節。
"""

import os
import sys
import math
import random
from datetime import datetime

# os：環境變數與路徑
print("cwd =", os.getcwd())
print("PATH sep =", os.sep)

# sys：命令列參數、版本
print("Python version =", sys.version.split()[0])
print("argv =", sys.argv)

# math / random
print("pi =", math.pi, " sqrt(2) =", math.sqrt(2))
print("random 1~10 =", random.randint(1, 10))
print("random choice =", random.choice(['a', 'b', 'c']))

# datetime
print("now =", datetime.now().isoformat(timespec="seconds"))