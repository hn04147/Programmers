def numeral_system(number, base):
    NOTATION = '0123456789ABCDEF'
    q, r = divmod(number, base)
    n = NOTATION[r]
    return numeral_system(q, base) + n if q else n

def solution(n):
    num = int(str(numeral_system(n,3))[::-1], 3)
    '''answer = 0
    for idx, number in enumerate(num[::-1]):
        answer += int(number) * (3 ** idx)'''
    return num
