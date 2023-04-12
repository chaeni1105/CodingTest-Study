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
# -----------------------------------------------------------------------------
# 미니맥스 알고리즘이란?
# 3번으로 제한을 둔 예시를 계산해보겠습니다.
# 마지막 최종 score가 정해질 때에는 한 가지 밖에 없기 때문에 점수를 그대로 올려줍니다.
# 다음은 플레이어의 턴이기 때문에 '미니'전략으로 가장 점수가 낮은 경우를 올려줍니다.
# 다음은 컴퓨터 턴이기 때문에, 컴퓨터에게 가장 유리한 '맥스'점수를 올려줍니다.
# 결국 컴퓨터는 최적의 수를 알게 됩니다.(비기거나 이길 수 있는 수를 찾을 수 있습니다.)
# 이렇게 3번을 계산하는 것은 간단하지만, 처음부터라면 9! 약 36만번의 계산량을 가지는 것을 알 수 있습니다.
# 따라서 깊이를 정해서, 일정 수준까지의 깊이만 경우의 수를 확인하는 방법이 필요합니다.
# 하지만, 9번이므로 그냥 구현해보았습니다.

# 이 함수는 게임판의 한 줄을 인자로 받아 그 줄에서 컴퓨터가 선택할 최선의 수를 계산합니다. 
#  empty는 해당 줄에 돌이 하나도 없는지, user는 해당 줄에 유저의 돌이 몇 개 있는지, 
# com은 해당 줄에 컴퓨터의 돌이 몇 개 있는지를 나타냅니다. 
# 현재 컴퓨터가 유리한 상태인지, 불리한 상태인지를 확인하고 중첩 if문으로 들어가 임의로 가치를 매깁니다.
def max_value(none_,user,computer,min_max_):
    if(min_max_=='min'):    # 플레이어 턴에는 컴퓨터에게 가장 불리한 방법인 미니 (유저에게는 유리합니다.)
        if none_: return 1       # 라인이 전부 비어있다면? + 임의로 1의 가치를 매겼습니다.
        if computer: return 0        # 라인에 x가 하나라도 있다면?(User 돌 1개 존재) + 임의로 0의 가치를 매겼습니다.
        if user == 1: return 3    # 라인에 o가 1개 있다면?(Computer 돌 2개 존재) + 임의로 3 의 가치를 매겼습니다.
        if user == 2: return 7    # 라인에 o가 2개 있다면?(Computer 돌 2개 존재) + 임의로 7의 가치를 매겼습니다.
        
    if(min_max_ =='max'):    # 컴퓨터 턴에는 컴퓨터에게 가장 유리한 맥스 
        if none_: return 1       # 라인이 전부 비어있다면? + 임의로 1의 가치를 매겼습니다.
        if user: return 0        # 라인에 o가 하나라도 있다면?(User 돌 1개 존재) + 임의로 0의 가치를 매겼습니다.
        if computer == 1: return 3      # 라인에 x가 1개 있다면?(Computer 돌 2개 존재) + 임의로 3의 가치를 매겼습니다. 
        if computer == 2: return 7      # 라인에 x가 2개 있다면?(Computer 돌 2개 존재) + 임의로 7의 가치를 매겼습니다.   
        
# 보드 위치에서, 더해줘야할 줄의 개수를 저장한 리스트입니다.
pos_list = {'00':3,'01':2,'02':3,'10':2,'11':4,'12':2,'20':3,'21':2,'22':3}

# minimax함수에서는 사용자가 둔 수 이후에 대한 탐색과 컴퓨터가 둔 수 이후에 대한 탐색을 재귀적’으로 수행됩니다.
# 이 때, 사용자는 값을 최대화 하는쪽으로 / 컴퓨터는 값을 최소화 하는 쪽으로 탐색합니다.
# 재귀적으로 탐색을 수행하다보면 승패가 결정된 값이 반환됩니다.
def minimax(board,i_idx,j_idx):
    min_ = 0
    max_ = 0
    sum_list = pos_list[str(i_idx) + str(j_idx)] #행렬에 따라 사전에서 맞는 줄의 개수를 불러와서 조건에 따라 더함 
    
    # 저는 처음으로 돌을 뒀을 때, 되는 경우의 수를 전부 나누었습니다.
    # 따라서 아래 코드부터는 반복되는 부분이 존재합니다.
    # 먼저 가로 라인, 세로 라인, 대각 라인입니다.
    if sum_list==3:
        none_=True # 빈 곳 초기화
        computer=0 # computer 초기화
        user=0 # user 초기화
        for a in range(3): # 가로 라인
            if board[a][j_idx]==1:
                none_=False
                user+=1
            elif board[a][j_idx]==2:
                none_=False
                computer+=1
        min_+=max_value(none_,user,computer,'min') #min 값을 min_에 넣습니다.
        max_+=max_value(none_,user,computer,'max') #max 값을 max_에 넣습니다.
        
        none_=True # 빈 곳 초기화
        computer=0 # computer 초기화
        user=0 # user 초기화
        for b in range(3): # 세로 라인
            if board[i_idx][b]==1:
                none_=False
                user+=1
            elif board[i_idx][b]==2:
                none_=False
                computer+=1
        min_+=max_value(none_,user,computer,'min') #min 값을 min_에 넣습니다.
        max_+=max_value(none_,user,computer,'max') #max 값을 max_에 넣습니다.

        if j_idx==i_idx: # 오른쪽 대각선 라인
            none_=True # 빈 곳 초기화
            computer=0 # computer 초기화
            user=0 # user 초기화
            for d in range(3): # 대각 라인
                if board[d][d]==1:
                    none_=False
                    user+=1
                elif board[d][d]==2:
                    none_=False
                    computer+=1
            min_+=max_value(none_,user,computer,'min') #min 값을 min_에 넣습니다.
            max_+=max_value(none_,user,computer,'max') #max 값을 max_에 넣습니다.
        else:  # 왼쪽 대각선 라인
            none_=True # 빈 곳 초기화
            computer=0 # computer 초기화
            user=0 # user 초기화
            for d in range(3):
                if board[2-d][d]==1:
                    none_=False
                    user+=1
                elif board[2-d][d]==2:
                    none_=False
                    computer+=1
            min_+=max_value(none_,user,computer,'min') #min 값을 min_에 넣습니다.
            max_+=max_value(none_,user,computer,'max') #max 값을 max_에 넣습니다.
    elif sum_list==2:
        # 가로 라인, 세로 라인입니다.
        none_=True # 빈 곳 초기화
        computer=0 # computer 초기화
        user=0 # user 초기화
        for b in range(3): # 가로 라인
            if board[i_idx][b]==1:
                none_=False
                user+=1
   
            elif board[i_idx][b]==2:
                none_=False
                computer+=1
        min_+=max_value(none_,user,computer,'min') #min 값을 min_에 넣습니다.
        max_+=max_value(none_,user,computer,'max') #max 값을 max_에 넣습니다.

        none_=True # 빈 곳 초기화
        computer=0 # computer 초기화
        user=0 # user 초기화
        for a in range(3): # 세로 라인
            if board[a][j_idx]==1:
                none_=False
                user+=1
            elif board[a][j_idx]==2:
                none_=False
                computer+=1
        min_+=max_value(none_,user,computer,'min') #min 값을 min_에 넣습니다.
        max_+=max_value(none_,user,computer,'max') #max 값을 max_에 넣습니다.
              
    else:
        none_=True # 빈 곳 초기화
        computer=0 # computer 초기화
        user=0 # user 초기화
        for d in range(3): # 오른쪽 대각선 라인
            if board[d][d]==1: 
                none_=False
                user+=1
            elif board[d][d]==2:
                none_=False
                computer+=1
        min_+=max_value(none_,user,computer,'min') #min 값을 min_에 넣습니다.
        max_+=max_value(none_,user,computer,'max') #max 값을 max_에 넣습니다.

        none_=True # 빈 곳 초기화
        computer=0 # computer 초기화
        user=0 # user 초기화
        for d in range(3): # 왼쪽 대각선 라인
            if board[2-d][d]==1:
                none_=False
                user+=1
            elif board[2-d][d]==2:
                none_=False
                computer+=1
        min_+=max_value(none_,user,computer,'min') #min 값을 min_에 넣습니다.
        max_+=max_value(none_,user,computer,'max') #max 값을 max_에 넣습니다.
        
        none_=True # 빈 곳 초기화
        computer=0 # computer 초기화
        user=0 # user 초기화
        for b in range(3): # 가로 라인
            if board[i_idx][b]==1:
                none_=False
                user+=1
            elif board[i_idx][b]==2:
                none_=False
                computer+=1
        min_+=max_value(none_,user,computer,'min') #min 값을 min_에 넣습니다.
        max_+=max_value(none_,user,computer,'max') #max 값을 max_에 넣습니다.

        none_=True # 빈 곳 초기화
        computer=0 # computer 초기화
        user=0 # user 초기화
        for a in range(3): # 세로 라인
            if board[a][j_idx]==1:
                none_=False
                user+=1
            elif board[a][j_idx]==2:
                none_=False
                computer+=1
        min_+=max_value(none_,user,computer,'min') #min 값을 min_에 넣습니다.
        max_+=max_value(none_,user,computer,'max') #max 값을 max_에 넣습니다.
    
    minimax_val=max(min_,max_) # 최적의값을 찾아 minimax_val에 넣는다.
    return (i_idx,j_idx,minimax_val) # i_idx,j_idx,minimax_val 값을 반환한다.

score=[]
    # row, col = computer(board) # computer 함수를 다시 코딩 하시오
def computer(board):
    ### 현재 computer()함수는 빈곳에 랜덤하게 돌을 두도록 프로그래밍 되어있음
    ### 무조건 user를 상대로 [비기거나/이기도록] 미니맥스 알고리즘을 이용하여 다시 프로그래밍 하시오  
    ### computer() 함수와 minimax() 함수만 새로 작성하여 문제를 해결하시오
    row = 0
    col = 0
    
    # 둘 수 있는 곳이 몇 곳인지 확인한다. 
    for i_idx in range(3):
        for j_idx in range(3):
            if board[i_idx][j_idx] == 0:
                score.append(minimax(board, i_idx, j_idx)) # 미니맥스 알고리즘으로 얻은 값을 score 리스트에 추가합니다.
    
    score.sort(reverse=True, key=lambda x: x[2]) # 내림차순을 실행합니다.
    row,col,_=score.pop(0) # 맨 앞의 것을 pop()함수로 불러옵니다.

    return row, col # 미니맥스 알고리즘을 통해 얻은 행, 열 위치를 반환합니다.

# -----------------------------------------------------------------------------

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