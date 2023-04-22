class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:  
        nums = sorted(nums)
        output = []

        for i in range(len(nums)-2):
            if nums[i] > 0 : break
            newnums = nums[i+1:]
            leftidx = 0
            offset = nums[i]
            rightidx = len(newnums)-1
        
            while leftidx < rightidx:
                if offset+newnums[leftidx] > -1*newnums[rightidx]:
                    rightidx = rightidx-1
                elif offset+newnums[leftidx] < -1*newnums[rightidx]:
                    leftidx = leftidx + 1
                else:
                    if [offset,newnums[leftidx],newnums[rightidx]] not in output:
                        output.append([offset,newnums[leftidx],newnums[rightidx]])
                    rightidx = rightidx -1
                    leftidx - leftidx + 1    
        
        return output
