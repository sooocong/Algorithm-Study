from collections import deque

def solution(bridge_length, weight, truck_weights):
    second = 0
    
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    t = 0
    while t > 0 or truck_weights:
        second += 1
        
        out = bridge.popleft()
        t -= out
        
        if truck_weights and t + truck_weights[0] <= weight:
            x = truck_weights.popleft()
            bridge.append(x)
            t += x
            
        else:
            bridge.append(0)

    return second