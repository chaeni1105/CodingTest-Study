### [문제 분석]
# 목적 : 할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램 작성
# -> 단순 구현 문제이다. 첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력해야한다.
#    8682라면, 처음 8까지 가는데 9초가 소요되고, 6에는 7초, 8에 9초, 2에 3초이다.
#    즉 처음 숫자 + 1을 cnt하고, 나머지 숫자들도 모두 +1을한 상태로 계속 더해주면 되는것이다.

import sys
input = sys.stdin.readline

### [문제 풀이]
# 1단계 : 첫째 줄에 알파벳 대문자로 이루어진 단어를입력받고,이를 숫자로 변경하여 리스트에 저장한다.
# 2단계 : 리스트의 길이만큼 반복하는 for문에서 num리스트의 모든값을 차례로 cnt에 더한다.
# 3단계 : cnt를 출력한다.


# 1단계
S = input()
num = []
cnt = 0

# UNUCIC -> [8, 6, 8, 2, 4, 2]
for i in range(len(S)):
    if(S[i] in "ABC"):
        num.append(2)
    elif(S[i] in "DEF"):
        num.append(3)
    elif(S[i] in "GHI"):
        num.append(4)
    elif(S[i] in "JKL"):
        num.append(5)
    elif(S[i] in "MNO"):
        num.append(6)
    elif(S[i] in "PQRS"):
        num.append(7)
    elif(S[i] in "TUV"):
        num.append(8)
    elif(S[i] in "WXYZ"):
        num.append(9)
        
# 2단계

for i in range(len(num)):
    cnt += num[i] + 1
    

# 3단계
print(cnt)
    
# 주의할 점
# 1. 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
#    처음 위치로 돌아가므로, 그냥 num[0]부터 num[len(num)]까지 다 cnt에 더해주면 된다.

# 2. 꼭 예제 입출력 결과를 보고나서 문제 풀이를 설계하자.