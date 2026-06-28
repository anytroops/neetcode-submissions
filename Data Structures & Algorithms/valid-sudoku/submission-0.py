class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        sol  = {} 
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.': 
                    continue
                if val in rows[i]:
                    return False
                rows[i].add(val)
                if val in cols[j]:
                    return False
                cols[j].add(val)

                key = (i//3, j//3)
                if key not in sol:
                    sol[key] = set()
                if val in sol[key]:
                    return False
                sol[key].add(val)
        return True

        