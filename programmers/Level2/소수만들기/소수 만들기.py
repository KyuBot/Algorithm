import itertools

def solution(nums):
    answer = 0

    num = [0] * 3001
    check = dict()

    for i in range(2, 3001):
        if num[i] == 0:
            check[i] = 1
            for j in range(i, 3001, i):
                num[j] = 1

    com = list(itertools.combinations(nums, 3))

    for i in com:
        total = 0
        if check.get(sum(i), 0) == 1:
            answer += 1
    return answer
