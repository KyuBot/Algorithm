# 알고리즘 팁

### Python

> 파이썬 문제들을 풀면서 간단한 팁, 내장함수를 정리한 것!



1.  배열을 인덱스 순으로 배열 하고 싶을떄 :

   - 첫번째로 (키, 값) 딕셔너리 형태로 만들어 준 후 다시 배열로 만드는 것이 간단핟. 

   - sorted(딕셔너리, Key, reverse) 

   - 함수명
   - key=lambda x: 딕셔너리[x]
   - reverse=True

   > a = {1: 3, 2: 0.5, 3:0.5, 4: 1}
   >
   > sorted(a, key=lambda x:a[x], reverse=True) => sorted 함수가 배열로 반환을 해준다
   >
   > 결과는 [1, 4, 2, 3] => 값이 같으면 키가 앞에있는 것을 먼저 반환한다.

2. Zip 함수 
   -  list(x * y for x, y in zip(a, b)) 를 하면 x * y 배열을 리턴
   - 2차 배열 뒤집기 : list(map(list, zip(*배열))) 하면 뒤집어짐
   
3.  recursion

    - import sys
    - sys.setrecursionlimit(10**6)