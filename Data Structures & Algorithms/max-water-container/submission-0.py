class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area = -999999999

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                
                width = j - i
                height = min(heights[i], heights[j])
                area = width * height

                max_area = max(area, max_area)
        
        return max_area