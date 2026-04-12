class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dictA = {}
        res = 0
        l = 0
        
        for r in range(len(s)):
            dictA[s[r]] = 1 + dictA.get(s[r], 0)

            while (r-l+1) - max(dictA.values()) > k:
                dictA[s[l]] -= 1
                l+=1

            res = max(res, r-l+1)
            
        return res
