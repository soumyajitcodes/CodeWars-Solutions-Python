def sum_two_smallest_numbers(a):
    # your code here
    min1 = min(a)
    a.remove(min1)
    min2 = min(a)
    return min1 + min2
