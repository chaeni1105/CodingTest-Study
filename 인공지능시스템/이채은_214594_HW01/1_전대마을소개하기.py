# <문제 풀이>
# 1. 방문하여 1인 곳은 방문표시하기
# 2. 1번을 기준으로 상하좌우, 8칸에 1이 있나 확인하기
# 3. 1이 있다면, 해당 집으로 방문하면서 all_house 1 증가시키기
# 4. 1~3 과정을 반복하여 최종 all_house 반환 -> 집과 창고 분리하는데 사용
# 5. 전체 행렬에 1~4 과정을 반복하여 전대마을 집/창고 분리하기

# 전대마을(행렬) 입력받기
n_row, m_col = map(int, input('마을의 행과 열 개수를 공백 기준으로 분리하여 입력: ').split())
village = [] # 빈 2차원 리스트를 생성한다

# 2차원 리스트의 전대마을 정보를 입력받는다
for i in range(n_row):
    col = list(map(int, input(f'{i} 행 입력: ').split()))
    village.append(col)
    
all_house = 0 # 몇개의 집이 인접해있는지 알기 위해 all_house 변수를 초기화한다
sum_house = [] # 결과값을 담을 빈 리스트 생성한다

# 상,하,좌,우와 같이 주변 8칸의 위치 재귀적으로 호출하기 위해서 미리 리스트를 생성한다
da = [-1, 1, 0, 0, -1, 1, 1, -1]
db = [0, 0, -1, 1, 1, -1, 1, -1]

# DFS 알고리즘!
# x, y 위치인 노드를 방문하는데, 이 노드와 연결된 모든 노드들을 전부 방문한다
def dfs(a,b): # dfs함수를 정의한다.
    global all_house # 글로벌 전역변수 cnt를 선언한다.
    village[a][b] = 0 # 노드를 방문 처리한다. (0으로 값을 바꾼다)
    all_house += 1 # cnt를 1 증가시킨다.
    for i in range(0, 8, 1) : # 상,하,좌,우 위치를 구한다.
        na = a + da[i]
        nb = b + db[i]
        if(na <= -1 or na >= n_row or nb <= -1 or nb >= m_col):
            continue # 만약 주어진 범위를 벗어나면 continue를 반환한다
        if(village[na][nb] == 1):
            # 움직인 좌표에 집이 있다면 다시 dfs탐색
            dfs(na,nb) # 상,하,좌,우 위치를 재귀적으로 호출한다

home = 0 # 집의 개수를 초기화한다.
changgo = 0 # 창고의 개수를 초기화한다.

# 집 개수를 찾아내기
for i in range(n_row) :
    for j in range(m_col) :
        # 반복문 수행하면서 전대마을 행렬 전부를 dfs함수에 적용시킨다.
        if village[i][j] == 1:
            all_house = 0 # all_house를 초기화한다
            dfs(i,j) # dfs 함수를 호출한다.
            sum_house.append(all_house) # sum_house리스트에 몇개의 1이 인접해있는 집인지 저장한다.
            
for i in range(len(sum_house)): # 창고+집의 총 개수만큼 반복한다.
    if sum_house[i] == 1: # 만약 한 개의 1로 구성된 곳이라면 집이아니라 창고이다.
        changgo += 1 # 창고 +1
        
home = len(sum_house) - changgo # 창고+집의 총 개수에서 창고를 뺀 수는 집의 갯개수이다.

# 마을에 있는 집 개수 출력
print(f'전대마을에는 {home}개의 집, {changgo}개의 창고가 있습니다.')