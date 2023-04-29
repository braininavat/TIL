class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = ""
        idx = 0
        for num in nums:
            if(num != cur):
                nums[idx] = num
                cur = num
                idx += 1

        return idx