class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        a = len(operations)
        x = 0
        for i in range(a):
            if operations[i] == "--X":
                x=x-1
            elif operations[i] == "X--":
                x=x-1
            elif operations[i] == "X++":
                x=x+1
            else:
                x=x+1 
        return x