def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        result = str(bin(arr1[i] | arr2[i])[2:])
        answer_ = '' + ' ' * (n - len(result))
        for j in range(len(result)):
            answer_ += '#' if result[j] == '1' else ' '
        answer.append(answer_)
    return answer