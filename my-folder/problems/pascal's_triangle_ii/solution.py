class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prev = [1]
        for rows in range(1,rowIndex+1):
            curr = [1]*(rows+1)
            if rows>=2:
                for i in range(1,rows):
                    curr[i] = prev[i-1] + prev[i]
            prev = curr
        return prev
        