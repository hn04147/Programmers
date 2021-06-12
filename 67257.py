import re
from collections import deque

def cal(nums_, ops_, order):
    ops = deque(ops_)
    nums = deque(nums_)
    new_ops = deque([])
    new_nums = deque([])
    for i in range(len(order)):
        new_nums.append(nums.popleft())
        for j in range(len(ops)):
            operation = ops.popleft()
            if operation == order[i]:
                if operation == '+':
                    new_nums.append(int(new_nums.pop()) + int(nums.popleft()))
                elif operation == '-':
                    new_nums.append(int(new_nums.pop()) - int(nums.popleft()))
                else:
                    new_nums.append(int(new_nums.pop()) * int(nums.popleft()))
            else:
                new_ops.append(operation)
                new_nums.append(nums.popleft())
        nums = new_nums.copy()
        ops = new_ops.copy()
        new_nums.clear()
        new_ops.clear()
    return abs(int(nums.pop()))
        
        
def solution(expression):
    ops = re.findall('[-+*]', expression)
    nums = re.split('[-+*]', expression)
    result = [cal(nums, ops, ['*', '+', '-']),
              cal(nums, ops, ['*', '-', '+']),
              cal(nums, ops, ['+', '*', '-']),
              cal(nums, ops, ['+', '-', '*']),
              cal(nums, ops, ['-', '*', '+']),
              cal(nums, ops, ['-', '+', '*'])]
    answer = max(result)
    return answer
