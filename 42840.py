def solution(answers):
    guess = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    answer = []
    correct = [0, 0, 0]
    for i in range(3):
        num = 0
        for j in range(len(answers)):
            if answers[j] == guess[i][(j+1)%(len(guess[i]))-1]:
                num += 1
        correct[i] = num
    if correct[0] > correct[1] and correct[0] > correct[2]: answer = [1] 
    if correct[1] > correct[0] and correct[1] > correct[2]: answer = [2] 
    if correct[2] > correct[0] and correct[2] > correct[1]: answer = [3] 
    if correct[0] == correct[1] and correct[0] > correct[2]: answer = [1, 2] 
    if correct[0] == correct[2] and correct[0] > correct[1]: answer = [1, 3] 
    if correct[1] == correct[2] and correct[1] > correct[0]: answer = [2, 3] 
    if correct[0] == correct[1] and correct[1] == correct[2]: answer = [1, 2, 3] 
    return answer
