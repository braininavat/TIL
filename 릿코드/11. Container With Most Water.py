class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        minHeight = min(height[left],height[right])
        maxArea = 0;
        
        while left < right:
            
            if height[left] >= minHeight and height[right] >= minHeight:
                maxArea = max(maxArea,(right-left)*minHeight) 
             
            if height[left] > height[right]:
                right = right-1
            elif height[right] > height[left]:
                left = left +1
            else:
                left = left+1
                right = right-1
            minHeight = min(height[left],height[right])
        return maxArea
                