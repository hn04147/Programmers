def solution(arr, divisor):
    answer = []
    for c in arr:
        if c % divisor == 0:
            answer.append(c)
    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()
    return answer
