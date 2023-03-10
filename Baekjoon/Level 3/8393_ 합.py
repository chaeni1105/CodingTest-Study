### [문제 분석]
# 목적 : 1부터 n까지 합을 구하는 프로그램 작성
# -> for문을 활용하여 1부터 n까지 합을 출력한다.

### [문제 풀이]
# 1단계 : n (1 ≤ n ≤ 10,000)을 입력받는다. 합을 출력할 sum을 초기화시킨다.
# 2단계 : for문을 활용하여 1부터 n까지 합을 출력한다.

import sys
input = sys.stdin.readline

# 1단계
n = int(input())
sum = 0

# 2단계
for i in range(1, n+1):
    sum += i

print(sum)
