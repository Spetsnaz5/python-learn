# Python 學習筆記

## 目錄

### 02. 控制流程（Control Flow）
| 檔案 | 主題 |
| ---- | ---- |
| [02_01_if_statements.py](02_controlflow/02_01_if_statements.py) | `if` / `elif` / `else` 條件判斷 |
| [02_02_for_statements.py](02_controlflow/02_02_for_statements.py) | `for` 迴圈與可迭代物件 |
| [02_03_range_function.py](02_controlflow/02_03_range_function.py) | `range()` 函式 |
| [02_04_break_and_continue.py](02_controlflow/02_04_break_and_continue.py) | `break` / `continue` |
| [02_05_else_on_loops.py](02_controlflow/02_05_else_on_loops.py) | 迴圈上的 `else` 子句 |
| [02_06_pass_statements.py](02_controlflow/02_06_pass_statements.py) | `pass` 佔位語句 |
| [02_07_match_statements.py](02_controlflow/02_07_match_statements.py) | `match` / `case` 結構化匹配 |

### 03. 函式（Functions）
| 檔案 | 主題 |
| ---- | ---- |
| [03_01_defining_functions.py](03_functions/03_01_defining_functions.py) | 定義函式、docstring、first-class object |
| [03_02_default_arguments.py](03_functions/03_02_default_arguments.py) | 預設參數值 |
| [03_03_keyword_arguments.py](03_functions/03_03_keyword_arguments.py) | 關鍵字參數 |
| [03_04_special_parameters.py](03_functions/03_04_special_parameters.py) | positional-only `/` 與 keyword-only `*` |
| [03_05_args_kwargs.py](03_functions/03_05_args_kwargs.py) | `*args` / `**kwargs` |
| [03_06_unpacking_arguments.py](03_functions/03_06_unpacking_arguments.py) | `*` / `**` 解包傳入函式 |
| [03_07_lambda.py](03_functions/03_07_lambda.py) | `lambda` 與 `map` / `filter` / `reduce` |
| [03_08_docstrings.py](03_functions/03_08_docstrings.py) | docstring 慣例 |
| [03_09_annotations.py](03_functions/03_09_annotations.py) | 函式型別標註（annotation） |
| [03_10_coding_style.py](03_functions/03_10_coding_style.py) | PEP 8 程式風格 |

### 04. 資料結構（Data Structures）
| 檔案 | 主題 |
| ---- | ---- |
| [04_01_list.py](04_datastructures/04_01_list.py) | List 列表 |
| [04_02_del.py](04_datastructures/04_02_del.py) | `del` 語句 |
| [04_03_tuples.py](04_datastructures/04_03_tuples.py) | Tuple 元組 |
| [04_04_sets.py](04_datastructures/04_04_sets.py) | Set 集合 |
| [04_05_dict.py](04_datastructures/04_05_dict.py) | Dictionary 字典 |
| [README.md](04_datastructures/README.md) | 四種資料結構對照表 |

### 05. 模組（Modules）
| 檔案 | 主題 |
| ---- | ---- |
| [05_01_modules.py](05_modules/05_01_modules.py) | `import` 與自訂模組 |
| [05_02_standard.py](05_modules/05_02_standard.py) | 標準模組導覽 |
| [05_03_dir.py](05_modules/05_03_dir.py) | `dir()` 檢視模組內容 |

### 06. 輸入輸出（Input / Output）
| 檔案 | 主題 |
| ---- | ---- |
| [06_01_output.py](06_io/06_01_output.py) | f-string 與 `str.format()` |
| [06_02_files.py](06_io/06_02_files.py) | 檔案讀寫 |

### 07. 錯誤與例外（Errors and Exceptions）
| 檔案 | 主題 |
| ---- | ---- |
| [07_01_syntax_errors.py](07_errors/07_01_syntax_errors.py) | 語法錯誤 vs 例外 |
| [07_02_exceptions.py](07_errors/07_02_exceptions.py) | 例外總覽與常見型別 |
| [07_03_handling_exceptions.py](07_errors/07_03_handling_exceptions.py) | `try`/`except`/`else`/`finally` |
| [07_04_raising_exceptions.py](07_errors/07_04_raising_exceptions.py) | `raise` |
| [07_05_exception_chaining.py](07_errors/07_05_exception_chaining.py) | 例外鏈（`raise ... from ...`）|
| [07_06_user_defined_exceptions.py](07_errors/07_06_user_defined_exceptions.py) | 自訂例外類別 |
| [07_07_clean_up_actions.py](07_errors/07_07_clean_up_actions.py) | `finally` 清理動作 |
| [07_08_predefined_clean_up.py](07_errors/07_08_predefined_clean_up.py) | `with` 與 context manager |
| [07_09_multiple_exceptions.py](07_errors/07_09_multiple_exceptions.py) | 多重例外 |
| [07_10_exception_notes.py](07_errors/07_10_exception_notes.py) | `add_note()`（3.11+）|

### 08. 物件導向（OOP）
| 檔案 | 主題 |
| ---- | ---- |
| [08_01_scopes_and_namespaces.py](08_oop/08_01_scopes_and_namespaces.py) | Scope / Namespace / `global` / `nonlocal` |
| [08_02_first_look_at_classes.py](08_oop/08_02_first_look_at_classes.py) | 類別語法初探 |
| [08_03_classes.py](08_oop/08_03_classes.py) | 類別變數 vs 實例變數 |
| [08_04_class_and_instance_variables.py](08_oop/08_04_class_and_instance_variables.py) | 可變預設值的陷阱與修正 |
| [08_05_inheritance.py](08_oop/08_05_inheritance.py) | 繼承與 `super()` |
| [08_06_private_variables.py](08_oop/08_06_private_variables.py) | name mangling |
| [08_07_odds_and_ends.py](08_oop/08_07_odds_and_ends.py) | `dataclass` / `namedtuple` / `enum` |
| [08_08_iterators.py](08_oop/08_08_iterators.py) | 自訂迭代器 |
| [08_09_generator.py](08_oop/08_09_generator.py) | 產生器 `yield` |
| [08_10_property.py](08_oop/08_10_property.py) | `@property` getter/setter |
| [08_11_private_advanced.py](08_oop/08_11_private_advanced.py) | 雙底線 name mangling 進階 |
| [08_12_mixin.py](08_oop/08_12_mixin.py) | Mixin 多重繼承模式 |
| [08_13_abstract.py](08_oop/08_13_abstract.py) | `abc.ABC` 抽象類別 |
| [08_14_classmethod.py](08_oop/08_14_classmethod.py) | `@classmethod` |
| [08_15_staticmethod.py](08_oop/08_15_staticmethod.py) | `@staticmethod` |
| [08_16_getattr.py](08_oop/08_16_getattr.py) | `getattr()` 動態屬性存取 |

### 09. 標準函式庫導覽（Standard Library）
| 檔案 | 主題 |
| ---- | ---- |
| [09_01_os_sys.py](09_stdlib/09_01_os_sys.py) | 作業系統與直譯器資訊 |
| [09_02_pathlib.py](09_stdlib/09_02_pathlib.py) | 路徑操作 |
| [09_03_datetime.py](09_stdlib/09_03_datetime.py) | 日期與時間 |
| [09_04_math_random.py](09_stdlib/09_04_math_random.py) | 數學與亂數 |
| [09_05_json.py](09_stdlib/09_05_json.py) | JSON 序列化 |
| [09_06_re.py](09_stdlib/09_06_re.py) | 正規表達式 |
| [09_07_collections.py](09_stdlib/09_07_collections.py) | `Counter` / `defaultdict` / `deque` |
| [09_08_itertools_functools.py](09_stdlib/09_08_itertools_functools.py) | 函式式工具 |
| [09_09_logging.py](09_stdlib/09_09_logging.py) | 日誌模組 |

## 執行方式

```bash
# 任一檔案皆可單獨執行
python 02_controlflow/02_01_if_statements.py
```

建議使用 Python 3.11 以上版本（部份語法如 `match` 需 3.10+、`exception notes` 需 3.11+）。
