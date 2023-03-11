### [문제 분석]
# 목적 : 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.) 
#        이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램 작성
# -> 2번연산만 한다음에 N-(2번연산횟수)해서 3번연산을 구하고 둘의 최솟값min()을 구한다.

### [문제 풀이]
# 1단계 : 1. 큐의 크기 N, 뽑아내려고 하는 수의 개수 M을 입력받는다. queue 리스트를 만든다.
#         2. 지민이가 뽑아내려고 하는 수의 위치를 순서대로 입력받는다.
#         3. 큐 리스트 안에 수를 넣어놓는다.
# 2단계 : 
# 3단계 :

import sys
input = sys.stdin.readline

from collections import deque

# 1단계
N, M = map(int, input().split())
queue = deque()

num = list(map(int, input().split()))

for i in range(1, N+1):
    queue.append(i)
    
# 2단계
cnt2 = 0 
cnt3 = 0

# for i in range(0, M):
#     while True:
#         if(queue[0] == num[i]):
#             queue.popleft()
#             break
#         else:
#             if(queue.index(num[i]) < len(queue)/2): #2의 index번호는 현재 1이다. 따라서 5보다 작기때문에 왼쪽수를 오른쪽으로 이동한다.
#                 while(queue[0] != num[i]):
#                     queue.append(queue[0])
#                     queue.popleft() #가장 앞(왼쪽) 수를 삭제한다.
#                     cnt2 += 1
#                     break
#             else: #9의 index번호는 7이다. 따라서 4.5보다 크기 때문에 오른쪽수를 왼쪽으로 이동한다.
#                 while(queue[0] != num[i]):
#                     queue.appendleft(queue[0])
#                     queue.pop() #가장 뒤(오른쪽) 수를 삭제한다.
#                     cnt3 += 1
#                     break
# print(cnt2 + cnt3)

for i in range(0, M):
    while True:
        if(queue.index(num[i]) < len(queue)/2): #2의 index번호는 현재 1이다. 따라서 5보다 작기때문에 왼쪽수를 오른쪽으로 이동한다.
            while(queue[0] != num[i]):
                queue.append(queue[0])
                queue.popleft() #가장 앞(왼쪽) 수를 삭제한다.
                cnt2 += 1

        elif(queue.index(num[i]) > len(queue)/2): #9의 index번호는 7이다. 따라서 4.5보다 크기 때문에 오른쪽수를 왼쪽으로 이동한다.
            while(queue[0] != num[i]):
                queue.appendleft(queue[0])
                queue.pop() #가장 뒤(오른쪽) 수를 삭제한다.
                cnt3 += 1

        elif(queue[0] == num[i]):
            queue.popleft()
            break
print(cnt2 + cnt3)
            
            
#10 3 -> 큐의 크기10(1,2,3,4,5,6,7,8,9,10), 뽑아내려고 하는 수의 개수3(2, 9, 5)
#왼쪽1칸이동(2,3,4,5,6,7,8,9,10,1) -> 2를 뽑아내기.
#오른쪽3칸이동(9,10,1,3,4,5,6,7,8) -> 9를 뽑아내기.
#오른쪽4칸이동(5,6,7,8,9,10,1,3,4) -> 5를 뽑아내기.
#총합 8!!!

# 3단계

    
# 주의할 점
# 1. 큐는 선입선출 방식이지만 덱은 양방향에서 삽입과 삭제 가능하기에 시간 복잡도가 O(1)이므로 deque를 이용하여 양방향 순환 큐의 문제를 해결하면 된다.
# 2. 
