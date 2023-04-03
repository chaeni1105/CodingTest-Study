import math

class Game():
    def __init__(self, size, board, player, computer):
        self.size = size         # 구름게임 맵 크기 (정방행렬)
        self.board = board       # 구름게임 맵 
        self.player = player     # 플레이어 위치 
        self.computer = computer # 컴퓨터 위치 

    # 구름게임 출력 함수 
    def board_visualization(self):
        for idx in range(self.size):
            for jdx in range(self.size):
                if self.board[idx][jdx] == 0:   # 낭떠러지 
                    print("□ ", end='')
                elif self.board[idx][jdx] == 1: # 구름 
                    print('▨ ', end='')
                elif self.board[idx][jdx] == 2: # 플레이어
                    print('◆ ', end='')
                elif self.board[idx][jdx] == 3: # 컴퓨터 
                    print('● ', end='')
                else:
                    pass
            print()


    # 플레이어 이동 위치 함수 
    def position(self):
        player = list(map(int, input(f'플레이어가 이동할 위치 입력: ').split()))
        # 맵을 벗어나지 않도록 설정 
        if player[0] >= self.size or player[1] >= self.size:
            self.position()
        
        # 이동할 위치가 구름이고 상하좌우 방향이라면 플레이어 위치로 변환 / 기존 위치는 낭떠러지로 변환 
        if self.board[player[0]][player[1]] == 1 and (abs(self.player[0]-player[0]) + abs(self.player[1]-player[1])) == 1:
            self.board[self.player[0]][self.player[1]] = 0
            self.player = player
            self.board[player[0]][player[1]] = 2
        else:
            self.position()


    # 게임이 끝났는지 확인하는 함수 
    def win_condition(self, board, 코드 작성):
        # 리턴값 0: 컴퓨터 승리 / 1: 플레이어 승리 / 2: 승패 결정 X 
        
        #### 코드 작성 ####

        pass # 코드 작성 후 삭제
    

    # 게임 결과에 따른 minimax 알고리즘 점수를 리턴하는 함수 
    def evaluate(self, board, 코드 작성):
        result = self.win_condition(board, 코드 작성) # 게임 결과를 받아옴

        #### 코드 작성 ####

        pass # 코드 작성 후 삭제 
    

    # 타겟이 이동할 수 있는 위치를 찾는 함수 
    def ismove(self, board, 코드 작성):
        moves = [] # 초기화 
        
        #### 코드 작성 ####

        return moves


    # MiniMax 알고리즘 수행 함수 
    def minimax(self, board, 코드 작성):
        # 리턴값 : best_score, best_move (플레이어가 갈 수 있는 최적의 위치와 이에 따른 점수 리턴)

        #### 코드 작성 ####
        
        pass # 코드 작성 후 삭제 


    # 컴퓨터가 이동할 최적의 위치를 받는 함수 
    def best_pos(self):
    	# 컴퓨터가 이동할 최적의 위치 
        position = self.minimax(self.board, 코드 작성 )[1]

        # 위치를 받아와서 구름게임 맵과 컴퓨터 위치 변경 
        self.board[self.computer[0]][self.computer[1]] = 0
        self.computer = [position[0], position[1]]
        self.board[position[0]][position[1]] = 3


# 구름게임 맵 입력 
board = []
size = int(input('구름게임 맵 크기(정방행렬): '))
print('낭떠러지 : 0     구름 : 1')
for s in range(size):
    tmp = list(map(int, input(f'{s}행 입력: ').split()))

while True: # 플레이어 시작 위치 입력 
    player = list(map(int, input(f'플레이어 시작 위치 입력: ').split()))
    if player[0] >= 0 and player[0] < size and player[1] >= 0 and player[1] < size:
        if board[player[0]][player[1]] == 1:
            break
board[player[0]][player[1]] = 2

while True: # 컴퓨터 시작 위치 입력 
    computer = list(map(int, input(f'컴퓨터 시작 위치 입력: ').split()))
    if computer[0] >= 0 and computer[0] < size and computer[1] >= 0 and computer[1] < size:
        if board[computer[0]][computer[1]] == 1:
            break
board[computer[0]][computer[1]] = 3

# 구름게임 세팅 
game = Game(size, board, player, computer)

print("============= Initial State =============")
game.board_visualization()

# 구름게임 시작 
while True:
    print("=============== Computer ================")
    result = game.win_condition(game.board, 코드 작성) # 컴퓨터가 진행하기 전 게임 상황 확인 
    if result == 0: # 컴퓨터가 이긴 경우 게임 종료 
        game.board_visualization()
        print('컴퓨터가 승리하였습니다.')
        break
    elif result == 1: # 플레이어가 이긴 경우 게임 종료 
        game.board_visualization()
        print('플레이어가 승리하였습니다.')
        break
    game.best_pos()
    game.board_visualization()

    print("=============== Your turn ===============")
    result = game.win_condition(game.board, 코드 작성) # 플레이어가 진행하기 전 게임 상황 확인 
    if result == 0:
        game.board_visualization()
        print('컴퓨터가 승리하였습니다.')
        break
    elif result == 1:
        game.board_visualization()
        print('플레이어가 승리하였습니다.')
        break
    game.position()
    game.board_visualization()