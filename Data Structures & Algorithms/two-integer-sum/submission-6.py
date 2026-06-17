class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:            
        reverse_idx = {}
        for a in range(len(nums)):
            reverse_idx[nums[a]] = a
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in reverse_idx and i != reverse_idx[diff]:
                return [i, reverse_idx[diff]]
