public class Solution {
    public int RomanToInt(string s) {
        int result = 0;
        for (int i = 0; i < s.Length; i++) {
            if (i < s.Length - 1 && GetValue(s[i]) < GetValue(s[i+1])) {
                result -= GetValue(s[i]);
            } else {
                result += GetValue(s[i]);
            }
        }
        return result;
    }
    
    private int GetValue(char c) {
        switch (c) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: return 0;
        }
    }
}