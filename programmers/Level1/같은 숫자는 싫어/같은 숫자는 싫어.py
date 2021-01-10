def solution(arr):
    answer = []
    c = 10
    for x in range(len(arr)):
        if c != arr[x]:
            answer.append(arr[x])
            c = arr[x]
    return answer
