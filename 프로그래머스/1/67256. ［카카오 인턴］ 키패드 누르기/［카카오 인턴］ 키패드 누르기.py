def solution(numbers, hand):
    keypad = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }
    
    left = '*'
    right = '#'
    result = []

    for num in numbers:
        if num in [1,4,7]:
            result.append('L')
            left = num

        elif num in [3,6,9]:
            result.append('R')
            right = num

        else:
            lx, ly = keypad[left]
            rx, ry = keypad[right]
            nx, ny = keypad[num]

            left_dist = abs(lx - nx) + abs(ly - ny)
            right_dist = abs(rx - nx) + abs(ry - ny)

            if left_dist < right_dist:
                result.append('L')
                left = num
            elif left_dist > right_dist:
                result.append('R')
                right = num
            else:
                if hand == 'right':
                    result.append('R')
                    right = num
                else:
                    result.append('L')
                    left = num

    return ''.join(result)