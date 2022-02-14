import math

def is_square(n):
    if n>=0:
        sqrtmath = int(math.sqrt(n))
        return sqrtmath*sqrtmath == n
    else:
        return False
        # fix me