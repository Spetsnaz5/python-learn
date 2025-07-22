
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
    
    
    
if 1 == 1 and 0 == 0:
    pass
elif 1 == 1 or 0 == 0:
    pass
else:
    pass

x, y = 5, 5
end = (5, 5)
if (x, y) == end:
    print((x, y) == end)