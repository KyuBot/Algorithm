def solution(N, stages):
    answer = []
    all = len(stages)
    state = [0] * (N + 1)
    # 최악의 조건은 500 * 200000 = 10**8
    # 시간 초과 날것이 분명함
    finish = 0
    for stage in stages:
        if stage == N+1:
            finish += 1
        else:
            state[stage] += 1

    # 1스테이지 도달한 사람 = N명, 1스테이지를 클리어 하지 못한사람 = state[stage]
    # 2스테이지 도달한 사람 = N - state[1], 2스테이지를 클리어 하지 못한사람 = stage[1]
    # 3스테이지 도달한 사람 = N - ( state[1] + state[2] )

    tmp_arr = [0] * (N + 1)
    for i in range(1, len(state)):
        tmp_arr[i] = tmp_arr[i-1] + state[i-1]

    New_state = [all] * (N+1)
    # 도달한 사람
    for i in range(1, len(state)):
        New_state[i] -= tmp_arr[i]

    fail = [0] * (N+1)
    for i in range(1, len(state)):
        # 만약에 스테이지에 도달한 사람이 없으면 실패율은 0으로 처리한다.
        if New_state[i] == 0:
            fail[i] = 0
        else:
            fail[i] = state[i] / New_state[i]

    tmp = 0
    tmp_arr2 = [0] * (N + 1)
    # 좋지 않은 방법같지만, idx와 sort 합치는 법에 대한 방법 미숙으로 앞자리부터 한가지씩 max 값을 찾았다. 최대 500 * 500 의 경우의 수가 나온다.
    while tmp != N:
        mm = -1
        ans = 0
        for i in range(1, N+1):
            if fail[i] > mm and tmp_arr2[i] == 0:
                mm = fail[i]
                ans = i
        tmp_arr2[ans] = 1
        tmp += 1
        answer.append(ans)

    return answer
