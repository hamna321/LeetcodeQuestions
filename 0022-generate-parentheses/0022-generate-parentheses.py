class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        def recursion(openC,closeC):
            if(openC==closeC==n):
                res.append("".join(stack))
                return
                #the opening count is equal to closing count....
            if(openC<n):
                stack.append("(")
                recursion(openC+1,closeC)
                stack.pop()
                #firstly append the opening parenthesis  till it is less than the total available count of opening parenthesis...
            if(closeC<openC):
                stack.append(")")
                recursion(openC,closeC+1)
                stack.pop()
                #The moment where the opening parenthesis has been there then we should include an closing parenthesis for making the string balanced....
        recursion(0,0)
        return res