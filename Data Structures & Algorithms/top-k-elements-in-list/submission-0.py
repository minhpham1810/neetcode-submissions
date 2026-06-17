class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initialize a hash map to store values and their frequencies
        freq = {}
        for i in nums: 
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        # rank the hashmap values based on their values
        freq = sorted(freq.items(),key=lambda item: item[1], reverse=True ) # this will store key-value pair as tuples
        res= [] #result list
        count = 0 #counter to stop when k elements have been added to result list
        while count < k:
            res.append(freq.pop(0)[0]) #pop the 1st (most appearances) element from the list, and take its key
            count += 1 #increment counter
        return res