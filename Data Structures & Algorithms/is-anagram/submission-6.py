class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == '' and t == '':
            return True
        freq_s = {}
        freq_t = {}
        for i in s:
            if i in freq_s:
                freq_s[i] += 1
            else:
                freq_s[i] = 1
        for j in t:
            if j in freq_t:
                freq_t[j] += 1
            else:
                freq_t[j] = 1 
        return True if freq_s == freq_t else False    
        