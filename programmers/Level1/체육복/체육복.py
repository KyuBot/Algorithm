import copy
def solution(n, lost, reserve):
    answer = 0
    check = [1] * (n + 1)
    loss = [0] * (n + 1)
    a, b = 0, 0
    for i in lost:
        loss[i] = 1
        check[i] = 0

    for i in reserve:
        check[i] += 1

    check2 = copy.deepcopy(check)

    ## 왼쪽 방향으로 체육복을 빌려줌

    for i in range(2, n + 1):
        if check[i] == 2 and check[i-1] == 0:
            check[i] -= 1
            check[i-1] += 1
    ## 오른쪽 방향으로 체육복을 빌려줌
    for i in range(1, n):
        if check[i] == 2 and check[i+1] == 0:
            check[i] -= 1
            check[i+1] += 1
    a = check.count(1) + check.count(2) - 1
    b = check2.count(1) + check2.count(2) - 1

    ## 만약에 두 방향 중 큰 값이 있다면 그것을 출력력
    returnmax(a, b)
