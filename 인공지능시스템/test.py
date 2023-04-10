# <문제 풀이>
# 1. 방문하여 1인 곳은 방문표시하기
# 2. 1번을 기준으로 상하좌우, 8칸에 1이 있나 확인하기
# 3. 1이 있다면, 해당 집으로 방문하면서 cnt 1 증가시키기
# 4. 1~3 과정을 반복하여 최종 cnt 반환 -> 집과 창고 분리하는데 사용
# 5. 전체 행렬에 1~4 과정을 반복하여 전대마을 집/창고 분리하기

# import sys
# input = sys.stdin.readline

dx=[-1, 1, 0, 0, -1, 1, 1, -1]
dy=[0, 0, -1, 1, 1, -1, 1, -1]

# 전대마을(행렬) 입력
n_row, n_col = map(int, input('마을의 행과 열 개수를 공백 기준으로 분리하여 입력: ').split())
village = []

for i in range(n_row):
    col = list(map(int, input(f'{i} 행 입력: ').split()))
    village.append(col)
    
cnt = 0
result=[]

def dfs(x,y):
    global cnt
    village[x][y] = 0 #방문한 곳 0으로 만들기
    cnt+=1 #카운트 수 늘리기
    for i in range(8) : #상하좌우로 움직이기
        nx = x +dx[i]
        ny = y +dy[i]
        if nx < 0 or nx >= n_row or ny < 0 or ny >= n_col :
            #만약 움직인 좌표가 범위를 벗어났다면 continue
            continue
        if village[nx][ny] == 1 :
            #움직인 좌표에 집이 있다면 다시 dfs탐색
            dfs(nx,ny)

home = 0
changgo = 0

for i in range(n_row) :
    for j in range(n_col) :
        #이중 for문으로 matrix를 하나하나 돌으면서 1인 구간 찾기(시작점 찾기)
        if village[i][j] == 1:
            cnt = 0 #시작 전 카운트 초기화
            dfs(i,j)
            result.append(cnt) #탐색 끝난 후 카운트 값 저장
            
for i in range(len(result)):
    if result[i] == 1:
        changgo += 1
        
home = len(result) - changgo

# 마을에 있는 집 개수 출력
print(f'전대마을에는 {home}개의 집, {changgo}개의 창고가 있습니다.')