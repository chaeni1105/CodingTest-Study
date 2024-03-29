### [문제 분석]
# 목적 : 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램 작성
# -> 처음 등장하는 위치를 공백으로 구분해서 출력한다.(단어에 포함되어 있지 않다면 -1을 출력한다.)

### [문제 풀이]
# 1단계 : a부터 z까지 중, not in S 일 때, -1일 출력한다.
# 2단계 : 만약 in S라면, S의 몇번째 자리에 위치하는지 출력한다.(index함수 활용)
# 3단계 :

import sys
input = sys.stdin.readline

# 1단계
S = input()
for i in range(97,123):
    if(chr(i) in S):
        print(S.index(chr(i)),"", end='')
    else:
        print("-1 ", end='')

# 2단계

# 3단계

    
# 주의할 점
# 1. 97~122는 아스키코드표에서 알파벳 'a'부터 'z'까지 나타낸다.

# 2. 문자의 아스키 코드값을 리턴하는 함수는 ord() 이고,
#    참고로 아스키 코드값을 문자로 출력해주는 함수는 chr()이다.

# 3. index() 함수 안에 b가 들어왔다면 0을 리턴해준다.
#    a가 들어왔다면 인덱스 1을 리턴해준다.