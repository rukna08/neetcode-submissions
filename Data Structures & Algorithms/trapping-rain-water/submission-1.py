class Solution:
    def trap(self, height: List[int]) -> int:

        # pre-computer left max
        left_max_precompute = [0] * len(height)
        left_max_precompute[0] = 0
        for i in range(1, len(height)):
            left_max_precompute[i] = max(left_max_precompute[i-1], height[i-1])
        
        # pre-compute right max
        right_max_precompute = [0] * len(height)
        right_max_precompute[len(height)-1] = 0
        # loop right to left
        for i in range(len(height)-2, -1, -1):
            right_max_precompute[i] = max(right_max_precompute[i+1], height[i+1])

        total_water = 0

        # for each bar
        for i in range(len(height)):
            total_water += max(0, min(left_max_precompute[i], right_max_precompute[i]) - height[i])
        
        return total_water