class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 1:
            return False
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for j in freq:
            if freq[j] > 1:
                return True
        return False
    
        