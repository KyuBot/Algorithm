def solution(s):
    answer = s.count("p") + s.count("P") == s.count("y") + s.count("Y")

    return answer