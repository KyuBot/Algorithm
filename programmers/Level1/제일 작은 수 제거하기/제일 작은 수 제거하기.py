def solution(arr):
    i = float('inf')
    idx = 0
    if len(arr) == 1:
        return [-1]
    for n in range(len(arr)):
        if arr[n] < i:
            i = arr[n]
            idx = n
    arr.pop(idx)
    return arr