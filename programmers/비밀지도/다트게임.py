def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        ans = ''
        word = ''
        num = arr1[i]
        # 첫 숫자를 2진법으로 만든다
        while num > 0:
            word = str(num % 2) + word
            num //= 2
        # 두번째 숫자를 2진법으로 만든다
        word2 = ''
        num = arr2[i]
        while num > 0:
            word2 = str(num % 2) + word2
            num //= 2
        # 만약 n자리가 안된다면 0을 채워준다
        word = '0' * (n-len(word)) + word
        word2 = '0' * (n - len(word2)) + word2

        # 둘 중 하나가 1이면 #을 만들고 아니면 공백을 만든다
        for j in range(n):
            if word[j] == '1' or word2[j] == '1':
                ans += '#'
            else:
                ans += ' '
        answer.append(ans)
    return answer
