import sys
sys.setrecursionlimit(10**6)

def solution(n, m):
    answer = []
    max_result = 0
    if n > m:
        max_result = n
    else:
        max_result = m
    tmp_arr = [0] * (max_result + 1)
    check = [0] * (max_result + 1)
    check_n = [0] * (max_result + 1)
    check_m = [0] * (max_result + 1)
    for i in range(2, max_result + 1):
        if tmp_arr[i] == 0:
            check[i] = 1
            for j in range(i, max_result + 1, i):
                tmp_arr[j] = 1
    nn = n
    mm = m
    check_n[1] = 1
    check_m[1] = 1
    for i in range(2, n+1):
        if nn % i == 0:
            r = 0
            while nn % i == 0:
                r += 1
                nn = nn // i
            check_n[i] = r
    for i in range(2, m+1):
        if mm % i == 0:
            r = 0
            while mm % i == 0:
                r += 1
                mm = mm // i
            check_m[i] = r
    x, y = 1, 1
    for i in range(len(check)):
        if check_n[i] > 0 and check_m[i] > 0:
            x = x * i ** (min(check_n[i], check_m[i]))
        if check_n[i] > 0 or check_m[i] > 0:
            y = y * i **  (max(check_n[i], check_m[i]))

    return [x, y]
