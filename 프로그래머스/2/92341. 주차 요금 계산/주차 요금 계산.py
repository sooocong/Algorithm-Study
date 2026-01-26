import math

def solution(fees, records):
    record = []
    in_car = {}
    total_car = {}

    
    for i in range(len(records)):
        record.append(records[i].split(' '))
        record[i][0] = int(record[i][0][0:2]) * 60 + int(record[i][0][3:5])

    for re in record:
        if re[1] not in in_car and re[2] == 'IN':
            in_car[re[1]] = re[0]
        elif re[1] in in_car and re[2] == 'OUT':
            if re[1] not in total_car:
                total_car[re[1]] = re[0] - in_car[re[1]]
            else:
                total_car[re[1]] += re[0] - in_car[re[1]]
            in_car.pop(re[1])
    
    for i, v in in_car.items():
        if i not in total_car:
            total_car[i] = 1439 - v
        else:
            total_car[i] += 1439 - v
            
    answer = []
    for car, time in sorted(total_car.items()):
        fee = fees[1]
        if time > fees[0]:
            fee += math.ceil((time - fees[0]) / fees[2]) * fees[3]
            
        answer.append(fee)
    
    
    return (answer)