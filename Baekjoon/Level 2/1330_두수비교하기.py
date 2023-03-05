### [문제 분석]
# 목적 : A와 B 비교
# -> A와 B를 비교해서 <, >, == 를 출력한다.

### [문제 풀이]
# 1단계 : A와 B를 입력받는다.
# 2단계 : if, elif, else 조건물을 사용해서 각각 <, >, ==를 출력한다.


# 1단계
A, B = map(int, input().split())

# 2단계
if(A > B):
    print(">")
elif(A < B):
    print("<")
else:
    print("==")
