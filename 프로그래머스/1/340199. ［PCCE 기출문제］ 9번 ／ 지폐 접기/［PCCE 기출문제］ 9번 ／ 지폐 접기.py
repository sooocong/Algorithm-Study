def solution(wallet, bill):
    answer = 0
    
    while 1:
        bill.sort()
        wallet.sort()
        
        if wallet[0] >= bill[0] and wallet[1] >= bill[1]:
            return answer
        else:
            bill[1] //= 2
            answer += 1