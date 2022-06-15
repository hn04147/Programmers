def solution(lottos, win_nums):
    def get_result(num):
        if 2 <= num:
            return 7 - num
        else:
            return 6
    
    num_zero = 0
    win = 0
    for lotto in lottos:
        if lotto == 0:
            num_zero += 1
        elif lotto in win_nums:
            win += 1
            
    answer = [get_result(win + num_zero), get_result(win)]
    
    return answer