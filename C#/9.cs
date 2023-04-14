public class Solution {
    public bool IsPalindrome(int x) {
        if(x < 0) {
            return false; // negative numbers are not palindromes
        }
        int reversed = 0;
        int original = x;
        while(x != 0) {
            int digit = x % 10;
            reversed = reversed * 10 + digit;
            x /= 10;
        }
        return reversed == original; // check if the reversed number is equal to the original number
    }
}