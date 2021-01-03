def solution(n):
    answer = 0
    n = str(n)
    for word in n:
        answer += int(word)

    return answer