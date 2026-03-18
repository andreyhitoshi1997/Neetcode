import enum
def firstUniqChar(s):
    'l' : [0,1]
    d = {}
    #enumaeratoe da um char e um index
    for ch in enumerate(s):
        if ch not in d:
            d[ch] = []
        d[ch].append(i)
    for ch in s:
        if len(d[ch]) == 1:
            return ch
    return -1