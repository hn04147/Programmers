# 참고 https://kimjingo.tistory.com/155

def solution(board, skill):
    answer = 0
    height, width = len(board), len(board[0])
    imos = [[0 for _ in range(width+1)] for _ in range(height+1)]
    
    for skill_type, r1, c1, r2, c2, degree in skill:
        skill_type = 1 if skill_type == 2 else -1
        imos[r1][c1] += (skill_type * degree)
        imos[r1][c2+1] += (skill_type * degree * -1)
        imos[r2+1][c1] += (skill_type * degree * -1)
        imos[r2+1][c2+1] += (skill_type * degree)
        
    for i in range(height):
        for j in range(width):
            imos[i][j] = imos[i][j] if j == 0 else imos[i][j] + imos[i][j-1]
            
    for i in range(height):
        for j in range(width):
            imos[i][j] = imos[i][j] if i == 0 else imos[i][j] + imos[i-1][j]
        
    for i in range(height):
        for j in range(width):
            board[i][j] = board[i][j] + imos[i][j]
            answer = answer + 1 if board[i][j] > 0 else answer
    
    return answer