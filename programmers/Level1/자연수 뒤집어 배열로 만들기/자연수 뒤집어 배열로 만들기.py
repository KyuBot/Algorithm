def solution(n):
    answer = []
    n = str(n)
    answer = list(map(int, reversed(n)))
    return answer