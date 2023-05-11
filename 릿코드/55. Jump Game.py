class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #1. 0이 나오는 구간을 찾는다
        #2. 없으면 True
        #3. 있으면 전에서 index 와 jump 를 더한값보다 큰게 있는지 확인
        cur = 0
        start = 0
        end = 0
        high = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                end = i
                for j in range(start,end):
                    idx = j+nums[j]
                    high = max(idx,high)
                if high <= i:
                    if i != len(nums)-1: 
                        return False
                else:
                    start = i
        
        return True
