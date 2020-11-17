n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#DFS로 특정 노드를 방문한 뒤 연결된 모든 노드 방문
def dfs(x,y):
    if x<= -1 or x>=n or y<= -1 or y>=m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        print(x,y)
        return True
    return False

#모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
print(result)
