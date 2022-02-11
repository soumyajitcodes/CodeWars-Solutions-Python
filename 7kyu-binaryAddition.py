def add_binary(a,b):
    #your code here
    sum = a+b
    sumToBin = bin(sum).replace("0b", "")
    return str(sumToBin)