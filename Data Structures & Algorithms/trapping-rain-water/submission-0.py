class Solution:
    def trap(self, height: List[int]) -> int:

        total_water = 0

        # for each bar
        for i in range(len(height)):
            max_left = 0
            max_right = 0

            # we deploy a left finder from beginning to
            # left block of the ith block.
            for left_finder in range(0, i):
                max_left = max(max_left, height[left_finder])
            
            # we deploy a right finder from right block of
            # the ith block to the ending block.
            for right_finder in range(i+1, len(height)):
                max_right = max(max_right, height[right_finder])

            # use the formula for finding water on top
            # of the ith block.
            total_water += max(0, min(max_left, max_right) - height[i])
        
        return total_water