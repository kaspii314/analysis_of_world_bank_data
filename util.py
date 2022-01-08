def nth_power(n, fn=lambda x: x**2):
    '''
    calculates power for integers up to n
    '''
    return [ fn(i) for i in range(n) ]


print(nth_power(10))