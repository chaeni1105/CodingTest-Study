### [문제 분석]
# 목적 : 체육수업을 들을 수 있는 학생의 최댓값 구하는 프로그램 작성
# -> 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 
#    그리디 알고리즘을 사용하여 왼쪽부터 체육복을 빌려주게한다.

### [문제 풀이]
# 1단계 : 일단 reverse배열과 lost배열에서의 중복을 제거한다.(reverse의 값을 remove한다.)
# 2단계 : 리벌스값-1 한것과 lost값이 같을 시, lost값에서 제거한다. 리벌스값+1 한것도 역시 lost값과 같을 시, lost값에서 제거한다.
# 3단계 : 전체 갯수에서 아직도 빌리지 못한 학생 수를 빼서 총 체육복이 있는 학생들 수를 구한다.

def solution(n, lost, reserve):
    answer = 0
    
    # 1단계
    #여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있기 때문에, reserve와 lost값은 중복이 되면 안된다.
    for i in range(len(reserve)):
        if (reserve[i] in lost): #reserve[i]값이 lost리스트 안에 몇개나 있는지 확인(1이상이면 True 0이면 False)
            reserve.remove(reserve[i])
            lost.remove(reserve[i])
    # new_lost = set(lost) - set(reserve)
    # new_reserve = set(reserve) - set(lost)
    
    # 질문 1 : 굳이 new_lost에 저장해야하는 이유는???
    # 질문 2 : set이랑 똑같이 동작하는 반복문 코드는 없을까?
        
    #reserve리스트에서 1부터 5까지 오름차순 순서대로 체육복 없는 사람에게 빌려준다고 하면,
    #오른쪽보다 왼쪽 학생부터 빌려주어야한다!!! 오른쪽학생부터 빌려준다면, 
    #2, 4번학생이 없고 3, 5번 학생이 체육복을 빌려줄 수 있다고 하면..  오른쪽부터 빌려줬을 때 2번
    #학생이 못받습니다. 따라서 reverse 요소를 기준으로왼쪽에 있는 값을 먼저 빌려주어야합니다.
    
    # 2단계
    for i in reserve:
        if(i-1 in lost): #왼쪽 값이 lost에 있으면, lost에서 제거
            lost.remove(i-1)
        elif(i+1 in lost): #오른쪽 값이 lost에 있으면, lost에서 제거
            lost.remove(i+1)
       
    # 3단계 
    answer = n - len(lost)
        
    return answer

# 주의할 점
# 1. 중복되는 번호는 없다.
# -> lost != [1,1,2] / reserve != [3,3,5,4,2] 1,1이 중복될 수 없고 3,3이 중복될 수 없다.
# 2. 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있다. (남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없다.)
# -> lost = [1,2,3] / reserve = [3,4,5] lost값과 reserve값에 공통으로 존재하는 수가 있다.


# 깨달은 점
# 1. 알고리즘에 대한 지식이나 이를 다룰 줄 아는 기술도 중요하지만, 정작 문제를 제대로 이해하지 못하면 풀지 못한다.