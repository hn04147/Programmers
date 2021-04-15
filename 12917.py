def solution(s):
    s = sorted(s, reverse = True)
    answer = ''
    for c in s:
        answer += c
    return answer
