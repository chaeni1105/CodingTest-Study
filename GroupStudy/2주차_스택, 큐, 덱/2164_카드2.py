### [문제 분석]
# 목적 : 제일 위에 있는 카드를 바닥에 버리고, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮겨서 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하기.
# -> N장이라면 N-1만큼 위와 같은 동작을 반복하게 되는데, deque를 사용해보자. 맨 위에 있는 카드가 1번이니까 그것을 popleft하고, 그 다음 카드를 빼서 뒤에 삽입하는거다.

### [문제 풀이]
# 1단계 : 정수 N을 입력받는다. queue리스트도 만든다.
# 2단계 : N-1만큼 반복하는 for문을 만든다. 그 안에서 

import sys
input = sys.stdin.readline
from collections import deque

# 1단계
N = int(input)
queue = deque()

# 2단계

    
# 주의할 점
