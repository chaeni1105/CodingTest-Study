### [문제 분석]
# 목적 : 세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램 작성
# -> 점수/M*100으로 고친 모든 과목의 성적을 더해서 평균을 출력한다.

### [문제 풀이]
# 1단계 : 시험 본 과목의 개수 N을 입력받고, 둘째 줄에 세준이의 현재 성적을 입력 받는다. 
#         이때 리스트안의 점수 중 최댓값 M을 결정한다.
# 2단계 : 리스트 안의 모든 점수를 점수/M*100으로 고치고 sum에 더한다.
# 3단계 : sum / len(list)로 평균을 출력한다.

import sys
input = sys.stdin.readline
sum = 0

# 1단계
N = int(input())
answer = list(map(int, input().split()))
M = max(answer)

# 2단계
for i in range(N):
    answer[i] = answer[i]/M*100
    sum += answer[i]

# 3단계
print(sum/N)
    
# 주의할 점
# list 안에는 왜 map(float, input().split())이 들어가면 안되는지? int는 돼고, float는 안된다?
# list 안에는 정수여야한다. 따라서 int형으로 바꿔줘야한다. float형은 안된다!