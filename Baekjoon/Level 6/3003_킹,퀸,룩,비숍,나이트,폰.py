### [문제 분석]
# 목적 : 리스트를 입력받고, 두 개의 리스트를 빼는 방법을 연습하는 것입니다.
# -> 예제의 첫줄을 리스트로 입력받습니다. 먼저 생성해놓은 리스트에서 입력받은 리스트를뺍니다.

### [문제 풀이]
# 1단계 : 리스트 입력받기 및 생성
# 2단계 : 리스트 차 구하기
# 3단계 : 출력

import sys
input = sys.stdin.readline

# 1단계
inputList = list(map(int, input().split()))

answerList = [1, 1, 2, 2, 2, 8]

# 2단계
for i in range(6):
    answerList[i] = (answerList[i] - inputList[i])

# 3단계
for i in range(6):
    print(answerList[i], "", end='')
    
# 주의할 점
