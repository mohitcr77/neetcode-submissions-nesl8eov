class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        
        for r in range(len(s1),len(s2)+1):
            print(f"l,r : {l,r}")
            c = s2[l:r]
            print(f"c : {c}")
            print(sorted(s1) == sorted(c))
            if sorted(s1) == sorted(c):
                return True

            l += 1
            
            

        return False

        
