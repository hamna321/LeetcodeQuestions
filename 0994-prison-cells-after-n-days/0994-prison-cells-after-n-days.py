class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}
        is_cycle_found = False

        while n > 0:
            if not is_cycle_found:
                state_tuple = tuple(cells)
                if state_tuple in seen:
                    n %= seen[state_tuple] - n
                    is_cycle_found = True
                else:
                    seen[state_tuple] = n

            if n > 0:
                new_cells = [0] * len(cells)
                for i in range(1, len(cells) - 1):
                    new_cells[i] = 1 if cells[i - 1] == cells[i + 1] else 0
                cells = new_cells
                n -= 1

        return cells
