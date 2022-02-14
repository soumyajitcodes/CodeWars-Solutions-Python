def find_it(seq):
    odd = 0
    for i in seq:
        if seq.count(i)%2 != 0:
            odd = i
            break
    return odd
