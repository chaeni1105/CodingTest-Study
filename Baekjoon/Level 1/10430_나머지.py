### [문제 분석]
# 목적 : (A+B)%C, ((A%C) + (B%C))%C, (A×B)%C, ((A%C) × (B%C))%C 출력
# -> 위의 네 가지 값을 구하기

### [문제 풀이]
# 1단계 : A,B,C를 입력받은 다음, 차례대로 print()출력한다.

A, B, C = map(int, input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)
