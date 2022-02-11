def series_sum(n):
    # Happy Coding ^_^
    arraySeries = []

    for i in range(n):
        arraySeries.append(1 / (1 + i * 3))

    return '{:.2f}'.format(sum(arraySeries))