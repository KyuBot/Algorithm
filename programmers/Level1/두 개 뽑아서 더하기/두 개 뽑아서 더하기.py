def solution(numbers):
    answer = []
    ans = dict()
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            ans[numbers[i] + numbers[j]] = ans.get(numbers[i] + numbers[j], 0) + 1
    answer = sorted(list(ans))
    return answer