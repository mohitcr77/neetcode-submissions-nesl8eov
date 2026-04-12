class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [0] * len(gas) 
        add = 0
        for i in range(len(gas)):
            diff[i] = gas[i] - cost[i]
            add += diff[i]

        if add < 0:
            return -1


        print(diff)
        total = 0
        res = 0
        for i in range(len(diff)):
            # total = total + diff[i]
            # if total < 0:
            # j = i
            # total = total + diff[i]
            # print(total)
            # while total > 0 and j < len(gas)-1:
            #     j += 1
            #     total = total +diff[j]
            # if total > 0:
            #     return i
            # else:
            #     total = 0
            total += diff[i]

            if total <0:
                total = 0
                res = i+1


        return res

