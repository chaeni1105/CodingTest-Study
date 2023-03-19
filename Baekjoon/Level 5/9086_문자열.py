### [문제 분석]
# 목적 : 문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램 작성
# -> 각 테스트 케이스에 대해서 주어진 문자열의 첫 글자와 마지막 글자를 연속하여 출력한다.

### [문제 풀이]
# 1단계 : 테스트 케이스의 개수 T를 입력받고, 둘째줄부터는 T만큼 반복하는 for문 안에서 문자열을 입력받는다.
# 2단계 : 문자열의 첫 글자와 마지막 글자를 연속하여 출력한다.

import sys
input = sys.stdin.readline

# 1단계
T = int(input())
for i in range(T):
    S = input().rstrip("\n")
    # 2단계
    print(S[0]+S[len(S)-1])
    
# 주의할 점
# 엔터 입력을 무시해줘야 정확한 단어 길이가 나온다.
# 따라서  = input().rstrip("\n")을 해줘야한다.
