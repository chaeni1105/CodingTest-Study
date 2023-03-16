### [문제 분석]
# 목적 : 교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램 작성
# -> 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 2번째 줄에선 그 다음 출석번호를 출력한다.

### [문제 풀이]
# 1단계 : 28번 반복해서 제출한 학생의 출석번호가 입력된다.(출석번호에 중복은 없다.)
# 2단계 : set()함수를 이용해서 answer리스트를 구한다.
# 3단계 : answer리스트에서 가장작은수를 min()함수로 출력하고, 다음 출석번호는 max()함수로 출력한다.

import sys
input = sys.stdin.readline

# 1단계
submit = []
for i in range(28):
    submit.append(i)
    
not_submit = []
answer = []
# 2단계
answer = set(not_submit) - set(submit)

# 3단계
sorted(list(answer))
print(answer[0])
print(answer[1])
    
# 주의할 점.
