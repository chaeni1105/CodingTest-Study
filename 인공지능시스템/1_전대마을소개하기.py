#######
# 코드작성
#######
# 전대마을(행렬) 입력
n_row, n_col = map(int, input('마을의 행과 열 개수를 공백 기준으로 분리하여 입력: ').split())
village = []
for i in range(n_row):
    col = list(map(int, input(f'{i} 행 입력: ').split()))
    village.append(col)
 
# 마을에 있는 집 개수 출력
#### 코드 작성 ####
#print(f'전대마을에는 {#작성}개의 집, {#작성}개의 창고가 있습니다.')
#dfs