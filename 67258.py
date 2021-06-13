def solution(gems):
    type = []
    answer = [1, len(gems)]
    for i in gems:
        if i not in type:
            type.append(i)
    
    len_gems = len(gems)
    len_type = len(type)
    for i in range(len_gems - len_type + 1):
        type_ = []
        idx = i
        start, end = 1, len(gems) 
        while (idx < len_gems):
            if gems[idx] not in type_:
                type_.append(gems[idx])
                if len(type_) == len_type:
                    start, end = i + 1, idx + 1
                    if (answer[1] - answer[0]) > (end - start):
                        answer = [start, end]
                    break
            idx += 1
        
    
    return answer
