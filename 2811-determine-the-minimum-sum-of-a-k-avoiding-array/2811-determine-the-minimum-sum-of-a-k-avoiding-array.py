class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        minimum_array = []
        num = 1

        while len(minimum_array) < n:  # Ensure the array has exactly 'n' numbers
            # Check if 'num' is valid: no number in minimum_array + num equals k
            if all(num + x != k for x in minimum_array):
                minimum_array.append(num)
            num += 1  # Increment to check the next number

        result = sum(minimum_array)
        return result
