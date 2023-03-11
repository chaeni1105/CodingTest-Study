### [문제 분석]
# 목적 : 제일 위에 있는 카드를 바닥에 버리고, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮겨서 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하기.
# -> N장이라면 N-1만큼 위와 같은 동작을 반복하게 되는데, deque를 사용해보자. 맨 위에 있는 카드가 1번이니까 그것을 popleft하고, 그 다음 카드를 빼서 뒤에 삽입하는거다.

### [문제 풀이]
# 1단계 : 정수 N을 입력받는다. queue리스트도 만든다.
# 2단계 : N-1만큼 반복하는 for문을 만든다. queue안에 1부터 N까지의 수를 차례로 넣어준다.
# 3단계 : 반복문 안에서 맨 앞의 카드를 popleft 하고나서, 큐 안의 정수가 1개가 될때까지 다음 카드를 맨 뒤로 보낸다.

import sys
input = sys.stdin.readline
from collections import deque

# 1단계
N = int(input())
queue = deque()

# 2단계
for i in range(1, N+1):
    queue.append(i)

if(len(queue) == 1):
        print(queue[0])
        
# 3단계
for _ in range(N-1):
    queue.popleft()
    
    if(len(queue) == 1):
        print(queue[0])
    else:
        queue.append(queue[0])
        queue.popleft()
    
# 주의할 점
# 만약 1을 넣었을 때는 1이 출력되어야 하는데, 출력되지 못했다. 이런 실수 조심하자.
# 처음부터 카드가 1개라면, 바로 1을 출력할 수 있도록 if문을 중간에 추가해줘야한다.
