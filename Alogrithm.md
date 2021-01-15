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
    
4.   for 문 간단하게 쓰는법 

    - [x for x in range(100)]
    
5.  input 받는법

    - N, M = map(int, input().split())
    
6.  index 와 find 의 차이점

    > 둘다 문자열에서 값을 찾아 index를 반환하지만, find는 없으면 -1을 반환, index는 valueError. 따라서 find를 권장한다.
    
    * 주의사항 : find는 문자열 형태에서만 사용가능하고, index는 list도 가능하다.
    * index는 숫자도 찾을 수 있으니, 상황에 따라 사용하는 것을 권장.
    
7.   숫자판단 함수

    1. isdigit() => 숫자가 맞는지 판단. 이때 3² 도 숫자로 판단. 단일 글자가 숫자로 생겼으면 True
    2. isdecimal() => 숫자가 맞는지 판단. 이때 3²은 숫자로 판단하지 않는다. int형 불가로 판단.
    3. isnumeric() => 숫자가 맞는지 판단. 이떄 3²과 숫자값 표현에 해당하는 문자열까지 인정한다. 제곱근 및 분수, 거듭제곱 특수문자도 isnumeric() 함수는 True를 반환.

8.   for 과 if의 조함

    - [x for x in range(arr) if x % 2 == 0]

9.  if 조건

    > if 조건식: True 결과값 = False 결과값
    
10.  import collections

     > collections.Counter(리스트) = > 리스트를 개수를 세서 딕셔너리로 반환 해준다.
     >
     > 이때 딕셔너리는 앞에서 부터 순서대로 큰 갯수부터 해준다
     >
     > 그리고 dict - dict 가 가능하다는 사실..

11.  enumerate

     > for idx, result in enumerate(리스트):
     >
     > ​	인덱스와 값이 동시에 나옴!
     
12.  import math

     > math.gcm(a, b) = > 최대공약수를 구할 수 있음.
     
13.  