def print_array(arr):
    for c in arr:
        print(c)

def solution(rows, columns, queries):
    answer = []
    num_plus = 1
    arr = [[0]*columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = num_plus
            num_plus += 1
    
    for c in queries:
        #배열 돌리기
        x1, y1, x2, y2 = c[0]-1, c[1]-1, c[2]-1, c[3]-1
        idx = arr[x1][y2]
        for y in range(y2, y1, -1):
            arr[x1][y] = arr[x1][y-1]
        for x in range(x1, x2):
            arr[x][y1] = arr[x+1][y1]
        for y in range(y1, y2):
            arr[x2][y] = arr[x2][y+1]
        for x in range(x2, x1, -1):
            arr[x][y2] = arr[x-1][y2]
        arr[x1+1][y2] = idx
        
        #최솟값 찾기
        min = 10000
        for y in range(y2, y1, -1):
            if arr[x1][y] < min:
                min = arr[x1][y]
        for x in range(x1, x2):
            if arr[x][y1] < min: 
                min = arr[x][y1]
        for y in range(y1, y2):
            if arr[x2][y] < min: 
                min = arr[x2][y]
        for x in range(x2, x1, -1):
            if arr[x][y2] < min: 
                min = arr[x][y2]
        answer.append(min)
        
    return answer
