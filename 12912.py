def sum(a, b):
    answer = 0
    for i in range(a, b+1):
        answer += i
    return answer

def solution(a, b):
    answer = 0
    if a == b:
        answer = a
    elif a > b:
        answer = sum(b, a)
    else:
        answer = sum(a, b)
    return answer
