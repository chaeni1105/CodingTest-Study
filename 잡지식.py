# sys.stdin.readlines()는 ^z 혹은 컨트롤+z를 누르기 전까지 계속 입력을 받을 수 있다.
# sys.stdin.readline()은 한 줄씩 입력을 받는다. 

# + readline()과 readlines()로 받았을 때는 \n 값이 포함되므로
# ex. ['문자\n','문자2\n']
# strip()을 써서 공백을 제거해야 한다.