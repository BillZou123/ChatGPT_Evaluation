public class Solution {
    public IList<string> LetterCombinations(string digits) {
        Dictionary<char, string> dict = new Dictionary<char, string>()
        {
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };
        IList<string> result = new List<string>();
        if(digits.Length == 0) return result;
        result.Add("");
        foreach(char digit in digits)
        {
            IList<string> temp = new List<string>();
            foreach(char letter in dict[digit])
            {
                foreach(string combination in result)
                {
                    temp.Add(combination + letter);
                }
            }
            result = temp;
        }
        return result;
    }
}