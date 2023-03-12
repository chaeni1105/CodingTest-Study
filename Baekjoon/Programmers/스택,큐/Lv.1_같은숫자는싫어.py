### [문제 분석]
# 목적 : 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하는 프로그램 작성
# -> 만약 뒤따라 오는 수가 앞의 수랑 다를 시, 뒤의 수를 추가!!

### [문제 풀이]
# 1단계 : 빈 answer리스트를 만들고, 그곳에 arr의 가장 첫번째 수를 넣는다!(index 0번)
# 2단계 : 만약 앞의 수와 뒤의 수가 같으면 그냥 넘어가고, 다를 시에는 뒤에 나오는 수를 answer리스트에 추가한다.
#         이때, for문을 사용하여 0부터 마지막인덱스보다 하나 적은 것까지 반복적으로 비교를 할 수 있게한다.

def solution(arr):
    # 1단계
    answer = []
    answer.append(arr[0])
    
    # 2단계
    for i in range(0, len(arr)-1):
        if(arr[i] == arr[i+1]):
            pass
        else:
            answer.append(arr[i+1])
            
    return answer