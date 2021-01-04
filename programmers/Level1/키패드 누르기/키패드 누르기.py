def solution(numbers, hand):
    answer = ''
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    now_l = [3, 0]
    now_r = [3, 2]

    for num in numbers:
        if num in (1, 4, 7, '*'):
            answer += 'L'
            for i in range(len(keypad)):
                for j in range(len(keypad[i])):
                    if keypad[i][j] == num:
                        now_l = [i, j]
        elif num in (3, 6, 9, '#'):
            answer += 'R'
            for i in range(len(keypad)):
                for j in range(len(keypad[i])):
                    if keypad[i][j] == num:
                        now_r = [i, j]
        else:
            ll = 0
            rr = 0
            now = [0, 0]
            for i in range(len(keypad)):
                for j in range(len(keypad[i])):
                    if keypad[i][j] == num:
                        now = [i, j]
            if abs(now[0] - now_l[0]) + abs(now[1] - now_l[1]) > abs(now[0] - now_r[0]) + abs(now[1] - now_r[1]):
                answer += 'R'
                now_r = [now[0], now[1]]
            elif abs(now[0] - now_l[0]) + abs(now[1] - now_l[1]) < abs(now[0] - now_r[0]) + abs(now[1] - now_r[1]):
                answer += 'L'
                now_l = [now[0], now[1]]
            else:
                if hand == 'right':
                    answer += 'R'
                    now_r = [now[0], now[1]]
                else:
                    answer += 'L'
                    now_l = [now[0], now[1]]
    return answer
