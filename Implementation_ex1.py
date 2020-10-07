# [ 상하좌우 ]
# N x N 크기의 정사각형 공간, 가장 왼쪽 위 좌표 = (1,1), 가장 오른쪽 아래 좌표 = (N,N)
# 상,하,좌,우 방향으로 이동 가능, 시작 좌표는 (1,1)
# 첫 줄에 띄어쓰기 기준으로 L,R,U,D 중 하나의 문자가 반복적으로 입력
# L : 왼쪽, R : 오른쪽, U : 위, D : 아래
# N X N 크기의 공간을 벗어나는 움직임은 무시

n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D
dx = [ 0, 0, -1, 1 ]
dy = [ -1, 1, 0, 0 ]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print( x, y )