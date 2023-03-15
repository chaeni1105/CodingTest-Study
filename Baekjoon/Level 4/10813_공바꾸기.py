### [문제 분석]
# 목적 : M번 공을 바꾼 이후에 각 바구니에 어떤 공이 들어있는지 구하는 프로그램 작성
# -> 공을 교환하고, 1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다.

### [문제 풀이]
# 1단계 : 
# 2단계 : 
# 3단계 :


import sys
input = sys.stdin.readline

# 1단계
N, M = map(int, input().split()) #총 바구니의 개수 N, 총 공을 넣는 횟수 M
answer = [] 

for i in range(1, N+1): # [1, 2, 3, 4, 5] 배열 생성
    answer.append(i)


for _ in range(M): #공을 M번 넣는만큼 반복
    i, j, k = map(int, input().split()) #i번과 j번 바구니에 들어있는 공을 서로 바꾼다.

    # 2단계
    for num in range (i-1, j): #1번바구니~2번바구니까지 0 -> 3으로 공을 바꿔치기함.
        answer[num] = k

# 3단계
for i in range(N):
    print(answer[i], "", end='')

    
# 주의할 점
