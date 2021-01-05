def solution(x):
    answer = True
    x = str(x)
    n = 0
    for i in x:
        n += int(i)

    if int(x) % n != 0:
        answer = False


    return answer