def solution(numbers, hand):
    answer = ''
    hand = hand
    coordinates = {1:[0, 0], 2:[1, 0], 3:[2, 0],
                   4:[0, 1], 5:[1, 1], 6:[2, 1],
                   7:[0, 2], 8:[1, 2], 9:[2, 2],
                             0:[1, 3]}
    left_loc = [0, 3]
    right_loc = [2, 3]
    for i in range(len(numbers)):
        if numbers[i] in [1, 4, 7]:
            answer += 'L'
            left_loc = coordinates[numbers[i]]
        elif numbers[i] in [3, 6, 9]:
            answer += 'R'
            right_loc = coordinates[numbers[i]]
        else:
            left_dist = abs(left_loc[0] - coordinates[numbers[i]][0]) + abs(left_loc[1] - coordinates[numbers[i]][1])
            right_dist = abs(right_loc[0] - coordinates[numbers[i]][0]) + abs(right_loc[1] - coordinates[numbers[i]][1])
            if left_dist < right_dist:
                answer += 'L'
                left_loc = coordinates[numbers[i]]
            elif left_dist > right_dist:
                answer += 'R'
                right_loc = coordinates[numbers[i]]
            else:
                if hand == "left":
                    answer += 'L'
                    left_loc = coordinates[numbers[i]]
                else:
                    answer += 'R'
                    right_loc = coordinates[numbers[i]]
    return answer
