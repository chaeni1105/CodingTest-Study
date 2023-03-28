### [문제 분석]
# 목적 : 입력 받은 대로 출력하는 프로그램 작성
# -> 입력받은 그대로를 출력시킨다

### [문제 풀이]
# 1단계 : 문자열을 입력받는다
# 2단계 : 문자열을 출력한다

import sys
input = sys.stdin.readline

# 1단계
S = input()

# 2단계
while True:
    try:
        print(S)
    except EOFError:
        break

    
# 주의할 점
# 예외 처리 구문 : try~ except~문\
# try: (예외가 발생할 수도 있는 코드)
# except: (예외가 발생했을 경우 실행되는 코드)
# EOFError : 입력이 끝남(End Of File) 에러
# 데이터가 없어 더 이상 값을 읽을 수 없을 때 발생하는 에러