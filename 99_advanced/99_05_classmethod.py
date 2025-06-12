"""
@classmethod 是一種類別方法（class method），與普通的實例方法不同。它的
第一個參數是類別本身（慣稱為 cls），而不是實例（self），因此可用來操作「類別層級」的資料
（如：類別變數），甚至可作為工廠方法來建立新物件。
"""
class User:
    id = None
    name = None

    @classmethod
    def set_id(cls, id):
        cls.id = id
    
    def set_name(self, name):
        self.name = name

u = User()
u.set_id(1) # 類別變數
u.set_name('alice') # 實例變數

u2 = User()
u2.set_id(2) # 類別變數
u2.set_name('bill') # 實例變數

print(u.id, u.name) # 2 alice
print(u2.id, u2.name) # 2 bill
