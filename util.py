def nth_power(n, fn=lambda x: x**2):
    '''
    calculates power for integers up to n
    args:
        n: highest number in the list of numbers
        power: power for numbers to raise, default power is 2
    '''
    return [ fn(i) for i in range(n) ]


print(nth_power(10))