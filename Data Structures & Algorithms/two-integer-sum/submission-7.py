class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:            
        reverse_idx = {} # hash map for index-value pair
        for a in range(len(nums)):
            reverse_idx[nums[a]] = a
        # loop thru the original list by index
        for i in range(len(nums)):
            # find the complement of the value in that index with the target
            diff = target - nums[i]
            # check if the complement is in the hash map and two indices are different
            if diff in reverse_idx and i != reverse_idx[diff]:
                # return the indices in a list
                return [i, reverse_idx[diff]]
