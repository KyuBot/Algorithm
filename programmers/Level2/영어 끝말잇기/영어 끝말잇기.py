def solution(n, words):
    answer = []
    check = {words[0]: 1}

    word = words[0][-1]

    ans1 = 0
    ans2 = 0

    for i in range(1, len(words)):
        if word != words[i][0] or 1 == check.get(words[i], 0):
            ans1 = i % n + 1
            ans2 = i // n + 1
            return [ans1, ans2]
        else:
            word = words[i][-1]
            check[words[i]] = 1

    return [0, 0]

solution(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank'])