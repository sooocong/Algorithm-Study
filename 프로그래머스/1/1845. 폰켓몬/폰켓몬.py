def solution(nums):
    pick = len(nums) // 2 # 뽑을 폰켓몬 수
    cnt = len(set(nums))
    
    answer = min(pick, cnt)

    return answer