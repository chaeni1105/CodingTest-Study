# 문제의 목적 : (0,0)의 출발지에 존재하는 로봇을 (N-1,M-1)의 도착지로 옮기는 최단거리를 계산하는 것이다.
# -> 전형적인 BFS 문제 유형이다.

# 1. 우주선이 차지하고 있는 위치가 두칸이다.
# -> 방문 여부를 관리하기 위해서는 우주선의 위치 정보를 튜플로 처리하면 된다. -> 집합 자료형 set을 사용한다.
# 2. 우주선이 이동하는 경우.
# -> 상,하,좌,우로 이동하는 경우이다.
# 3. 우주선이 회전하는 경우.
# -> 먼저 첫번째, 우주선이 가로로 놓인 상태에서 아래쪽으로 회전하는 경우가 있다.(아래쪽에 감시 시스템이 존재하지 않아야한다.)
# -> 두번째, 우주선이 가로로 놓인 상태에서 위쪽으로 회전하는 경우가 있다.(위쪽에 감시 시스템이 존재하지 않아야한다.)
# -> 세번째, 우주선이 세로로 놓인 상태에서 오른쪽으로 회전하는 경우가 있다.(오른쪽에 감시 시스템이 존재하지 않아야한다.)
# -> 네번째, 우주선이 세로로 놓인 상태에서 왼쪽으로 회전하는 경우가 있다.(왼쪽에 감시 시스템이 존재하지 않아야한다.)
# 4. 초기에 주어진 맵을 변형한다.
# -> 주변 외곽을 감시시스템으로 전부 둘러싸게 한다.

# 데큐 라이브러리 사용
from collections import deque

# 특정한 위치에서 이동 가능한 다음 위치를 반환하는 함수이다.
def possible_position(position_, board):
    
    # 상하좌우로 이동하는 경우 4가지 경우를 미리 지정합니다.
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    position_ = list(position_) # position을 집합에서 리스트로 변환시킵니다.
    result_position_ = [] # 반환 결과를 저장할 리스트를 생성한다. (이 위치들은 이동이 가능하다)
    # 00, 01, 10, 11인덱스의 값을 각각 4개의 값에 저장합니다.
    p1_a, p1_b, p2_a, p2_b = position_[0][0], position_[0][1], position_[1][0], position_[1][1] 

    # 현재 우주선이 위, 아래, 왼쪽, 아래쪽으로 이동할 수 있는지 확인합니다.
    for i in range(4):
        pp1_a, pp1_b, pp2_a, pp2_b = p1_a + dx[i], p1_b + dy[i], p2_a + dx[i], p2_b + dy[i]
        # 이동하려는 두 칸에 감시 시스템이 존재하는지 확인합니다.
        if board[pp1_a][pp1_b] == 0 and board[pp2_a][pp2_b] == 0:
            result_position_.append({(pp1_a, pp1_b), (pp2_a, pp2_b)})
            
    if p1_b == p2_b: # 현재 우주선이 세로일 때, 오른쪽/왼쪽으로 회전할 수 있는지 확인합니다.
        for i in [-1, 1]: # 왼쪽으로 회전하거나, 오른쪽으로 회전시킵니다.
            if board[p1_a][p1_b + i] == 0 and board[p2_a][p2_b + i] == 0: # 왼쪽 or 오른쪽 두 칸이 모두 비어 있을 때,
                # 위 칸을 통해 왼쪽/오른쪽으로 회전합니다.
                result_position_.append({(p1_a, p1_b), (p1_a, p1_b + i)})
                # 아래 칸을 통해 왼쪽/오른쪽으로 회전합니다.
                result_position_.append({(p2_a, p2_b), (p2_a, p2_b + i)})

    elif p1_a == p2_a: # 현재 우주선이 가로일 때, 위/아래로 회전할 수 있는지 확인합니다.
        for i in [-1, 1]: # 위쪽으로 회전하거나, 아래쪽으로 회전시킵니다.
            if board[p1_a + i][p1_b] == 0 and board[p2_a + i][p2_b] == 0: # 위쪽 or 아래쪽 두 칸이 모두 비어 있을 때,
                # 왼쪽 칸을 통해 위/아래로 회전합니다.
                result_position_.append({(p1_a, p1_b), (p1_a + i, p1_b)})
                # 오른쪽 칸을 통해 위/아래로 회전합니다.
                result_position_.append({(p2_a, p2_b), (p2_a + i, p2_b)})

    # 상하좌우, 회전으로 이동할 수 있는 모든 위치를 반환합니다.
    return result_position_

# 이 함수는 특정한 출발지에 존재하는 우주선을 도착지로 옮기는 최단시간을 계산하여 반환합니다.
def min_time(n, m, board): # n행, m열, 지도보드를 인자로 갖는 함수입니다. 

    # 먼저 지도보드를 1로 둘러쌉니다.
    new_board = [[1] * (n + 2) for _ in range(m + 2)]
    for i in range(n): # n행
        for j in range(m): # m열
            new_board[i + 1][j + 1] = board[i][j] # 지도보드를 1로 둘러싼 새로운 지도보드를 만듭니다.

    # BFS 알고리즘 !
    queue = deque() # queue 구현을 위해 deque라이브러리를 사용합니다.
    visited = [] # 방문처리를 위해 빈 리스트를 생성합니다.
    position = {(1, 1), (1, 2)} # 시작 위치입니다. 지도보드의 테두리를 1로 둘러 쌌으므로, 0,0 / 0,1 이 아니라 1씩 더한 1,1 / 1,2 위치입니다.
    queue.append((position, 0)) # 큐에 시작 위치를 추가합니다.
    visited.append(position) # 시작 위치를 방문 처리합니다.
    
    while queue: # 이 while문은 큐가 빌 때까지 반복합니다.
        position, time = queue.popleft() # 현재 위치와 현재 시간을 꺼냅니다.
        if (n, m) in position: # (n, m)에 우주선이 도착하면,
            return time # 최단 시간을 return합니다.
        
        for result_position in possible_position(position, new_board): # 이동할 수 있는 위치를 반환하는 함수를 for문 안에 호출합니다.
            if result_position not in visited: # 만약 방문하지 않은 위치라면,
                queue.append((result_position, time + 1)) # 큐에 위치와 1초를 더한 시간을 추가합니다.
                visited.append(result_position) # 위치를 방문 처리합니다.
    return 0

# 감시 공간 크기를 입력받습니다.
n, m = map(int, input('감시 공간 크기 입력: ').split())

board_ = [] # 빈 리스트를 생성합니다.
for s in range(n): # n행만큼 반복합니다.
    tmp = list(map(int, input(f'{s}행 입력: ').split())) # 행을 입력받습니다.
    board_.append(tmp) # 보드에 행을 추가하여 2차원 리스트를 생성합니다.

answer = min_time(n, m, board_) # 최단 시간을 반환하는 함수를 호출합니다.
print(f'감시 공간을 탈출할 수 있는 최단 시간은 {answer}초입니다.') # 정답을 출력합니다.