def solution(sizes):
    height, width, size = 0, 0, 0
    is_first = True
    for i in sizes:
        if is_first:
            height = i[0] if i[0] < i[1] else i[1]
            width = i[1] if i[0] < i[1] else i[0]
            is_first = False
        else:
            height_ = i[0] if i[0] < i[1] else i[1]
            width_ = i[1] if i[0] < i[1] else i[0]
            height = height_ if height_ > height else height
            width = width_ if width_ > width else width
            
    answer = height * width
    return answer