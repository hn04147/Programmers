import math

def time_to_minutes(time):
    hour, minute = time.split(':')
    return int(hour) * 60 + int(minute)

def get_fee(fees, minutes):
    if minutes <= fees[0]:
        return fees[1]
    else:
        return fees[1] + math.ceil((minutes - fees[0]) / fees[2]) * fees[3]

def solution(fees, records):
    answer = []
    car_nums = []
    cars = {}
    fees_dict = {}
    
    for record in records:
        time, num, status = record.split(' ')
        if num not in cars:
            car_nums.append(num)
            cars[num] = [time_to_minutes(time)]
            fees_dict[num] = 0
        else:
            cars[num].append(time_to_minutes(time))
            
    for car in cars:
        if len(cars[car]) % 2 != 0:
            cars[car].append(time_to_minutes('23:59'))
            
    for car in cars:
        times = cars[car]
        accumulated_fee = 0
        for i in range(0, len(times), 2):
            accumulated_fee += (times[i+1] - times[i])
        fees_dict[car] = get_fee(fees, accumulated_fee)
        
    for car_num in sorted(car_nums):
        answer.append(fees_dict[car_num])
    
    return answer