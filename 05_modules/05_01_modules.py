# 匯入整個模組並重新命名
import my_math.my_math as math
# 匯入模組中的指定函式
from my_math.my_math import add

if __name__ == "__main__":
    #print(__name__)
    
    print(math.add(10, 30))

    print(math.sub(10, 30))

    print(add(100, 50))