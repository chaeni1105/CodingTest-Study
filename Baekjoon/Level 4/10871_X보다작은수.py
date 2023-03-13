### [문제 분석]
# 목적 : 수열 A에서 정수 X보다 작은 수를 모두 출력하는 프로그램 작성
# -> X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. (X보다 작은 수는 적어도 하나 존재한다.)

### [문제 풀이]
# 1단계 : 정수 N개와 정수 X, 그리고 정수 N개로 이루어진 수열 A를 입력받는다. 출력시킬 정답리스트도 생성한다.
# 2단계 : A리스트의 0부터 N-1까지 차례로 정수 X와 비교한다. 정수 X보다 작으면 정답리스트에 추가시킨다.
# 3단계 :

import sys
input = sys.stdin.readline

# 1단계
N, X = map(int, input().split())
A = list(map(int, input().split()))
answer = []

# 2단계
for i in range(0, N):
    if(A[i] < X):
        answer.append(A[i])
        
for i in answer:
    print(i, "", end='')
    
# 주의할 점
# 만약 A리스트에서 remove하는 방식으로 한다면, A리스트의 인덱스 번호가 앞당겨지기 때문에 A[i]를 사용하기 힘들어진다.
# 따라서 정수 X보다 작으면 정답리스트에 추가시키는 방식으로 해야한다.