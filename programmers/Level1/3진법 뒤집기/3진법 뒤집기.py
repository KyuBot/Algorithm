def solution(n):
    answer = 0
    ans = ""
    while n > 0:
        ans = str(n % 3) + ans
        n = n // 3

    for i in range(len(ans)):
        answer += int(ans[i]) * 3**(i)
    return answer