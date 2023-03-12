### [문제 분석]
# 목적 : 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.) 
#        이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램 작성
# -> 2번연산만 한다음에 N-(2번연산횟수)해서 3번연산을 구하고 둘의 최솟값min()을 구한다.

### [문제 풀이]
# 1단계 : 1. 큐의 크기 N, 뽑아내려고 하는 수의 개수 M을 입력받는다. queue 리스트를 만든다.
#         2. 지민이가 뽑아내려고 하는 수의 위치를 순서대로 입력받는다.
#         3. 큐 리스트 안에 수를 넣어놓는다.
# 2단계 : 만약 뽑을 번호가 절반을 기점으로 더 왼쪽에 있으면 2번연산을 하고,가운데보다 더 오른쪽에 있으면 3번연산을 행한다.
#         그리고, 2,3번 연산을 통해 뽑아야할 수가 맨 앞으로 오면 제거하고 while문을 빠져나온다.

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
#         if(queue.index(num[i]) < len(queue)/2): #2의 index번호는 현재 1이다. 따라서 5보다 작기때문에 왼쪽수를 오른쪽으로 이동한다.
#             while(queue[0] != num[i]):
#                 queue.append(queue.popleft()) #가장 앞(왼쪽) 수를 삭제한다.
#                 cnt2 += 1

#         else: #9의 index번호는 7이다. 따라서 4.5보다 크기 때문에 오른쪽수를 왼쪽으로 이동한다.
#             while(queue[0] != num[i]):
#                 queue.appendleft(queue.pop()) #가장 뒤(오른쪽) 수를 삭제한다.
#                 cnt3 += 1
                
#         if(queue[0] == num[i]):
#             queue.popleft()
#             break
                
# print(cnt2 + cnt3)

for i in range(0, M):
    if(queue.index(num[i]) < len(queue)/2): #2의 index번호는 현재 1이다. 따라서 5보다 작기때문에 왼쪽수를 오른쪽으로 이동한다.
        while(queue[0] != num[i]):
            queue.append(queue.popleft()) #가장 앞(왼쪽) 수를 삭제한다.
            cnt2 += 1

    else: #9의 index번호는 7이다. 따라서 4.5보다 크기 때문에 오른쪽수를 왼쪽으로 이동한다.
        while(queue[0] != num[i]):
            queue.appendleft(queue.pop()) #가장 뒤(오른쪽) 수를 삭제한다.
            cnt3 += 1
                
    if(queue[0] == num[i]):
        queue.popleft()
            
                
print(cnt2 + cnt3)
            
            
#10 3 -> 큐의 크기10(1,2,3,4,5,6,7,8,9,10), 뽑아내려고 하는 수의 개수3(2, 9, 5)
#왼쪽1칸이동(2,3,4,5,6,7,8,9,10,1) -> 2를 뽑아내기.
#오른쪽3칸이동(9,10,1,3,4,5,6,7,8) -> 9를 뽑아내기.
#오른쪽4칸이동(5,6,7,8,9,10,1,3,4) -> 5를 뽑아내기.
#총합 8!!!
    
# 주의할 점
# 1. 큐는 선입선출 방식이지만 덱은 양방향에서 삽입과 삭제 가능하기에 시간 복잡도가 O(1)이므로 deque를 이용하여 양방향 순환 큐의 문제를 해결하면 된다.

# 풀리지 않는 의문. 물어보기 ㄱ
# queue.append(queue.popleft()) 가장 앞(왼쪽) 수를 삭제할 때, 이렇게 하지 않고,

# queue.append(queue[0])
# queue.popleft() 
# 이렇게 두 줄로 하면 시간초과가 뜬다. 그 이유가 무엇일까?
# 사실 while문이 있어야하는 이유를 모르겠다. -> 없어도 된다! 어차피 2,3번 연산안에 while문이 존재하여 맨 앞으로 수가 갈때까지 반복하므로!!
