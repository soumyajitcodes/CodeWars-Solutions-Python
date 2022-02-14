def find_short(s):
    # your code here
    strList = s.split(" ")
    strLenList = [len(i) for i in strList]
    return min(strLenList) # l: shortest word length
