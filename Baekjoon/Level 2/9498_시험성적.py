### [문제 분석]
# 목적 : 시험성적을 A~F까지 출력하기
# -> 조건문을 활용해서 점수 구간을 설정하여 A~F까지 출력한다.

### [문제 풀이]
# 1단계 : 시험성적을 입력받는다.
# 2단계 : if, elif, else 조건문을 사용해서 구간을 설정하고, A~F까지 출력한다.


# 1단계
score = int(input())

# 2단계
if(90 <= score <= 100):
    print("A")
elif(80 <= score <= 89):
    print("B")
elif(70 <= score <= 79):
    print("C")
elif(60 <= score <= 69):
    print("D")
else:
    print("F")
    
# else든 elif든 마지막 F는 뭐를 써도 상관없다!
# <= 등호 사용할 때, 조심할것! 잘 사용했는지 한 번 더 확인하기!