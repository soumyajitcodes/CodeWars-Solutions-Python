def fake_bin(x):
    numlist = []

    for i in x:
        if int(i) < 5:
            numlist.append("0")
        else:
            numlist.append("1")
    return ''.join(numlist)
