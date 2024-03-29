### [문제 분석]
# 목적 : 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램 작성
# -> 문자열을 입력받고, 공백을 만날때마다 cnt1씩 해주면 된다.

### [문제 풀이]
# 1단계 : 문자열을 입력받는다.
# 2단계 : 문자열의 길이만큼 반복하는 for문안에서 if만약 공백이 있을 때마다 cnt1씩 해준다. cnt의 초기값은 1로 설정한다.
# 3단계 :

import sys
input = sys.stdin.readline

# 1단계
S = input().strip() # 양측 공백제거.
cnt = 1

# 2단계
for i in range(len(S)):
    if(S[i] == " "):
        cnt += 1

# 3단계
print(cnt)
    
    
#다른 풀이
splitList = S.split() # ['The', 'Curious', 'Case', 'of', 'Benjamin', 'Button']
print(len(splitList)) # 6개 !!!
# -> split()함수를 사용해서 리스트에 6개의 단어를 넣고 리스트의 길이를 print하면 된다.
    
    
# 주의할 점
# 1. if(S[i] == ""): 할때 틀린점이 있다. 바로 공백은 " " 따옴표 사이의 공간을 띄어줘야 한다는거다. 조심하자.

# 2. 또한 문자열은 공백으로 시작하거나 끝날 수 있다. 라는 조건을 주의깊게 보아야한다.
#    이 조건때문에 양측 공백을 제거하는 strip()함수가 필요하기 때문이다.

# 아니 내 풀이가 왜 틀린거지? ㅁㄴㄹ어ㅏㅣㄴ어라ㅣㄷ너럼넝라ㅣㅓㅁㄴㅇ럼너린아ㅓㅏㅣ어ㅏㅣ어럼라ㅣㅓ리나ㅓ리ㅓㅇ ㅠㅠㅠㅠㅠ
