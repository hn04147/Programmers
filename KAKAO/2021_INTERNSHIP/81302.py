from collections import deque

def solution(places):
    answer = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    for place in places:
        flag = False
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    q = deque([])
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0 <= nx < 5 and 0 <= ny < 5:
                            if place[nx][ny] == 'P':
                                flag = True
                                break
                            if place[nx][ny] == 'O':
                                q.append([nx, ny])
                    if flag == True:
                        break
                    for k in range(len(q)):
                        x, y = q.popleft()
                        for l in range(4):
                            nx = x + dx[l]
                            ny = y + dy[l]
                            if 0 <= nx < 5 and 0 <= ny < 5:
                                if nx != i and ny != j and place[nx][ny] == 'P':
                                    flag = True
                                    break
                if flag == True:
                    break
            if flag == True:
                break
        answer.append(0 if flag == True else 1)
                
    return answer