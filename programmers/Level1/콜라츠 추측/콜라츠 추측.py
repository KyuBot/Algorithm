def solution(num):
    now = 0
    # num이 1이라는 조건을 붙여줘야한다.
    if num == 1:
        return 0
    while now < 500:
        now += 1

        if num % 2 == 0:
            num = num // 2
            if num == 1:
                return now
        else:
            num = num * 3 + 1

    return -1