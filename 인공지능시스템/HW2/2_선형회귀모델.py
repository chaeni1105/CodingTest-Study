

f = open("linear_regression.txt",'r') # linear_regression.txt 파일을 읽기 전용으로 open
lines = f.readlines() # 모든 라인의 데이터를 load

for line in lines:
    line_data = line.split(' ') # split 명령어 안에 있는 string 데이터로 데이터를 나누어 리스트형태로 변환하는 함수
        # (‘ ’)은 공백을 기준으로 데이터를 나눔
    print(line_data)
    
f.close()