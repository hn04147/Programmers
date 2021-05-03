from collections import deque

# 두 단어중 다른 알파벳 개수 return
def diff(front, end):
    difference = 0
    if len(front) == len(end):
        for i in range(len(front)):
            if front[i] != end[i]:
                difference += 1
    return difference

def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append(begin)
    
    for _ in range(len(words)):
        for _ in range(len(queue)):
            word = queue.popleft()
            for c in words:
                if diff(word, c) == 1:
                    queue.append(c)
                    if c == target:
                        answer += 1
                        return answer
        answer += 1           
                    
    return 0
