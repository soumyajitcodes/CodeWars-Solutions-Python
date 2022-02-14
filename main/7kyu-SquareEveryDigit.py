def square_digits(num):
    if num > 0:
        sqList = []

        while (num > 0):
            temp = num % 10
            sqList.append(temp * temp)
            num = num // 10

        sqListStr = [str(i) for i in sqList[::-1]]
        return int("".join(sqListStr))
    else:
        return 0

