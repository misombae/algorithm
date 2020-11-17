from collections import deque

#미로탈출
#N*M 직사각형 형태의 미로에서 0은 이동불가, 1은 이동가능
#미로의 출구는(N,M)위치에 있다.

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4): #상하좌우
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 # 방문한 경우 1에서 바꿔 준다.
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(dfs(0,0))

