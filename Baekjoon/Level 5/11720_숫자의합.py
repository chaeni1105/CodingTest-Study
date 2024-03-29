### [문제 분석]
# 목적 : N개의 숫자가 공백 없이 쓰여있을 때, 이 숫자를 모두 합해서 출력하는 프로그램 작성
# -> 입력으로 주어진 숫자 N개의 합을 출력한다.

### [문제 풀이]
# 1단계 : 첫째 줄에 숫자의 개수 N을 입력받는다. 둘째줄에는 문자열의 형태로 숫자를 입력받는다.
# 2단계 : N만큼 반복한는 for문 안에 문자열을 리스트 취급하여 전부 더한다.

import sys
input = sys.stdin.readline

# 1단계
N = int(input())
num = input()
sum = 0

# 2단계
for i in range(N):
    sum += int(num[i])

print(sum)
    
# 주의할 점
