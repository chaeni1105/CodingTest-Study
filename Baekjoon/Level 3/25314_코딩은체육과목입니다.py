### [문제 분석]
# 목적 : 혜아가 N바이트 정수까지 저장할 수 있다고 생각해서 칠판에 쓴 정수 자료형의 이름은 무엇인지 알아내기.
# -> 혜아가 N바이트 정수까지 저장할 수 있다고 생각하는 정수 자료형의 이름을 출력한다.

### [문제 풀이]
# 1단계 : 문제의 정수N을 입력받는다.
# 2단계 : 4byte에 long int 가 출력되고, 20byte에 long*5 int가 출력된다. 이말은 즉슨, N//4를 해서 나온 몫만큼 long이 출력되는것이다.
#        N//4만큼 for문을 돌려 long을 출력해보자.

import sys
input = sys.stdin.readline

# 1단계
N = int(input())

# 2단계
for i in range(N//4):
    print("long ", end='')
print("int")