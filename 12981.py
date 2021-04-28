def solution(n, words):
    result = []
    result.append(words[0])
    idx = 1
    
    for i in range(idx, len(words)):
        if words[i][:1] == words[i-1][-1:]:
            #단어가 중복됬을때:
            if words[i] in result:
                return [i%n+1, i//n+1]
                break
            result.append(words[i])
        #단어를 잘못 말했을 때:
        elif words[i][:1] != words[i-1][-1:]:
            return [i%n+1, i//n+1]
            break
        #아무 이상 없을때:
        
    return [0, 0]
            
            
