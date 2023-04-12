from collections import deque

def bfs(cx, cy, radius):
    visited = set() # 방문한 인공지능학부 학생들의 좌표를 저장할 set
    dx = [-1, 0, 1, 0] # 상하좌우
    dy = [0, 1, 0, -1]

    q = deque([(cx, cy)])
    cnt = 0 # 디저트를 받은 인공지능학부 학생 수

    def is_ai_student(x, y):
        sum_digits = sum(map(int, str(abs(x) + abs(y))))
        return sum_digits <= 16 and sum_digits % 2 == 0

    while q:
        x, y = q.popleft()
        if abs(x - cx) ** 2 + abs(y - cy) ** 2 > radius ** 2:
            continue # 주어진 영역을 벗어난 경우

        if is_ai_student(x, y) and (x, y) not in visited:
            visited.add((x, y))
            cnt += 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if abs(nx - cx) ** 2 + abs(ny - cy) ** 2 <= radius ** 2:
                if is_ai_student(nx, ny) and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((nx, ny))

    return cnt

cx, cy = map(int, input('중심 좌표 입력: ').split())
radius = int(input('원의 반지름 입력: '))
answer = bfs(cx, cy, radius)
print(f'디저트를 받은 인공지능학부 학생은 총 {answer}명입니다.')