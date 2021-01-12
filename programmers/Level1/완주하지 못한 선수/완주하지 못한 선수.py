def solution(participant, completion):
    answer = ''
    all = dict()

    for x in participant:
        all[x] = all.get(x, 0) + 1

    for x in completion:
        all[x] = all.get(x) - 1

    for x in all:
        if all[x] > 0:
            answer = x

    return answer

