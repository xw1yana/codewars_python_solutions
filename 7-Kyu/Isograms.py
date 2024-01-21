def is_isogram(string):
    string = string.lower()
    s = set()
    for i in string:
        if i in s:
            return False
        else:
            s.add(i)
    return True
    #your code here