class MyError(Exception):
    """自訂例外類別"""
    pass

raise MyError("這是一個自訂例外")