### [문제 분석]
# 목적 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램 작성
# -> 각 테스트 케이스마다 A+B를 출력한다.

### [문제 풀이]
# 1단계 : 무한으로 A와 B를 입력받고, A+B를 계속 출력해낸다.
# 2단계 : try-except문을 활용하여 테스트 케이스가 들어오지 않을 때, while문을 종료시킨다.

import sys
input = sys.stdin.readline

# 1단계
while(True):
    try:
        A, B = map(int, input().split())
        print(A+B)
    # 2단계
    except:
        break

    
# 주의할 점
# 테스트케이스(입력)이 얼마나 들어올지 모르는 상황이다.(무한 반복)
# 끝나는 시점의 조건도 걸려있지 않다.
# 이런 경우 try, except로 테스트케이스가 들어오지 않을 때,
# except의 break로 while문을 종료시킨다.

# try : try안의 코드를 실행해봐라.
# except : try 코드가 안될경우 except 안의 명령어를 수행해라.
