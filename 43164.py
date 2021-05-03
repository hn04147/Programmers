import numpy as np
from collections import deque

def solution(tickets):
    answer = []
    tickets = np.array(tickets)
    queue = deque()
    queue.append("ICN")
    index = []
    length = len(tickets)
    answer.append("ICN")
    
    for i in range(length):
        index = []
        departure = queue.popleft()
        for j in range(len(tickets)):
            if tickets[j][0] == departure:
                index.append([tickets[j][1], j])
        index.sort()
        arrive = index[0][0]
        answer.append(arrive)
        queue.append(arrive)
        tickets = np.delete(tickets, index[0][1], axis=0)
    
    return answer

'''
def solution(tickets):
    res = []
    answer=[]
    def DFS(start,ticket_list,res):
        res.append(start)
        if len(ticket_list)==1:
            res.append(ticket_list[0][1])
            answer.append(res)
        else:
            for t in ticket_list:
                if start==t[0]:
                    copy_tList=ticket_list.copy()
                    copy_tList.remove(t)
                    DFS(t[1],copy_tList,res.copy())
    DFS('ICN',tickets,res)       
    return min(answer)
'''
