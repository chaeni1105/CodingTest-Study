### [문제 분석]
# 목적 : 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램 작성
# -> N개의 정수 중에 v가 몇 개인지 출력힌디.

### [문제 풀이]
# 1단계 : 첫째 줄에 N개의 정수, 둘째 줄에 공백으로 구분되어져있는 정수들, 셋째 줄에는 찾으려고 하는 정수 v를 입력받는다.
# 2단계 : nums의 길이만큼 반복문을 돌린다. 반복문 안에서는 v정수랑 같은 정수가 nums안에 있는지 찾고, 만약 있다면 count 1을 한다.

import sys
input = sys.stdin.readline

# 1단계
N = int(input())
nums = list(map(int, input().split()))
v = int(input())
cnt = 0

# 2단계
for i in range(0, len(nums)):
    if(nums[i] == v):
        cnt += 1
        
print(cnt)
