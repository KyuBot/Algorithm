def solution(n):
    answer = 0
    check = [0] * (n + 1)
    ans = [0] * (n + 1)
    for i in range(2, n + 1):
        if check[i] == 0:
            ans[i] = 1
            for j in range(i, n + 1, i):
                check[j] = 1

    return ans.count(1)