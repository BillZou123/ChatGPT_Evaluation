class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            res = int(str(x)[::-1])
        else:
            res = -1 * int(str(abs(x))[::-1])
            
        if res > 2**31 - 1 or res < -2**31:
            return 0
        else:
            return res