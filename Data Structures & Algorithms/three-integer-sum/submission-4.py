class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        output = []

        for start in range(len(nums)):

            if start > 0 and nums[start] == nums[start - 1]:
                continue

            left = start + 1
            right = len(nums) - 1

            while left < right:

                sum = nums[start] + nums[left] + nums[right]

                if sum == 0:
                    output.append([nums[start], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                
                elif sum < 0:
                    left += 1
                
                elif sum > 0:
                    right -= 1
            

        return output