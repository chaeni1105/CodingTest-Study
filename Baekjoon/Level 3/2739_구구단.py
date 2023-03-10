### [문제 분석]
# 목적 : 구구단 N단을 출력하는 프로그램 작성
# -> 출력 형식에 맞춰서 구구단 N단을 출력하기.

### [문제 풀이]
# 1단계 : N을 입력받는다.
# 2단계 : for문을 활용하여 N단을 형식에 맞춰 출력한다.

import sys
input = sys.stdin.readline

# 1단계
N = int(input())

# 2단계
for i in range(1, 10):
    print(N, "*", i, "=", N*i)
    
# 주의할 점
# for i in range(1, 10) -> 1부터 10까지가 아니라, 1부터 9까지이다!!