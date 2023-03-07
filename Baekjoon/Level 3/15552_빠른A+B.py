### [문제 분석]
# 목적 : input 대신 sys.stdin.readline을 사용하여 입출력 방식을 빠르게 바꿔본다.
# -> . 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있기 때문이다.

### [문제 풀이]
# 1단계 : import sys를 하고, sys.stdin.readline이용하여, 시간초과가 일어나는 것을 막는다.
# 2단계 : 테스트케이스의 개수 T를 입력 받고, 다음 T줄에는 각각 두 정수 A와 B를 입력받아 이를 더한다.


# 1단계
import sys
input = sys.stdin.readline

# 2단계
T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    print(A+B)
    
# 주의할 점 X

# 참고로 알게된 사항
# input = sys.stdin.readline을 먼저 써주면 int(input())으로 축약해서 쓸 수 있다. (앞에 import sys를 써줘야한다.)

# 입력을 다 받고 나서야 출력을 할 필요는 없습니다. 입력과 출력을 번갈아서 해도 됩니다. 근본적으로 입력 파일과 출력 파일은 분리되어 있습니다.