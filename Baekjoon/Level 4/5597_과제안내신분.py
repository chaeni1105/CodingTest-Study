### [문제 분석]
# 목적 : 교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램 작성
# -> 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 2번째 줄에선 그 다음 출석번호를 출력한다.

### [문제 풀이]
# 1단계 : 먼저 [1, ~ 30]리스트를 만든다.
# 2단계 : 28번 반복해서 제출한 학생의 출석번호가 입력된다.(출석번호에 중복은 없다.)
#         출석번호는 입력되는 동시에 1~30 리스트에서 삭제가 된다.
# 3단계 : 최소, 최대함수를 사용해서 정답을 출력한다.

import sys
input = sys.stdin.readline

# 1단계
student = []
for i in range(1, 31):
    student.append(i)

for _ in range(28):
    submit = int(input())
    student.remove(submit)

# 3단계
print(min(student))
print(max(student))
    
# 주의할 점.
# set함수 사용보다는 더 쉬운 방법이 있었다.
# 입력받는 동시에 학생 리스트에서 제출한 사람을 삭제시키는 방법이다.
# 그럼 하나의 리스트만 선언해서 정답을 출력할 수 있었다.
