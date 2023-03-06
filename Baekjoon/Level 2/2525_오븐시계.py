### [문제 분석]
# 목적 : 오븐구이가 끝나는 시각을 계산하는 프로그램 작성
# -> 요리를 시작하는 시각과 요리하는 데 필요한 시간이 분단위로 주어졌을 때, 요리가 끝나는 시각을 계산하여 출력한다.

### [문제 풀이]
# 1단계 : 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)으로 입력받고, 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)도 입력받는다.
# 2단계 : 1. 분(B)과 요리시간(C)를 더했을 때, 60을 안넘는 경우 -> B + C
#        2. 분(B)과 요리시간(C)를 더했을 때, 60을 넘는 경우 -> A + ((B + C)//60), (B + C)%60 => A는 60으로나눈 몫만큼 더해줘야한다.
#        3. 분(B)과 요리시간(C)를 더했을 때, 60이 되는 경우 -> A + ((B + C)//60), B = 0


# 1단계
A, B = map(int, input().split())
C = int(input())

# 2단계
if((B+C) < 60):
    B = B+C
    print(A, B)
    
elif((B+C) > 60):
    A = A + ((B + C)//60)
    B = (B + C)%60 #주의 (이 라인이 A보다 먼저 실행되면 B가 바뀐상태로 A가 실행되므로 조심해야한다.)
    if(A >= 24):
        A = A - 24 #주의 A가 24시가 되면 0으로 바꿔야한다!!
    print(A, B)
    
elif((B+C) % 60 == 0): #주의 (B+C가 0일 때가 아닌, 60의 배수일 때여야한다.)
    A = A + ((B+C)//60) #주의 (B가 0이 되면서 (B+C)//60만큼 더 더해줘야한다.)
    B = 0 #주의 (이 라인이 A보다 먼저 실행되면 B가 0이 먼저 되버리므로 조심해야한다.)
    if(A >= 24):
        A = A - 24 #주의 A가 24시가 되면 0으로 바꿔야한다!!
    print(A, B)
    
# 주의할 점
# 60분이 되었을 때는, 0분으로 표현해야하는데, 깜박 잊을 뻔 했다!! 문제 꼼꼼히 읽자!
# 단순히 B+C가 60이 넘을때, A를 +1하면 안된다. +2일수도, 3일수도 있지 않느냐!
# 분을 다 뜯어봐야한다. -> A는 60으로나눈 몫만큼 더해줘야한고, B는 B+C한것에서 60으로 나눈 나머지이다.
# 딱60분이 될 때는, B가 0이 되면서 1을 더 더해줘야한다.