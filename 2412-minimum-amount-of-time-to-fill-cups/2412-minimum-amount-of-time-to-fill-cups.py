class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort(reverse=True)
        # If the biggest cup amount is bigger than sum of the other two, answer is biggest cup
        # Else answer is half of total rounded up
        if amount[0] >= amount[1] + amount[2]:
            return amount[0]
        else:
            return (sum(amount) + 1) // 2
