from collections import deque

def solution(numbers, target):
    size = len(numbers)
    answer = 0
    queue = deque()
    queue.append(0)
    for i in range(size):
        idx = deque()
        while queue:
            num = queue.popleft()
            idx.append(num+numbers[i])
            idx.append(num-numbers[i])
        queue = idx
    for c in queue:
        if c == target:
            answer += 1
    return answer
