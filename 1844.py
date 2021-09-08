from collections import deque

def solution(maps):
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
    visited = deque()
    visited.append([0, 0, 1])
    maps[0][0] = 0
    final_x, final_y = len(maps[0])-1, len(maps)-1
    
    while visited:
        y, x, cnt = visited.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == final_x and ny == final_y:
                return cnt+1
            elif 0 <= nx < len(maps[0]) and 0 <= ny < len(maps) and maps[ny][nx] == 1:
                visited.append([ny, nx, cnt+1])
                maps[ny][nx] = 0
    return -1

'''

def bfs(start, maps):
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    queue = deque()
    queue.append(start)
    while queue:
        y, x, cnt = queue.popleft()
        maps[y][x] = 0
        for dy, dx in dirs:
            ny, nx = y+dy, x+dx
            if ny == len(maps)-1 and nx == len(maps[0])-1:
                return cnt+1
            elif 0<=ny<len(maps) and 0<=nx<len(maps[0]) and maps[ny][nx]==1:
                maps[ny][nx] = 0
                queue.append((ny, nx, cnt+1))
    return -1

def solution(maps):
    return bfs((0, 0, 1), maps)
'''
