"""
logging：標準日誌模組

取代 print 來記錄程式狀態，具備：
    - 分級（DEBUG < INFO < WARNING < ERROR < CRITICAL）
    - 格式化（時間、模組、等級、訊息）
    - 多個輸出目的地（console、檔案、網路...）
    - 每個模組獨立的 logger

基本用法：
    logger = logging.getLogger(__name__)
    logger.debug("...") / info / warning / error / exception / critical

設定方式建議：
    一次性腳本 -> logging.basicConfig(...)
    專案     -> dictConfig / fileConfig
"""

import logging

# 最簡易設定
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)

log = logging.getLogger("demo")

log.debug("除錯細節：x=%s", 42)
log.info("程式啟動")
log.warning("磁碟空間剩 10%%")
log.error("連線失敗")

# 記錄例外（自動附 traceback）
try:
    1 / 0
except ZeroDivisionError:
    log.exception("運算出錯")

# 模組化：每個模組有自己的 logger
child = logging.getLogger("demo.child")
child.info("子 logger 訊息會繼承父設定")
