public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> map = new Dictionary<string, List<string>>();
        foreach(string s in strs){
            char[] c = s.ToCharArray();
            Array.Sort(c);
            string key = new string(c);
            if(!map.ContainsKey(key))
                map[key] = new List<string>();
            map[key].Add(s);
        }
        return new List<IList<string>>(map.Values);
    }
}