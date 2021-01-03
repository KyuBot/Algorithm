def solution(s, n):
    answer = ''

    for word in s:
        if word == " ":
            answer += " "
        elif 'a' <= word <= 'z':
            N = n + ord(word) - ord('a')
            while N >= 26:
                N %= 26
            answer += chr(ord('a') + N)
        else:
            N = n + ord(word) - ord('A')
            while N >= 26:
                N %= 26
            answer += chr(ord('A') + N)

    return answer

solution('z', 1)