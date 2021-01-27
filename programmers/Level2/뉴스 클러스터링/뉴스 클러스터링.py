def solution(str1, str2):
    answer = 0
    st1, st2 = dict(), dict()

    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            st1[str1[i:i+2].lower()] = st1.get(str1[i:i+2].lower(), 0) + 1

    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            st2[str2[i:i+2].lower()] = st2.get(str2[i:i+2].lower(), 0) + 1


    if len(st1) == 0 and len(st2) == 0:
        return 65536

    j_st1 = 0
    j_st2 = 0

    for idx, result in st1.items():
        if st2.get(idx, 0) != 0:
            j_st1 += min(result, st2[idx])
        j_st2 += result
    for idx, result in st2.items():
        j_st2 += result
    j_st2 -= j_st1
    return int(j_st1 / j_st2 * 65536)

