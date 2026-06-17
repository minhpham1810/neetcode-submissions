class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        freq_values = freq.values()
        for j in freq_values:
            if j != 1:
                return True

        return False
         