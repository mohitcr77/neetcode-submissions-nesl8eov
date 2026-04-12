class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""


        dictT, dictW = {}, {}

        for c in t:
            dictT[c] = 1 + dictT.get(c, 0)

        have, need = 0, len(dictT)
        res, resLen = [-1, -1], float("infinity")
        l=0

        for r in range(len(s)):
            c = s[r]

            dictW[c] = 1 + dictW.get(c, 0)

            if c in dictT and dictW[c] == dictT[c]:
                have += 1

            while have == need :
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1


                dictW[s[l]] -= 1
                if s[l] in dictT and dictW[s[l]] < dictT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r+1] if resLen != float("infinity") else ""

