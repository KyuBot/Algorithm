def solution(a, b):
    answer = ''
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = b
    for i in range(a):
        day += month[i]
    ans = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    return ans[day % 7]