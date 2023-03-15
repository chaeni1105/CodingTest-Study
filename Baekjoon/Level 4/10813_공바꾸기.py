### [문제 분석]
# 목적 : M번 공을 바꾼 이후에 각 바구니에 어떤 공이 들어있는지 구하는 프로그램 작성
# -> 공을 교환하고, 1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다.

### [문제 풀이]
# 1단계 : 총 바구니의 개수 N, 총 공을 넣는 횟수 M를 입력받고, [1, 2, 3, 4, 5] 배열 생성한다.
# 2단계 : i번과 j번 바구니에 들어있는 공을 서로 바꾼다. 이는 M번 반복하는 반복문 안에 쓴다.
# 3단계 : 1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다.(출력 모양 조심!)


import sys
input = sys.stdin.readline

# 1단계
N, M = map(int, input().split()) #총 바구니의 개수 N, 총 공을 넣는 횟수 M
answer = [] 

for i in range(1, N+1): # [1, 2, 3, 4, 5] 배열 생성
    answer.append(i)

for _ in range(M): #공을 M번 바꾸는만큼 반복
    i, j = map(int, input().split())

    # 2단계
    #1번바구니와 2번바구니의 공을 서로 바꿔치기함.
    temp = answer[i-1]
    answer[i-1] = answer[j-1]
    answer[j-1] = temp

# 3단계
for i in range(N):
    print(answer[i], "", end='')
