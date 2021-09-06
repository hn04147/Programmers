def solution(info, query):
    infos, conditions, answer = [], [], []
    for i in range(len(info)):
        infos.append(info[i].split())
    for i in range(len(query)):
        idx = query[i].split()
        index = []
        for j in idx:
            if j != 'and':
                index.append(j)
        conditions.append(index)
        # index = []
        # index.append(idx[0])
        # index.append(idx[2])
        # index.append(idx[4])
        # index.append(idx[6])
        # index.append(idx[7])
        # conditions.append(index)
    
    for i in conditions:
        result = 0
        for j in infos:
            if (i[0] == j[0] or i[0] == '-') and (i[1] == j[1] or i[1] == '-') and (i[2] == j[2] or i[2] == '-') and (i[3] == j[3] or i[3] == '-') and (int(i[4]) <= int(j[4])):
                result = result + 1
        answer.append(result)
    
    return answer