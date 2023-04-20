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
    def win_condition(self, board):
        # 리턴값 0: 컴퓨터 승리 / 1: 플레이어 승리 / 2: 승패 결정 X 
        for player in ['X', 'O']:
            # 가로줄 검사
            for i in range(size):
                if board[i][0] == player and board[i][1] == player and board[i][2] == player:
                    if player == self.computer:
                        return 0
                    else:
                        return 1
            # 세로줄 검사
            for i in range(size):
                if board[0][i] == player and board[1][i] == player and board[2][i] == player:
                    if player == self.computer:
                        return 0
                    else:
                        return 1
            # 대각선 검사
            if board[0][0] == player and board[1][1] == player and board[2][2] == player:
                if player == self.computer:
                    return 0
                else:
                    return 1
            if board[0][2] == player and board[1][1] == player and board[2][0] == player:
                if player == self.computer:
                    return 0
                else:
                    return 1

    # 게임 결과에 따른 minimax 알고리즘 점수를 리턴하는 함수 
    # 게임판(board)의 상태를 받아와서 게임 결과(result)에 따른 minimax 알고리즘에서의 점수를 계산하여 리턴하는 함수입니다.
    def evaluate(self, board):
        result = self.win_condition(board) # 게임 결과를 받아옴
        if result == 0: # 컴퓨터 승리
            return 10
        elif result == 1: # 플레이어 승리
            return -10
        elif result == 2: # 승패 결정 X
            return 0
        else: # 무승부
            return 0 
    

    # 타겟이 이동할 수 있는 위치를 찾는 함수 
    # ismove 함수는 반환값으로 비어있는 모든 위치의 좌표를 담은 리스트를 반환합니다.
    def ismove(self, board):
        moves = []
        for i in range(size):
            for j in range(size):
                if board[i][j] == '':
                    moves.append((i, j))
        return moves


    # MiniMax 알고리즘 수행 함수 
    # 현재 차례가 컴퓨터인지, 플레이어인지를 구분하여 최적의 수를 찾아야합니다.
    # 현재 상태에서 가장 높은 점수를 얻을 수 있는 수를 찾는 경우. 컴퓨터가 수를 선택하고, 반대의 상황에서는 상대방이 
    # 가장 낮은 점수를 얻을 수 있는 수를 선택해야 하므로 플레이어가 수를 선택합니다. 
    # 최적의 수를 찾을 때마다 이에 따른 점수와 해당 수를 함께 저장하여 리턴합니다.
    
    def minimax(self, board, depth, is_maximizing):
        # 리턴값 : best_score, best_move (플레이어가 갈 수 있는 최적의 위치와 이에 따른 점수 리턴)
        # 게임이 끝났으면 현재 보드판 상태를 평가하고 점수를 리턴
        result = self.win_condition(board)
        if result != 2:
            return self.evaluate(board), None

        if is_maximizing:
            # 컴퓨터 차례인 경우, 최고의 점수를 찾기 위해 가능한 모든 수를 시도
            best_score = -math.inf
            best_move = None
            for move in self.ismove(board):
                board[move[0]][move[1]] = self.computer
                score, _ = self.minimax(board, depth+1, False)
                board[move[0]][move[1]] = ''
                if score > best_score:
                    best_score = score
                    best_move = move
            return best_score, best_move

        else:
            # 플레이어 차례인 경우, 상대방이 최소한의 점수를 얻을 수 있도록 최적의 수를 선택
            best_score = math.inf
            best_move = None
            for move in self.ismove(board):
                board[move[0]][move[1]] = self.player
                score, _ = self.minimax(board, depth+1, True)
                board[move[0]][move[1]] = ''
                if score < best_score:
                    best_score = score
                    best_move = move
            return best_score, best_move


    # 컴퓨터가 이동할 최적의 위치를 받는 함수 
    def best_pos(self):
    	# 컴퓨터가 이동할 최적의 위치 
        position = self.minimax(self.board)[1]

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
    result = game.win_condition(game.board) # 컴퓨터가 진행하기 전 게임 상황 확인 
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
    result = game.win_condition(game.board) # 플레이어가 진행하기 전 게임 상황 확인 
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