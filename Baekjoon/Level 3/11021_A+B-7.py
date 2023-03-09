### [문제 분석]
# 목적 :  A+B를 출력하는 프로그램 작성
# -> 테스트할 개수 T와, 두 정수 A와 B를 입력받은 다음, A+B를 출력한다.

### [문제 풀이]
# 1단계 : 테스트 케이스의 개수 T와, 두 정수 A와 B를 반복적으로 for문을 활용하여 입력받는다.
# 2단계 : for문을 활용하여 T만큼 돌리고, 반복적으로 A와 B를 더해서 출력해낸다.

import sys
input = sys.stdin.readline

# 1단계
T = int(input())
printList = []

for i in range(T):
    A, B = map(int, input().split())
    output = (A+B)
    printList.append(output)

# 2단계
for i in range(T):
    print("Case #", i+1 , ": ", printList[i], sep='')
    
# 주의할 점
# 1. Case번호는 1부터 시작하므로, i+1로 출력해줘야한다.
# 2. 공백없이 출력하려면 sep=''을 마지막에 붙이면 된다!