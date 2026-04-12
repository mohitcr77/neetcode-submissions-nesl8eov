class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix)-1

        r,c = len(matrix)-1, len(matrix[0])-1
        mid = 0
        while t <= b :
            mid = (t + b) // 2

            if matrix[mid][0] > target:
                b = mid - 1

            elif matrix[mid][-1] < target:
                t = mid + 1

            else:
                break

        print(f"mid : {mid}")

        l,r = 0, c

        while l <= r:
            m= (l+r)//2
            print(f"m : {m}")
            if matrix[mid][m] > target:
                r = m -1

            elif matrix[mid][m] < target:
                l = m + 1

            elif matrix[mid][m] == target:
                return True



        return False



        



            