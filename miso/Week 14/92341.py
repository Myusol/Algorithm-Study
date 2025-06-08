from collections import defaultdict
import math

def solution(fees, records):
    default_time = fees[0]
    default_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]
    
    parking = defaultdict(int)
    state = defaultdict(int)
    
    for i in range(len(records)):
        t, n, s = records[i].split()
        h, m = t.split(':')
        t = int(h) * 60 + int(m)
        
        if s == 'IN':
            state[n] = t
                
        if s == 'OUT':
            parking[n] += t - state[n]
            del state[n]

    answer = []
    for car, io in state.items():
        t = 23 * 60 + 59 - io
        state[car] = 0
        parking[car] += t
            
    parking = sorted(parking.items())
    for num, time in parking:
        if time <= default_time:
            answer.append(default_fee)
        else:
            cal = (time - default_time) / unit_time
            m = default_fee + math.ceil(cal) * unit_fee
            answer.append(m)
            
    return answer