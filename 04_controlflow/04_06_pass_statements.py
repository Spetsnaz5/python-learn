"""
pass：什麼事情都不做的「空敘述」。
用於語法上需要程式碼，但實際上尚未實作的情境，或作為縼找位子用。
類似：... (Ellipsis) 也常被當縼佈使用。
"""

while True:
   pass  # Busy-wait for keyboard interrupt (Ctrl+C)

class MyEmptyClass:
    pass

def initlog(*args):
    pass   # Remember to implement this!