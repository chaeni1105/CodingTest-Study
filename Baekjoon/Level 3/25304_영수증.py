### [문제 분석]
# 목적 :  구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사
# -> 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지에 따라 Yes/No를 출력

### [문제 풀이]
# 1단계 : 영수증에 적힌 총 금액 X, 영수증에 적힌 구매한 물건의 종류의 수 N, 이후 N개의 줄에는 각 물건의 가격 a와 개수 b를 입력받는다. +sum 초기화
#         + A리스트와 B리스트를 빈 공간으로 생성해준다.
# 2단계 : N만큼 반복하는 for문 안에서 a와 b를 곱해서 총 금액 sum을 X와 비교하여 Yes/No를 출력한다.

import sys
input = sys.stdin.readline

# 1단계
X = int(input())
N = int(input())

A = []
B = []

for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
sum = 0

# 2단계
for i in range(0, N):
    sum += A[i]*B[i]
if(sum == X):
    print("Yes")
else:
    print("No")
    
# 주의할 점
# 리스트를 사용할때는 꼭 빈 리스트를 먼저 생성하고, append함수를 써 리스트에 값을 추가해야한다!
# 입력받으면서 출력을 동시에 하면 코드 길이를 줄일 수 있다!