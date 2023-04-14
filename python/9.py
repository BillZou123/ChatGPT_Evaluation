class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            num = x
            reverse = 0
            while num != 0:
                reverse = reverse * 10 + num % 10
                num = num // 10
            if x == reverse:
                return True
            else:
                return False