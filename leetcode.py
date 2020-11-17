class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        for val in len(nums)+1: 
            a = nums[val]
            b = val + 1
            for val in (b, len(nums)+1): 
                 