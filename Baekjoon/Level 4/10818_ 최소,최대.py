### [문제 분석]
# 목적 : 최솟값과 최댓값을 구하는 프로그램 작성
# -> 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

### [문제 풀이]
# 1단계 : 정수의 개수 N과 N개의 정수를 공백으로 구분해서 입력받는다.
# 2단계 : min, max함수를 이용하여 최솟값과 최댓값을 출력한다.

import sys
input = sys.stdin.readline

# 1단계
N = int(input())
A = list(map(int, input().split()))

# 2단계
print(min(A), max(A))
