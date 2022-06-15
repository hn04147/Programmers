def solution(n, computers):
    for c in computers:
        print(c)
    answer = 0
    connected = [0]*n
    stack = []
    
    for i in range(n):
        if connected[i] == 0:
            stack.append(i)
            while stack:
                idx = stack.pop()
                for j in range(n):
                    if idx != j and connected[j] == 0 and computers[idx][j] == 1:
                        stack.append(j)
                        connected[j] = 1
            answer += 1
                
    return answer
