def descending_order(num):
    num = [i for i in str(num)]
    return int(''.join(sorted(num, reverse=True)))
