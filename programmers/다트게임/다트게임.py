def solution(dartResult):
    answer = 0
    total = [0]
    prev = ''
    now = '0'
    for word in dartResult:
        # 만약 숫자라면. 10점의 점수까지 고려
        if '0' <= word <= '9':
            now = now + word
        else:
            # S가 나오면 1제곱
            if word == 'S':
                now = int(now)**1
                # 총 더할 것에 추가
                total.append(now)
                # 이전 숫자를 저장
                prev = now
                now = '0'
            # D가 나오면 2제곱
            elif word == 'D':
                now = int(now)**2
                total.append(now)
                prev = now
                now = '0'
            # T가 나오면 3제곱
            elif word == 'T':
                now = int(now)**3
                total.append(now)
                prev = now
                now = '0'
            # 만약 스타상이 나오면 이전에 저장한것을 2배 방금 저장한것을 2배
            elif word == '*':
                total[-2] = total[-2] * 2
                total[-1] = total[-1] * 2
            # 만약 아차상이 나오면 지금 나온것만 -
            elif word == '#':
                total[-1] = total[-1] * (-1)
    # 총 더해준다
    answer = sum(total)
    return answer