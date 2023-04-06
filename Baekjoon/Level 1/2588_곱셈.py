### [문제 분석]
# 목적 : (세 자리 수) × (세 자리 수) 곱셈 과정을 코드로 나타내 보는 문제
# -> 세자리 수를 곱할 때 나타나는 값 3개를 더해서 최종 값까지 총 4개를 구하기.

### [문제 풀이]
# 1단계 : 곱할 두 수 A와 B를 입력받는다.
# 2단계 : B의 1의자리, 10의자리, 100의자리를 A랑 각각 곱한 값을 구한다.
# 3단계 : 곱한 값들을 전부 더해 최종값을 구한다.
# 4단계 : 4개의 값들을 전부 출력한다.

# 1단계
A = int(input())
B = int(input())

# 2단계
num1 = A * (B%10)
num2 = A * ((B//10)%10)
num3 = A * (B//100)

# 3단계
num4 = num1 + 10*num2 + 100*num3

# 4단계
print(num1)
print(num2)
print(num3)
print(num4)


# # 1단계
# A = int(input())
# B = input()

# # 2단계
# num1 = A * int(B[2])
# num2 = A * int(B[1])
# num3 = A * int(B[0])

# # 3단계
# num4 = num1 + 10*num2 + 100*num3

# # 4단계
# print(num1)
# print(num2)
# print(num3)
# print(num4)