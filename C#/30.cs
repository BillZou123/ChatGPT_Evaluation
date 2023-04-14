public class Solution {
    public IList<int> FindSubstring(string s, string[] words) {
        IList<int> result = new List<int>();
        int wordLength = words[0].Length;
        int concatLength = wordLength * words.Length;
        Dictionary<string, int> wordCount = new Dictionary<string, int>();
        foreach(string word in words) {
            if(!wordCount.ContainsKey(word)) {
                wordCount[word] = 0;
            }
            wordCount[word]++;
        }
        for(int i = 0; i <= s.Length - concatLength; i++) {
            Dictionary<string, int> seen = new Dictionary<string, int>();
            int j = 0;
            while(j < words.Length) {
                string word = s.Substring(i + j * wordLength, wordLength);
                if(!wordCount.ContainsKey(word)) {
                    break;
                }
                if(!seen.ContainsKey(word)) {
                    seen[word] = 0;
                }
                seen[word]++;
                if(seen[word] > wordCount[word]) {
                    break;
                }
                j++;
            }
            if(j == words.Length) {
                result.Add(i);
            }
        }
        return result;
    }
}