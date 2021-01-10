def solution(arr, divisor):
    answer = [x for x in arr if x % divisor == 0]
    answer.sort()
    if answer == []:
        answer = [-1]
    return answer