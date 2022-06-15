answer = [0, 0]

def quad(arr, a, b, l):
    global answer
    top_left = arr[a][b]
    for i in range(a, a+l):
        for j in range(b, b+l):
            if arr[i][j] != top_left:
                l = l//2
                quad(arr, a, b, l)
                quad(arr, a, b+l, l)
                quad(arr, a+l, b, l)
                quad(arr, a+l, b+l, l)
                return
    answer[top_left] += 1

def solution(arr):
    global answer
    quad(arr, 0, 0, len(arr))
    return answer
