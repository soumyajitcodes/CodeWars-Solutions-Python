def sort_array(source_array):
    oddArray = sorted([x for x in source_array if x % 2 != 0])
    n = 0

    for i, el in enumerate(source_array):

        if el % 2 != 0:
            source_array[i] = oddArray[n]
            n += 1

    return source_array
