# Python 學習筆記

## 目錄

### 04. 控制流程（Control Flow）
| 檔案 | 主題 |
| ---- | ---- |
| [04_01_if_statements.py](04_controlflow/04_01_if_statements.py) | `if` / `elif` / `else` 條件判斷 |
| [04_02_for_statements.py](04_controlflow/04_02_for_statements.py) | `for` 迴圈與可迭代物件 |
| [04_03_the_range_function.py](04_controlflow/04_03_the_range_function.py) | `range()` 函式 |
| [04_04_break_and_continue_statements.py](04_controlflow/04_04_break_and_continue_statements.py) | `break` / `continue` |
| [04_05_else_Clauses_on_Loops.py](04_controlflow/04_05_else_Clauses_on_Loops.py) | 迴圈上的 `else` 子句 |
| [04_06_pass_statements.py](04_controlflow/04_06_pass_statements.py) | `pass` 佔位語句 |
| [04_07_match_statements.py](04_controlflow/04_07_match_statements.py) | `match` / `case` 結構化匹配 |
| [04_08_defining_functions.py](04_controlflow/04_08_defining_functions.py) | 定義函式 |
| [04_09_01 ~ 04_09_08](04_controlflow/) | 進階函式：預設值、關鍵字參數、`*args`/`**kwargs`、lambda、docstring、annotation |
| [04_10_intermezzo_coding_style.py](04_controlflow/04_10_intermezzo_coding_style.py) | PEP 8 程式風格 |

### 05. 資料結構（Data Structures）
| 檔案 | 主題 |
| ---- | ---- |
| [05_01_list.py](05_datastructures/05_01_list.py) | List 列表 |
| [05_02_del.py](05_datastructures/05_02_del.py) | `del` 語句 |
| [05_03_tuples.py](05_datastructures/05_03_tuples.py) | Tuple 元組 |
| [05_04_sets.py](05_datastructures/05_04_sets.py) | Set 集合 |
| [05_05_dict.py](05_datastructures/05_05_dict.py) | Dictionary 字典 |
| [README.md](05_datastructures/README.md) | 四種資料結構對照表 |

### 06. 模組（Modules）
| 檔案 | 主題 |
| ---- | ---- |
| [06_01_modules.py](06_modules/06_01_modules.py) | `import` 與自訂模組 |
| [06_02_standard.py](06_modules/06_02_standard.py) | 標準模組導覽 |
| [06_03_dir.py](06_modules/06_03_dir.py) | `dir()` 檢視模組內容 |

### 07. 輸入輸出（Input / Output）
| 檔案 | 主題 |
| ---- | ---- |
| [07_01_output.py](07_inputoutput/07_01_output.py) | f-string 與 `str.format()` |
| [07_02_files.py](07_inputoutput/07_02_files.py) | 檔案讀寫 |

### 08. 錯誤與例外（Errors and Exceptions）
| 檔案 | 主題 |
| ---- | ---- |
| [08_01_syntax_errors.py](08_errors/08_01_syntax_errors.py) | 語法錯誤 vs 例外 |
| [08_02_exceptions.py](08_errors/08_02_exceptions.py) | 例外總覽與常見型別 |
| [08_03_handling_exceptions.py](08_errors/08_03_handling_exceptions.py) | `try`/`except`/`else`/`finally` |
| [08_04_raising_exceptions.py](08_errors/08_04_raising_exceptions.py) | `raise` |
| [08_05_exception_chaining.py](08_errors/08_05_exception_chaining.py) | 例外鏈（`raise ... from ...`）|
| [08_06_user_defined_exceptions.py](08_errors/08_06_user_defined_exceptions.py) | 自訂例外類別 |
| [08_07_defining_clean_up_actions.py](08_errors/08_07_defining_clean_up_actions.py) | `finally` 清理動作 |
| [08_08_predefined_clean_up.py](08_errors/08_08_predefined_clean_up.py) | `with` 與 context manager |
| [08_09_raising_and_handling_multiple_unrelated_exceptions.py](08_errors/08_09_raising_and_handling_multiple_unrelated_exceptions.py) | 多重例外 |
| [08_10_enriching_exceptions_with_notes.py](08_errors/08_10_enriching_exceptions_with_notes.py) | `add_note()`（3.11+）|

### 09. 類別（Classes）
| 檔案 | 主題 |
| ---- | ---- |
| [09_01_scopes_and_namespaces.py](09_classes/09_01_scopes_and_namespaces.py) | Scope / Namespace / `global` / `nonlocal` |
| [09_02_first_look_at_classes.py](09_classes/09_02_first_look_at_classes.py) | 類別語法初探 |
| [09_03_classes.py](09_classes/09_03_classes.py) | 類別變數 vs 實例變數 |
| [09_04_class_and_instance_variables.py](09_classes/09_04_class_and_instance_variables.py) | 可變預設值的陷阱與修正 |
| [09_05_inheritance.py](09_classes/09_05_inheritance.py) | 繼承與 `super()` |
| [09_06_private_variables.py](09_classes/09_06_private_variables.py) | name mangling |
| [09_07_odds_and_ends.py](09_classes/09_07_odds_and_ends.py) | `dataclass` / `namedtuple` / `enum` |
| [09_08_iterators.py](09_classes/09_08_iterators.py) | 自訂迭代器 |
| [09_09_generator.py](09_classes/09_09_generator.py) | 產生器 `yield` |

### 10. 標準函式庫導覽（Standard Library）
| 檔案 | 主題 |
| ---- | ---- |
| [10_01_os_sys.py](10_stdlib/10_01_os_sys.py) | 作業系統與直譯器資訊 |
| [10_02_pathlib.py](10_stdlib/10_02_pathlib.py) | 路徑操作 |
| [10_03_datetime.py](10_stdlib/10_03_datetime.py) | 日期與時間 |
| [10_04_math_random.py](10_stdlib/10_04_math_random.py) | 數學與亂數 |
| [10_05_json.py](10_stdlib/10_05_json.py) | JSON 序列化 |
| [10_06_re.py](10_stdlib/10_06_re.py) | 正規表達式 |
| [10_07_collections.py](10_stdlib/10_07_collections.py) | `Counter` / `defaultdict` / `deque` |
| [10_08_itertools_functools.py](10_stdlib/10_08_itertools_functools.py) | 函式式工具 |
| [10_09_logging.py](10_stdlib/10_09_logging.py) | 日誌模組 |

### 99. 進階主題（Advanced）
| 檔案 | 主題 |
| ---- | ---- |
| [99_01_property.py](99_advanced/99_01_property.py) | `@property` getter/setter |
| [99_02_private.py](99_advanced/99_02_private.py) | 雙底線 name mangling |
| [99_03_mixin.py](99_advanced/99_03_mixin.py) | Mixin 多重繼承模式 |
| [99_04_abstract.py](99_advanced/99_04_abstract.py) | `abc.ABC` 抽象類別 |
| [99_05_classmethod.py](99_advanced/99_05_classmethod.py) | `@classmethod` |
| [99_06_staticmethod.py](99_advanced/99_06_staticmethod.py) | `@staticmethod` |
| [99_07_getattr.py](99_advanced/99_07_getattr.py) | `getattr()` 動態屬性存取 |

## 執行方式

```bash
# 任一檔案皆可單獨執行
python 04_controlflow/04_01_if_statements.py
```

建議使用 Python 3.11 以上版本（部份語法如 `match` 需 3.10+、`exception notes` 需 3.11+）。
