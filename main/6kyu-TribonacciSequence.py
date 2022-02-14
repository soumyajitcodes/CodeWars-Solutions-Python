def tribonacciSequence(signature, n):
    # your code here
    n1, n2, n3 = signature

    if n == 0:
        return []

    else:
        for i in range(n - 3):
            sumList = n1 + n2 + n3
            n1 = n2
            n2 = n3
            n3 = sumList
            signature.append(sumList)

        return signature[:n]
