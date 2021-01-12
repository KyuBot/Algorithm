def solution(answers):

    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    ans = [0] * 3

    for i in range(len(answers)):
        if supo1[i % 5] == answers[i]:
            ans[0] += 1
        if supo2[i % 8] == answers[i]:
            ans[1] += 1
        if supo3[i % 10] == answers[i]:
            ans[2] += 1

    answer = [x + 1 for x in range(len(ans)) if ans[x] == max(ans)]
    return answer

solution([1,2,3,4,5])