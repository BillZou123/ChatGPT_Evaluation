public class Solution {
    public bool IsMatch(string s, string p) {
        int sIndex = 0, pIndex = 0, sStarIndex = -1, pStarIndex = -1;
        while (sIndex < s.Length) {
            if (pIndex < p.Length && (s[sIndex] == p[pIndex] || p[pIndex] == '?')) {
                sIndex++;
                pIndex++;
            } else if (pIndex < p.Length && p[pIndex] == '*') {
                sStarIndex = sIndex;
                pStarIndex = pIndex;
                pIndex++;
            } else if (pStarIndex != -1) {
                sStarIndex++;
                sIndex = sStarIndex;
                pIndex = pStarIndex + 1;
            } else {
                return false;
            }
        }
        while (pIndex < p.Length && p[pIndex] == '*') {
            pIndex++;
        }
        return pIndex == p.Length;
    }
}