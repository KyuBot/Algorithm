def solution(s):
    answer = True
    answer = (len(s) == 4 or len(s) == 6) and s.isnumeric()
    return answer
