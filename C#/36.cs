public class Solution {
    public bool IsValidSudoku(char[][] board) {
        // Check each row
        for (int i = 0; i < 9; i++) {
            HashSet<char> seen = new HashSet<char>();
            for (int j = 0; j < 9; j++) {
                char c = board[i][j];
                if (c != '.') {
                    if (seen.Contains(c)) {
                        return false;
                    }
                    seen.Add(c);
                }
            }
        }
        // Check each column
        for (int j = 0; j < 9; j++) {
            HashSet<char> seen = new HashSet<char>();
            for (int i = 0; i < 9; i++) {
                char c = board[i][j];
                if (c != '.') {
                    if (seen.Contains(c)) {
                        return false;
                    }
                    seen.Add(c);
                }
            }
        }
        // Check each 3x3 sub-box
        for (int box = 0; box < 9; box++) {
            HashSet<char> seen = new HashSet<char>();
            for (int i = box / 3 * 3; i < box / 3 *