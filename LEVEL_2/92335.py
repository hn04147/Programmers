import math

def numeral_system(number, base):
    NOTATION = '0123456789ABCDEF'
    q, r = divmod(number, base)
    n = NOTATION[r]
    return numeral_system(q, base) + n if q else n

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    converted = str(numeral_system(n, k)).split('0')
    for num in converted:
        if num != '':
            if is_prime_number(int(num)):
                answer += 1
    return answer