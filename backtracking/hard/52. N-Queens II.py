class Solution:
    def totalNQueens(self, n: int) -> int:
        sol = 0
        col = set()
        posDiag = set()
        negDiag = set()

        def backtrack(r):
            nonlocal sol
            if r == n: 
                sol += 1
                return
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)

                backtrack(r+1)
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
        backtrack(0)
        return sol