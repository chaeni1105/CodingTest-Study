### [문제 분석]
# 목적 : 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램 작성
# -> 문자를 특정 횟수만큼 더해주는 구현문제이다. 

### [문제 풀이]
# 1단계 : 테스트케이스 개수 T를 입력받는다. 둘째줄에는 반복 횟수 R과 문자열 S를 입력받는다.
# 2단계 : 문자열을 리스트로 생각해본다.(ABC면 S[0], S[1], S[2])
#         문자열의 길이만큼 반복하는 반복문 안에서 S[0]을 R만큼 반복추가해서, '새로운 answer'리스트에 추가한다.
# 3단계 : answer 리스트 문자열을 출력한다.

import sys
input = sys.stdin.readline

# 1단계
T = int(input())
for i in range(T):
    
    RS = list(map(str, input().split()))
    R = int(RS[0])
    S = str(RS[1])

    # print(type(R)) -> <class 'int'>
    # print(type(S)) -> <class 'str'>

    # 2단계
    for i in range(len(S)):
        print(S[i]*R, end='')
    print()

    
# 주의할 점
# 1. R은 int type으로, S는 str타입으로 받아야한다. 
#    따라서, list형태로 입력을 받고, 인덱스 0번과 1번을 차례로 R, S로 했어야 했다.

# 2. print할때, i를 프린트하면 0~answer의길이 까지 나오기만한다.
#    따라서, answer[i]를 프린트하여야 리스트안의 원소가 나오게된다.

# 3. 굳이 answer 리스트를 따로 만들지 않아도 된다.
#    answer리스트에 추가하는게 아니라 바로, 출력해주면 된다.

# 4. print()를 해서 정답이 나오면 다시 입력받을 수 있게 줄바꿈을 해줘야한다.. !!!