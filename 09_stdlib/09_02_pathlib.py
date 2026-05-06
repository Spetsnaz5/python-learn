"""
pathlib：物件導向的路徑操作（推薦取代 os.path）

常用：
    Path.cwd() / Path.home()
    p = Path("a/b/c.txt")
    p.parent / p.name / p.stem / p.suffix
    p.exists() / p.is_file() / p.is_dir()
    p.read_text(encoding=...) / p.write_text(...)
    p.iterdir() / p.glob("*.py") / p.rglob("*.py")
    p.mkdir(parents=True, exist_ok=True)
    p / "sub" / "file.txt"    # 使用 / 運算子組合路徑
"""

from pathlib import Path

here = Path(__file__).resolve().parent
print("目前檔案:", Path(__file__).name)
print("所在目錄:", here)

# 組合路徑（跨平台，不用管 / \）
target = here / "demo_output" / "hello.txt"
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text("hello pathlib", encoding="utf-8")

print("已寫入:", target)
print("檔案內容:", target.read_text(encoding="utf-8"))
print("父資料夾:", target.parent)
print("副檔名:", target.suffix, "| 無副檔名:", target.stem)

# 列出 10_stdlib 下所有 .py
for py in here.glob("*.py"):
    print(" -", py.name)

# 清理示範檔案
target.unlink()
target.parent.rmdir()
