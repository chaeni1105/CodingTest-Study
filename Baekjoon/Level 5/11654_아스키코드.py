### [문제 분석]
# 목적 : 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.
# -> 입력으로 주어진 글자의 아스키 코드 값을 출력한다.

### [문제 풀이]
# 1단계 : 글자를 입력받는다.(알파벳 소문자, 대문자, 숫자 0-9중 하나)
# 2단계 : 문자의 아스키 코드값을 리턴하는 함수 ord()를 사용한다. / 참고로 아스키 코드값을 문자로 출력해주는 함수는 chr()이다.


# 1단계
str_ = input()

# 2단계
print(ord(str_))

    
# 주의할 점
