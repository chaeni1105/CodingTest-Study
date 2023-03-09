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
    print(printList[i])
    
# 주의할 점
# 1. for i in range(T) -> 0~T-1까지, 그러니까 T가 4라면 0부터 3까지 출력된다.
# 2. printList = []로 빈 리스트를 만들고, printList에 바로 변수를 넣으려고 하면 오류가 생긴다.
# 그 이유는 이렇다. 생성은 빈 리스트인데, 인덱스 0번에 데이터를 넣으려고 하니, 빈 리스트인데 0번 인덱스가 어디 있니? 하는 것이다.
# 따라서 1) append() 또는 insert()함수를 사용하여 데이터를 넣는방법이 있다. -> printList.append(output)
# 2) 리스트 자체를 초기화해서 사용할 리스트 갯수를 미리 잡아놓는 방법도 있다.
# printList = [] -> null 리스트 선언
# printList = [0]*T -> 0값이 들어가 있는 T개의 방을 잡는다.
# printList[0] = 10 -> 0번째 인덱스에 10이라는 값을 넣어준다.