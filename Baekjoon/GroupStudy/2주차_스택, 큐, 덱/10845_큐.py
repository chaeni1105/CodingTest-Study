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
    cmd = list(input().split()) #리스트로 받아줘야함!
    
    if(cmd[0] == 'push'):
        queue.append(cmd[1]) #정수를 큐에 넣는다.
    
    elif(cmd[0] == 'pop'):
        if(len(queue) == 0):
            print(-1)
        else:
            print(queue[0])
            queue.popleft() #가장 앞에있는 정수를 큐에서 삭제한다.
        
    elif(cmd[0] == 'size'):
        print(len(queue)) #큐에 들어있는 정수의 개수를 출력한다.
        
    elif(cmd[0] == 'empty'):
        if(len(queue) == 0):
            print(1)
        else:
            print(0)
        
    elif(cmd[0] == 'front'):
        if(len(queue) == 0):
            print(-1)
        else:
            print(queue[0]) #큐의 가장 앞에 있는 정수를 출력한다.
        
    elif(cmd[0] == 'back'):
        if(len(queue) == 0):
            print(-1)
        else:
            print(queue[-1]) #큐의 가장 뒤에 있는 정수를 출력한다.
            
# 주의할 점
# 1. 파이썬으로 큐를 구현할 때는 collections 모듈에서 제공하는 deque 자료구조를 활용하자.
# 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이며 queue 라이브러리보다 간단하다.
# 대부분의 코테에서는 collections 모듈과 같은 기본 라이브러리 사용을 허용한다.

# 2. 조건을 항상 잘 확인하자.
# elif(cmd[0] == 'pop'):을 할때, 만약 큐가 비어있으면 -1을 출력해야함을 간과했다 ㅠㅠ
