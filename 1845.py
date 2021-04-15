def solution(nums):
    nums.sort()
    answer = []
    for i in range(len(nums)):
        if nums[i] not in answer:
            answer.append(nums[i])
    if len(answer)>=len(nums)/2:
        return len(nums)/2
    else:
        return len(answer)
