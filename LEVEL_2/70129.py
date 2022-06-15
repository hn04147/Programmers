def solution(s):
    answer = [0, 0]
    num = ''
    while s != '1':
        answer[0] += 1 
        for c in s:
            if c == '1':
                num += c
            elif c == '0':
                answer[1] += 1
        s = bin(len(num))[2:]
        num = ''
    return answer
