def solution(s):
    answer = ''
    now = 0
    for i in range(len(s)):
        if s[i] == ' ':
            now = 0
            answer += ' '
        else:
            if now % 2 == 0:
                answer += s[i].upper()
            else:
                answer += s[i].lower()
            now += 1
    return answer
