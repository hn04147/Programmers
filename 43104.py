def solution(N):
    if N==1: return 4
    if N==2: return 6
    if N==3: return 10
    if N>=4:
        list=[1,1]
        for i in range (2,N):
            list.append(list[i-2]+list[i-1])
        return (list[N-1]*3 + list[N-2]*2 + list[N-3]*2 + list[N-4])
    
print(solution(5))
print(solution(6))
print(solution(7))