def solution(array, commands):
    answer = [0] * len(commands)
    i = 0
    for c in commands:
        arrayCut = array[c[0]-1: c[1]]
        arrayCut.sort()
        answer[i] = arrayCut[c[2]-1]
        i += 1
    return answer
