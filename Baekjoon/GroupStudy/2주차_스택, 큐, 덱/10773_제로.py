### [문제 분석]
# 목적 :  K개의 줄에 정수가 1개씩 주어진다. 정수가 "0" 일 경우에는 가장 최근에 쓴 수가 지워질 때, 모든 수의 총 합을 출력하는 프로그램 작성
# -> 정수를 스택에 넣다가 0을 입력하면 맨 위에 있는걸 빼고, 마지막엔 리스트 안의 모든 수를 더하여 출력한다.

### [문제 풀이]
# 1단계 : K개의 줄을 입력받는다. stack이라는 빈 리스트를 생성한다. sum 초기화
# 2단계 : K만큼 반복하는 for문 안에서 정수를 계속 입력받는다. 입력받은 정수는 append()함수로 스택에 추가한다.
#        만약 정수가 0일경우 pop()함수로 스택에 가장 최근에 들어갔던 정수를 지운다.
# 3단계 : stack안에 들어있는 모든 정수들을 더한 총합을 출력한다.

import sys
input = sys.stdin.readline

# 1단계
K = int(input())
stack = []
sum = 0

# 2단계
for i in range(K):
    num = int(input())
    
    if(num == 0):
        stack.pop()
    else:
        stack.append(num)

# 3단계    
for i in stack:
    sum += i

print(sum)