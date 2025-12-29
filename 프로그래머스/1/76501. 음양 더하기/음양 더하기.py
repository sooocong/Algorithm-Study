def solution(absolutes, signs):
    absolutes_sum = 0
    
    for i in range(len(signs)):
        if signs[i]:
            absolutes_sum += absolutes[i]
        else:
            absolutes_sum -= absolutes[i]

    return absolutes_sum