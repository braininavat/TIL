class Solution(object):
    def twoSum(self, nums, target):
        numsdict = {}
        
        for x in range(len(nums)):
            sub = target - nums[x]
            if sub in numsdict:
                return [x,numsdict[sub]]
            else:
                numsdict[nums[x]] = x        