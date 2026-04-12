class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        
        count1 = {}
        for char in s1:
            count1[char] = 1 + count1.get(char, 0)

        for r in range(len(s1), len(s2) + 1):
            c = s2[l:r]
            
            count2 = {}
            for char in c:
                count2[char] = 1 + count2.get(char, 0)
            
            if count1 == count2: 
                return True
            
            l += 1
            
        return False

        
