### [문제 분석]
# 목적 :고양이 출력
# -> 고양이 모양을 print()함수를 이용하여 출력하기.

### [문제 풀이]
# 1단계 : 백준에서 고양이 모양을 복사한다.
# 2단계 : 백슬래시 출력을 위해, 1개인 백슬래시를 2개로 바꾼다!
# 3단계 : 한줄씩 출력하여 줄바꿈을 해준다!

print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")

# 주의할점
# \n : 줄바꿈
# \t : 탭(키보드의 tap과 같은기능)
# \b : 백스페이스
# 위와같은 이스케이프 시퀀스들 때문에, 백슬래시만 출력하려면 에러가 뜬다.
# 따라서 \\ 백슬래시를 두 번 써야 하나를 출력해낼 수 있다.
# \+ 하면 +도 출력할 수 있다.

