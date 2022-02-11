def solution(string, ending):
    # your code here...
    if string[(len(string)-len(ending)):] == ending:
        return True
    else:
        return False