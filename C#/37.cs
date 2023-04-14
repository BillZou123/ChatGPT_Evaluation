public class Solution {
    public void SolveSudoku(char[][] board) {
        Solve(board, 0, 0);
    }
    
    private bool Solve(char[][] board, int row, int col) {
        if (col == 9) {
            row++;
            col = 0;
            if (row == 9) {
                return true;
            }
        }
        if (board[row][col] != '.') {
            return Solve(board, row, col + 1);
        }
        for (char num = '1'; num <= '9'; num++) {
            if (IsValid(board, row, col, num)) {
                board[row][col] = num;
                if (Solve(board, row, col + 1)) {
                    return true;
                }
                board[row][col] = '.';
            }
        }
        return false;
    }
    
    private bool IsValid(char[][] board, int row, int col, char num) {
        for (int i = 0; i < 9; i++) {
            if (board[row][i] == num || board[i][col] == num || board[3 * (row / 3) + i / 3][3 * (col