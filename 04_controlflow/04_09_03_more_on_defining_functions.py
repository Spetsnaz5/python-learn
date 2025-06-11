# special-parameters
"""
| 符號  | 用途            |
| --- | ------------- |
| `/` | 前方參數只能位置傳參    |
| `*` | 後方參數只能關鍵字傳參   |
| 無   | 可同時接受位置與關鍵字傳參 |
"""
def greet(name, /):
    print(f"Hello {name}")

# greet("Alice")     #✅ 正確
# greet(name="Bob")  #❌ TypeError: name must be positional-only


def greet2(*, name):
    print(f"Hello {name}")

# greet2(name="Alice") #✅ 正確
# greet2("Bob")        #❌ TypeError: name must be keyword-only

def func(a, b, /, c, d=1, *, e, f=2):
    print(a, b, c, d, e, f)

# func(1, 2, 3, d=4, e=5, f=6)  #✅ 正確
# func(a=1, b=2, c=3, e=5)      #❌ TypeError: a and b must be positional-only
# func(1, 2, 3, 4, 5, 6)         #❌ TypeError: e must be keyword-only
