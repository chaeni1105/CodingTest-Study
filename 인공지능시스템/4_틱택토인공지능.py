### 객체지향 / 인공지능 설계 프로젝트 HW1
### 학번 : 20XXXXXX
### 이름 : 000
### 제출일자 : 22-09-XX

import random

def board_visualization(board):
    ### 틱택토 게임 출력 함수  
    for i_idx in range(3):
        for j_idx in range(3):
            
            if board[i_idx][j_idx] == 0: # not occupied
                print("▨", end='')
            elif board[i_idx][j_idx] == 1: # user
                print("○", end='')
            elif board[i_idx][j_idx] == 2: # computer
                print("×", end='')
            else:
                pass
        print()        
    
def board_turn(board, row, col, val):
    
    if 0 <= row < 3 and 0 <= col < 3:
        if board[row][col] == 0:
            board[row][col] = val
            return 1
        else:
            print("그곳에 돌을 둘 수 없습니다. 다시 입력하세요.")
            return 0
    else:
        print("그곳에 돌을 둘 수 없습니다. 다시 입력하세요.")
        return 0
        
    
def win_condition(v1,v2,v3): # 사용자 승리 return 100, 컴퓨터 승리 return -100, 무승부 return 0
    if v1 == v2 == v3:  
        if v1 == 1: return 100
        elif v2 == 2: return -100
        else: return 0
    else:
        return 0
        
    
def game_result(board): # 사용자 승리 return 100, 컴퓨터 승리 return -100, 무승부 return 0
    result = 0
    # check rows
    for i_idx in range(3):
        result = win_condition(board[i_idx][0],board[i_idx][1],board[i_idx][2])      
        if result != 0: return result
      
    # check cols
    for i_idx in range(3):
        result = win_condition(board[0][i_idx],board[1][i_idx],board[2][i_idx])
        if result != 0: return result
        
    #check diagonals
    result = win_condition(board[0][0],board[1][1],board[2][2])      
    if result != 0: return result
    result = win_condition(board[0][2],board[1][1],board[2][0])      
    if result != 0: return result
        
    return result

def position():
    row = int(input("돌을 놓을 행을 입력하세요 (0~2):"))
    col = int(input("돌을 놓을 열을 입력하세요 (0~2):"))
    
    return row, col


def minimax(board, turn):
    # board : 현재 틱택토 보드
    # turn : user 또는 computer의 차례
    
    # hint
    # 1. minimax함수에서는 사람이 이기면 큰 수 (+100), 컴퓨터가 이기면 작은수 (-100), 비기면 중간값(0) 반환 - game_result() 함수 활용
    # 2. ① 사용자가 둔 수 이후에 대한 탐색과 ② 컴퓨터가 둔 수 이후에 대한 탐색을 재귀적’으로 수행
    #    단, 사용자는 값을 최대화 하는쪽으로 / 컴퓨터는 값을 최소화 하는 쪽으로 탐색 
    #    재귀적으로 탐색을 수행하다보면 승패가 결정된 값이 반환됨
    
    
    return minimax_val

    
def computer(board):
    
    ### 현재 computer()함수는 빈곳에 랜덤하게 돌을 두도록 프로그래밍 되어있음
    ### 무조건 user를 상대로 [비기거나/이기도록] 미니맥스 알고리즘을 이용하여 다시 프로그래밍 하시오  
    ### computer() 함수와 minimax() 함수만 새로 작성하여 문제를 해결하시오
    
    row = 0
    col = 0
    empty_cnt = 0    
    for i_idx in range(3):
        for j_idx in range(3):
            if board[i_idx][j_idx] == 0:
                empty_cnt+=1

    rnd_idx = random.randrange(1,empty_cnt)
    
    empty_cnt = 0
    
    for i_idx in range(3): 
        for j_idx in range(3):
            if board[i_idx][j_idx] == 0:          
                if empty_cnt == rnd_idx:
                    row = i_idx
                    col = j_idx
                    return row, col
                    
                empty_cnt+=1
                
        
    return row, col    


### 게임 시작
print("게임 시작")
board = [[0,0,0],[0,0,0],[0,0,0]]
board_visualization(board)

for i_idx in range(5): # 플레이어는 최대 5번 돌을 둔다
    ###### User ######
    print("============= Your turn =============")
    row, col = position()
    while board_turn(board, row, col,1) == 0:
        row, col = position()
        
    board_visualization(board)
    if game_result(board) == 100:
        print("사용자가 승리하였습니다.")
        break
    elif game_result(board) == -100:
        print("컴퓨터가 승리하였습니다.")
        break      
    ########################
    
    
    
    ###### Computer ######
    print("============= Computer =============")
    row, col = computer(board) # computer 함수를 다시 코딩 하시오
    board_turn(board, row, col, 2)
    board_visualization(board)   
    if game_result(board) == 100:
        print("사용자가 승리하였습니다.")
        break
    elif game_result(board) == -100:
        print("컴퓨터가 승리하였습니다.")
        break
    ########################

    
if game_result(board) == 0:
    print("비겼습니다.")