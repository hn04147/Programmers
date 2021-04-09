def solution(heights):
    answer = []
    for i in range (len(heights)):
        j=i-1
        while True:
            if heights[j] > heights[i]:
                answer.append(j+1)
                break
            elif j == -1:
                answer.append(0)
                break
            j -= 1
    return answer

print(solution([6,9,5,7,4]))
print(solution([3,9,9,3,5,7,2]))
print(solution([1,5,3,6,7,6,5]))
