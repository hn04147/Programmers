def solution(board, moves):
    answer = 0
    pot = []
    for i in range(len(moves)):
        pos = moves[i] - 1
        for j in range(len(board)):
            if board[j][pos] != 0:
                pot.append(board[j][pos])
                board[j][pos] = 0
                if len(pot)>1 and pot[-1]==pot[-2]:
                    pot.pop(-1)
                    pot.pop(-1)
                    answer += 2
                break
    return answer
