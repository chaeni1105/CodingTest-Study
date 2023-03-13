### [문제 분석]
# 목적 : 
# -> 

### [문제 풀이]
# 1단계 : 
# 2단계 : 
# 3단계 :

def solution(n, lost, reserve):
    answer = 0
    answer = answer + n - len(lost)
    
    for i in range(0, len(reserve)):
            if((reserve[i] - 1) in lost):
                answer += 1
                lost.remove((reserve[i] - 1))

            elif((reserve[i] + 1) in lost):
                answer += 1
                lost.remove((reserve[i] + 1))

            else:
                pass
            
    return answer