def step(x, y):
    result = -1
    if x == y:
        if x % 4 == 0:
            result = x * 2
        else:
            result = x * 2 + 1
    elif x % 2 == 0 and y % 2 == 0:
        result = x + y
    elif x % 2 != 0 and y % 2 != 0:
        result = x + y - 1

    if result == -1:
        print 'No Number'
    else:
        print result
    return result

x = input()
y = input()
step(x,y)
