#######
#코드작성
#######
# 감시 공간 크기 입력
n, m = map(int, input('감시 공간 크기 입력: ').split())
board = []
for s in range(n): # 감시 공간 입력
 tmp = list(map(int, input(f'{s}행 입력: ').split()))
#### 코드 작성 ####
#print(f'감시 공간을 탈출할 수 있는 최단 시간은 {answer}초입니다.')