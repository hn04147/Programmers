def solution(n):
    answer = [0, 1, 2]
    if n <= 2:
        return answer[n]
    else:
        for i in range(3, n + 1):
            answer.append((answer[i - 1] + answer[i - 2]) % 1000000007)
    return answer[-1]