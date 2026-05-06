"""
os / sys：作業系統與直譯器

os：
- os.getcwd() / os.chdir()
- os.environ：環境變數
- os.listdir(path)：列出目錄內容
- os.makedirs / os.remove / os.rename
- os.path.join / os.path.exists / os.path.splitext（較新 API 建議用 pathlib）

sys：
- sys.argv：命令列參數
- sys.version / sys.version_info
- sys.path：模組搜尋路徑
- sys.exit(code)：結束程式
- sys.stdin / sys.stdout / sys.stderr
"""

import os
import sys

# ---- os ----
print("目前工作目錄:", os.getcwd())
print("使用者 HOME:", os.environ.get("USERPROFILE") or os.environ.get("HOME"))
print("這個檔案所在資料夾:", os.path.dirname(os.path.abspath(__file__)))

# 列出目前目錄前 5 個項目
for name in os.listdir(".")[:5]:
    print(" -", name)

# ---- sys ----
print("Python:", sys.version.split()[0])
print("Platform:", sys.platform)
print("argv:", sys.argv)
print("前 3 個 sys.path:")
for p in sys.path[:3]:
    print(" *", p)
