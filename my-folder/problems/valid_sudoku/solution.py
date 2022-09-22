class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashrow = collections.defaultdict(set)
        hashcol =collections.defaultdict(set)
        hashsq =collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] !=".":
                    if board[r][c] in hashrow[r] or board[r][c] in hashcol[c] or board[r][c] in hashsq[(r//3,c//3)]:
                        return False
                    else:
                        hashrow[r].add(board[r][c])
                        hashcol[c].add(board[r][c])
                        hashsq[(r//3,c//3)].add(board[r][c])
        # print(hashsq)
        return True
        