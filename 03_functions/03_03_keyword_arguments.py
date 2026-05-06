# keyword-arguments
def parrot(voltage, state='B', action='C', type='D'):
    print(voltage, state, action, type)
    
parrot('A')                         # 1 positional argument
parrot(voltage='AA')                # 1 keyword argument
parrot(voltage='AA', action='CC')   # 2 keyword arguments
parrot(action='CC', voltage='AA')   # 2 keyword arguments
parrot('AAA', 'BBB')                # 3 positional arguments
parrot('AA', state='BB')            # 1 positional, 1 keyword