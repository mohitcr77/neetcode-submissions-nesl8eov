class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # hand.sort()
        if len(hand) % groupSize != 0:
            return False

        freq = {}

        for i in hand:
            freq[i] = freq.get(i, 0) + 1
        print(freq)


        minHeap = list(freq.keys())

        heapq.heapify(minHeap)
        print(minHeap)
        while minHeap:
            i= minHeap[0]
            for j in range(i, i+groupSize):
                print(freq)
                print(f"j : {j}")
                if j not in freq:
                    return False
                
                freq[j] -= 1
                if freq[j] == 0:
                    if j != minHeap[0]:
                        return False
                    else:
                        heapq.heappop(minHeap)



        print(freq)
        return True

