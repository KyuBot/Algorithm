def solution(n):
    answer = 0
    answer = sorted(str(n), reverse=True)
    answer = "".join(answer)
    return int(answer)