class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        u = set()

        l = 0
        maxSeq = 0

        for r in range(len(s)):
            while s[r] in u:
                u.remove(s[l])
                l += 1
            u.add(s[r])
            maxSeq = max(maxSeq, r - l + 1)


        
        return maxSeq



                

