from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    now_weight = 0  #현재 다리위에 있는 트럭 총 무게
    truck_weights = deque(truck_weights)
    cross_river = deque()  #다리를 건너는 트럭
    time = deque()  #다리를 건너는 트럭 상황
    while True:
        if  len(truck_weights)!=0:
            if (now_weight + truck_weights[0]) <= weight:
                index = truck_weights.popleft()
                now_weight = now_weight + index
                cross_river.append(index)
                time.append(bridge_length)
        for index in range (0, len(time)):
            time.append(time.popleft()-1)
        answer += 1
        if time[0]==0:
            time.popleft()
            now_weight = now_weight - cross_river.popleft()
        if len(truck_weights) == 0 and len(cross_river) == 0:
             break
    return answer

print (solution(2, 10, [7, 4, 5, 6]))
print (solution(100, 100, [10]))
print (solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))