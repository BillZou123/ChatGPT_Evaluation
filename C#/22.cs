public class Solution {
    public IList<string> GenerateParenthesis(int n) {
        IList<string> result = new List<string>();
        Generate(n, "", result, 0, 0);
        return result;
    }

    private void Generate(int n, string current, IList<string> result, int open, int close) {
        if (current.Length == n * 2) {
            result.Add(current);
            return;
        }

        if (open < n) {
            Generate(n, current + "(", result, open + 1, close);
        }
        if (close < open) {
            Generate(n, current + ")", result, open, close + 1);
        }
    }
}