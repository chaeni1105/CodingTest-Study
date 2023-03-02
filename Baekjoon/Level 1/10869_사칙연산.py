### [문제 분석]
# 목적 : A+B, A-B, A*B, A/B(몫), A%B(나머지) 출력
# -> A+B, A-B, A*B, A/B(몫), A%B(나머지) 출력시키기

### [문제 풀이]
# 1단계 : 두 정7 3수 A와 B를 입력받은 다음, print()함수를 반복적으로 이용해서 출력한다.

A, B = map(int, input().split())
print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)