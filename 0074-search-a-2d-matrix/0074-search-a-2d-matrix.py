class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        if target > matrix[-1][-1]: return False    # <-- #3

        r = matrix[bisect_left(matrix, 
                  target, key = lambda x: x[-1])]   # <-- #1   row = r and i = index

        i = bisect_left(r, target)              # <-- #2

        return r[i] == target