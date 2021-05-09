'''num = [1, 2, 4]

def div(n):
    global num
    if n == 1:
        return '1'
    elif n == 2:
        return '2'
    elif n == 3:
        return '4'
    elif n > 3: 
        return str(div((n-1)//3)) + str(num[(n-1)%3])

def solution(n):
    return div(n)'''

def solution(n):
    answer = ''
    num = [1, 2, 4]
    while n>0:
        answer = str(num[(n-1)%3]) + answer
        n = (n-1)//3
    return answer
