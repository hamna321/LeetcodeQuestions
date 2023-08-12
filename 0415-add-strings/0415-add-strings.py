class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)
        a = int(num1)
        b = int(num2)
        total = a + b
        s = str(total)
        return s