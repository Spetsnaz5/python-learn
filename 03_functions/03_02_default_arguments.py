# default-argument-values 
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

#只給必要引數
ask_ok('Do you really want to quit?')
#給予一個選擇性引數
ask_ok('OK to overwrite the file?', 2)
#給予所有引數
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
