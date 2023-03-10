### [문제 분석]
# 목적 : 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램 작성
# -> 주어지는 명령의 수 N을 입력받고, 총 6가지의 명령을 받아서 수행한다.(출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.)

### [문제 풀이]
# 1단계 : 주어지는 명령의 수 N을 입력받는다. 빈 큐 리스트를 만든다.
# 2단계 : 명령을 입력받는다.
#        
# 3단계 : 명령에 따라 출력시킨다.

import sys
input = sys.stdin.readline

# 1단계
from collections import deque #데큐 자료구조

N = int(input())
queue = deque()

# 2단계
for _ in range(N):
    cmd = input().split()
    
    if(cmd[0] == 'push'):
        queue.append(cmd[1])
    
    elif(cmd[0] == 'pop'):
        print(queue[1])
        queue.popleft()

# 3단계    

# 주의할 점
# 1. 파이썬으로 큐를 구현할 때는 collections 모듈에서 제공하는 deque 자료구조를 활용하자.
# 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이며 queue 라이브러리보다 간단하다.
# 대부분의 코테에서는 collections 모듈과 같은 기본 라이브러리 사용을 허용한다.
