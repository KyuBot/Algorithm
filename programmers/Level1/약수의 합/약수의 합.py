def solution(n):
    answer = 0
    for c in range(1, n+1):
        if n % c == 0:
            answer += c
    return answer