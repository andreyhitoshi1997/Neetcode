def reverString(s):
    arr = [ch for ch in s]
    l, r = 0, len(s) -1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return "".join(arr)